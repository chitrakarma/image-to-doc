import os
from flask import Flask, render_template, request, jsonify, make_response
import pytesseract as tess
from PIL import Image
from docx import Document
from flask.helpers import send_from_directory
from os import abort
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
DOCS_FOLDER = 'docs/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOCS_FOLDER'] = DOCS_FOLDER


@app.route('/get-file/<file_name>')
def get_file(file_name):
    try:
        return send_from_directory(app.config['DOCS_FOLDER'], filename=file_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files["file"]

        # Converting image to text
        img = Image.open(file)
        text = tess.image_to_string(img)

        # Saving uploaded file
        filename = file.filename.split('.')[0]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Creating .docx file
        doc = Document()
        para = doc.add_paragraph(text)
        doc.save(f"docs/{filename}.docx")

        # Preparing a response
        res = make_response(jsonify(
            {"message": f"{file.filename} uploaded", "filename": f"{filename}", "text": text}))
        return res

    return render_template('index.html', name="Index")
