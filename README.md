# PDF Merger

A simple web application built with Flask that allows you to merge multiple PDF files into a single PDF document.

## Features

- Upload multiple PDF files
- Merge PDFs with a single click
- Modern blue-themed UI
- Secure file handling
- Support for large files (up to 16MB)

## Setup

1. Install Python 3.7 or higher if you haven't already.

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Click the "Choose PDF Files" button to select multiple PDF files
2. The selected files will be displayed below the button
3. Click "Merge PDFs" to combine the files
4. The merged PDF will be automatically downloaded

## Notes

- The application only accepts PDF files
- Files are processed securely in a temporary directory
- Merged files are saved in the 'uploads' directory 