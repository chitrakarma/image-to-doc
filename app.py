import os
from flask import Flask, render_template, request, jsonify, make_response, send_file
import pytesseract as tess
from PIL import Image
from docx import Document
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files["file"]

        # Converting image to text
        img = Image.open(file)
        text = tess.image_to_string(img)

        # Saving file
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Creating docx file
        doc = Document()
        para = doc.add_paragraph(text)
        doc.save(f"docs/{filename}.docx")

        res = make_response(jsonify(
            {"message": f"{file.filename} uploaded", "filename": f"{file.filename}"}))
        return res

    return render_template('index.html', name="Index")
