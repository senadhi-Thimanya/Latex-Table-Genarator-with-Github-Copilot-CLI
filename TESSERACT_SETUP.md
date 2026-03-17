# Tesseract OCR Setup for Windows

Tesseract is a system-level application needed for table text extraction. Follow these steps:

## ✅ Quick Setup (Recommended)

### Option 1: Using Chocolatey (Easiest)

1. **Open PowerShell as Administrator**
2. Run:
```powershell
choco install tesseract
```

That's it! Tesseract will be installed automatically.

---

### Option 2: Manual Installation

If Chocolatey is not available or fails:

1. **Download Tesseract**
   - Visit: https://github.com/UB-Mannheim/tesseract/wiki/Downloads
   - Download: `tesseract-ocr-w64-v5.x.exe` (64-bit) or `tesseract-ocr-w32-v5.x.exe` (32-bit)

2. **Run the Installer**
   - Double-click the downloaded `.exe` file
   - Follow the setup wizard
   - **Remember the installation path** (usually `C:\Program Files\Tesseract-OCR`)

3. **Verify Installation**
   - Open Command Prompt or PowerShell
   - Run: `tesseract --version`
   - You should see version information

---

## 🔧 If Installed in Non-Standard Location

If you installed Tesseract somewhere other than `C:\Program Files\Tesseract-OCR`, edit:

`vision_table_extractor.py`

And change the `common_paths` list to include your installation:

```python
common_paths = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"YOUR_INSTALL_PATH\tesseract.exe",  # Add your path here
]
```

---

## ✅ Test Installation

After installing, restart the web server:

```bash
python app.py
```

Then try uploading a table image. It should now work! 🎉

---

## 🆘 Still Not Working?

1. Make sure Tesseract is installed: `tesseract --version`
2. Check the installation path matches in `vision_table_extractor.py`
3. Restart the Python server after installing Tesseract
4. Try uploading a test image

