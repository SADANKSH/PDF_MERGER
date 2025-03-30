# PDF Merger

A simple web application that allows users to merge multiple PDF files into a single PDF document with drag-and-drop capability for arranging the order of pages.

## Features

- Upload multiple PDF files
- Drag and drop interface to arrange the order of PDFs before merging
- Remove individual PDFs from the selection
- Automatic download of the merged PDF file
- Responsive design for both desktop and mobile
- Error handling for various scenarios

## Requirements

- Python 3.6+
- Flask
- PyPDF2

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/pdf-merger.git
cd pdf-merger
```

2. Create a virtual environment and activate it:
```
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```
python app.py
```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`

3. Click "Choose PDF Files" to select multiple PDF files

4. Arrange the PDFs in your desired order using drag and drop

5. Click "Merge PDFs" to combine the files and download the result

## How to Arrange PDFs

1. Select multiple PDF files using the "Choose PDF Files" button
2. Drag and drop the files in the list to reorder them before merging
3. Use the "✕" button to remove any unwanted PDFs from the list
4. The PDFs will be merged in the order shown in the list (from top to bottom)

---

Created with ❤️ by SADANKSH GANGRADE - feel free to contact me for any questions or feedback! 