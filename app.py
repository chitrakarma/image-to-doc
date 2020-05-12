from flask import Flask, render_template, request, jsonify, make_response
import pytesseract as tess
from PIL import Image
from docx import Document
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        filesize = request.cookies.get("filesize")
        file = request.files["file"]

        print(f"Filesize: {filesize}")

        # Converting image to text
        img = Image.open(file)
        text = tess.image_to_string(img)
        print(text)

        # Creating docx file
        doc = Document()
        para = doc.add_paragraph(text)
        doc.save(f"docs/{file.filename}.docx")

        res = make_response(jsonify({"messasge": f"{file.filename} uploaded"}))
        return res

    return render_template('index.html', name="Index")
