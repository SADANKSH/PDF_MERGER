from flask import Flask, render_template, request, send_file, flash
from werkzeug.utils import secure_filename
import os
from PyPDF2 import PdfMerger
import tempfile

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if any file was uploaded
        if 'files[]' not in request.files:
            flash('No files selected', 'error')
            return render_template('index.html')
        
        files = request.files.getlist('files[]')
        
        # Check if user selected files
        if not files or files[0].filename == '':
            flash('No files selected', 'error')
            return render_template('index.html')
        
        # Check if all files are PDFs
        if not all(allowed_file(f.filename) for f in files):
            flash('Please upload only PDF files', 'error')
            return render_template('index.html')
        
        try:
            merger = PdfMerger()
            
            # Create a temporary directory for processing
            with tempfile.TemporaryDirectory() as temp_dir:
                # Save and merge all files
                for file in files:
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        filepath = os.path.join(temp_dir, filename)
                        file.save(filepath)
                        merger.append(filepath)
                
                # Save the merged PDF
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')
                merger.write(output_path)
                merger.close()
                
                # Return the merged file
                return send_file(output_path, as_attachment=True, download_name='merged.pdf')
                
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('index.html')
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 