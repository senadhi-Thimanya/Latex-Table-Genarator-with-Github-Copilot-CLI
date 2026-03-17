# Image Extraction Setup Guide

## Recommended: Tesseract OCR

Tesseract is the best choice for table extraction - it's free, open-source, and reliable.

### Installation

#### Windows
1. Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer (default installation is fine)
3. Install Pytesseract:
   ```bash
   pip install pytesseract
   ```
4. Restart your app:
   ```bash
   python app.py
   ```

#### macOS
```bash
brew install tesseract
pip install pytesseract
python app.py
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install tesseract-ocr
pip install pytesseract
python app.py
```

### Testing Tesseract Installation

After installation, verify it works:

```bash
# Check installation
tesseract --version

# Test with the app
python app.py
# Then upload an image in the "📷 Upload Image" tab
```

---

## Troubleshooting

### Problem: "Tesseract is not installed or it's not in your PATH"

**Solution:** 
1. Verify Tesseract is installed: Run `tesseract --version` in terminal
2. If not found, install from: https://github.com/UB-Mannheim/tesseract/wiki
3. After installation, restart the app

### Problem: Tesseract installed but still getting error

**Windows:**
- The installer may have installed to a custom path
- Try reinstalling to default location: `C:\Program Files\Tesseract-OCR`

**macOS/Linux:**
- Ensure `/usr/local/bin` is in your PATH
- Try: `export PATH="/usr/local/bin:$PATH"` before running the app

### Problem: Poor quality extraction

- Image must be clear and high contrast
- Try improving the image (brightness, sharpness)
- Or use https://www.onlineocr.net/ as fallback

---

## Alternative: Use Online OCR (No Installation Required)

If installing Tesseract is too complicated:

1. Go to https://www.onlineocr.net/
2. Upload your table image
3. Copy the extracted text
4. In the app, use the **"📋 Paste Data"** tab
5. Paste the extracted text
6. Generate LaTeX ✓

**This method always works and requires no installation!**

---

## Input Methods Summary

| Method | Setup | Speed | Quality |
|--------|-------|-------|---------|
| Paste Data | None | ⚡⚡⚡ | ✓ Perfect |
| Build Table | None | ⚡⚡ | ✓ Perfect |
| Tesseract OCR | 5 min | ⚡⚡ | ✓ Excellent |
| Online OCR + Paste | None | ⚡⚡⚡ | ✓ Good |

**Recommendation:** Start with Paste Data or Build Table (no setup), then optionally install Tesseract for automatic image extraction.
