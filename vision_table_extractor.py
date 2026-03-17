"""
Image-based table extraction with fallback to online OCR
Uses optional EasyOCR or PaddleOCR if available, otherwise suggests online alternatives
"""

from PIL import Image
from typing import Dict, List, Any
import os

# Try to import optional OCR libraries
try:
    import easyocr
    EASYOCR_AVAILABLE = True
except ImportError:
    EASYOCR_AVAILABLE = False

try:
    from paddleocr import PaddleOCR
    PADDLEOCR_AVAILABLE = True
except ImportError:
    PADDLEOCR_AVAILABLE = False


class TableExtractor:
    def __init__(self, hf_token: str = None):
        """Initialize table extractor with fallback options"""
        self.token = hf_token
        self.ocr_engine = None
        self.engine_type = None
        self.available = False
        
        # Try EasyOCR first
        if EASYOCR_AVAILABLE:
            try:
                print("[INFO] Loading EasyOCR...")
                self.ocr_engine = easyocr.Reader(['en'], gpu=False, verbose=False)
                self.engine_type = 'easyocr'
                self.available = True
                print("[OK] EasyOCR ready")
                return
            except Exception as e:
                print(f"[WARN] EasyOCR failed: {str(e)[:50]}")
        
        # Try PaddleOCR second
        if PADDLEOCR_AVAILABLE:
            try:
                print("[INFO] Loading PaddleOCR...")
                self.ocr_engine = PaddleOCR(use_angle_cls=True, lang='en')
                self.engine_type = 'paddleocr'
                self.available = True
                print("[OK] PaddleOCR ready")
                return
            except Exception as e:
                print(f"[WARN] PaddleOCR failed: {str(e)[:50]}")
        
        # No OCR available - provide guidance
        print("[INFO] No local OCR available")
        self.available = False
    
    def extract_table_from_image(self, image_input) -> Dict[str, Any]:
        """Extract table from image using available OCR"""
        
        if not self.available:
            return {
                'headers': [],
                'rows': [],
                'rows_detected': 0,
                'columns_detected': 0,
                'status': 'fallback',
                'message': 'Local OCR not available. Use the "Paste Data" tab or online OCR tools.'
            }
        
        try:
            # Load image
            if isinstance(image_input, str):
                if not os.path.exists(image_input):
                    return {
                        'headers': [],
                        'rows': [],
                        'status': 'error',
                        'message': f'Image not found'
                    }
                image_path = image_input
            else:
                # Save PIL image temporarily
                image_path = 'temp_ocr.jpg'
                image_input.save(image_path)
            
            # Run OCR based on available engine
            if self.engine_type == 'easyocr':
                results = self.ocr_engine.readtext(image_path)
                text_items = self._parse_easyocr(results)
            elif self.engine_type == 'paddleocr':
                results = self.ocr_engine.ocr(image_path, cls=True)
                text_items = self._parse_paddleocr(results)
            else:
                return {'status': 'error', 'message': 'No OCR engine loaded'}
            
            if not text_items:
                return {
                    'headers': [],
                    'rows': [],
                    'status': 'error',
                    'message': 'No text detected in image'
                }
            
            # Group into table
            table_data = self._group_into_rows(text_items)
            
            if not table_data['rows']:
                return {
                    'headers': [],
                    'rows': [],
                    'status': 'error',
                    'message': 'Could not parse image as table'
                }
            
            return {
                'headers': table_data.get('headers', []),
                'rows': table_data.get('rows', []),
                'rows_detected': len(table_data.get('rows', [])),
                'columns_detected': len(table_data.get('headers', [])),
                'status': 'success',
                'message': f"Extracted {len(table_data.get('rows', []))} rows"
            }
        
        except Exception as e:
            return {
                'headers': [],
                'rows': [],
                'status': 'error',
                'message': f'Error: {str(e)[:80]}'
            }
    
    def _parse_easyocr(self, results):
        """Parse EasyOCR results"""
        items = []
        for detection in results:
            text = detection[1]
            confidence = detection[2]
            bbox = detection[0]
            y_pos = min([p[1] for p in bbox])
            items.append({'text': text, 'y': y_pos, 'conf': confidence})
        return items
    
    def _parse_paddleocr(self, results):
        """Parse PaddleOCR results"""
        items = []
        if results:
            for line in results:
                for word in line:
                    text = word[1][0]
                    confidence = word[1][1]
                    bbox = word[0]
                    y_pos = min([p[1] for p in bbox])
                    items.append({'text': text, 'y': y_pos, 'conf': confidence})
        return items
    
    def _group_into_rows(self, text_items: List[Dict]) -> Dict[str, List]:
        """Group detected text into table rows"""
        if not text_items:
            return {'headers': [], 'rows': []}
        
        # Sort by y-position
        text_items = sorted(text_items, key=lambda x: x['y'])
        
        # Group by vertical proximity
        rows_grouped = []
        current_row = [text_items[0]]
        
        for i in range(1, len(text_items)):
            if abs(text_items[i]['y'] - text_items[i-1]['y']) < 20:
                current_row.append(text_items[i])
            else:
                if current_row:
                    rows_grouped.append(current_row)
                current_row = [text_items[i]]
        
        if current_row:
            rows_grouped.append(current_row)
        
        # Extract rows
        extracted_rows = []
        for row_items in rows_grouped:
            row_text = [item['text'].strip() for item in row_items if item['text'].strip()]
            if row_text:
                extracted_rows.append(row_text)
        
        # First row = headers
        headers = extracted_rows[0] if extracted_rows else []
        rows = extracted_rows[1:] if len(extracted_rows) > 1 else []
        
        return {'headers': headers, 'rows': rows}


def extract_table(image_path_or_file, token: str = None) -> Dict[str, Any]:
    """Extract table from image"""
    extractor = TableExtractor(token)
    return extractor.extract_table_from_image(image_path_or_file)
