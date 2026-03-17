"""Flask web application for converting table images to LaTeX."""

import io

from flask import Flask, jsonify, render_template, request
from PIL import Image

from vision_table_extractor import TableExtractor
from table_to_latex import convert_to_latex

# Try to load HuggingFace token
try:
    from config import HF_TOKEN
    HAS_HF_TOKEN = bool(HF_TOKEN)
except Exception:
    HF_TOKEN = None
    HAS_HF_TOKEN = False

app = Flask(__name__, template_folder="templates")

# Initialize table extractor (lazy loading)
table_extractor = None

def get_extractor():
    """Get or initialize table extractor"""
    global table_extractor
    if table_extractor is None:
        print("Initializing table extractor...")
        table_extractor = TableExtractor(hf_token=HF_TOKEN if HAS_HF_TOKEN else None)
    return table_extractor


@app.route("/", methods=["GET"])
def serve_index():
    """Serve the main HTML page."""
    return render_template("index_simple.html")


@app.route("/api/generate-latex", methods=["POST"])
def generate_latex():
    """
    Generate LaTeX code from table data
    """
    data = request.get_json(silent=True) or {}
    try:
        headers = data.get("headers", [])
        rows = data.get("rows", [])

        if not headers or not rows:
            return jsonify({"error": "Headers and rows are required"}), 400

        latex_code = convert_to_latex(
            headers=headers,
            rows=rows,
            section_title=data.get("section_title"),
            caption=data.get("caption"),
            label=data.get("label"),
        )

        return (
            jsonify(
                {
                    "latex_code": latex_code,
                    "rows_count": len(rows),
                    "cols_count": len(headers),
                    "message": f"Generated LaTeX for {len(rows)} rows × {len(headers)} columns",
                }
            ),
            200,
        )

    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback

        traceback.print_exc()
        return jsonify({"error": f"Error generating LaTeX: {str(e)}"}), 500


@app.route("/api/extract-table", methods=["POST"])
def extract_table():
    """
    Extract table from image using HuggingFace Vision API
    """
    try:
        file = request.files.get("file")
        if file is None:
            return jsonify({"error": "Image file is required"}), 400

        # Validate file type
        if file.mimetype not in {"image/png", "image/jpeg", "image/jpg"}:
            return jsonify({"error": "Invalid file type. Please upload PNG or JPG image."}), 400

        # Read image
        contents = file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # Extract table
        print(f"Extracting table from image: {file.filename}")
        extractor = get_extractor()
        result = extractor.extract_table_from_image(image)

        if result["status"] == "error":
            return jsonify({"error": result["message"]}), 400

        # Return extracted data
        headers = result.get("headers", [])
        rows = result.get("rows", [])

        return (
            jsonify(
                {
                    "status": "success",
                    "headers": headers,
                    "rows": rows,
                    "rows_detected": len(rows),
                    "columns_detected": len(headers),
                    "message": f"Successfully extracted table with {len(rows)} rows and {len(headers)} columns",
                }
            ),
            200,
        )

    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback

        traceback.print_exc()
        return jsonify({"error": f"Error processing image: {str(e)}"}), 500


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    print("Starting Table to LaTeX Generator...")
    print("Open http://localhost:8000 in your browser")
    app.run(host="0.0.0.0", port=8000, debug=False)

