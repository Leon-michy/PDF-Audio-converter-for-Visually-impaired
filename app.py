import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import send_from_directory
from ml.classifier import TextClassifier
from werkzeug.utils import secure_filename
import uuid
from pdf.extractor import PDFExtractor
from pdf.cleaner import TextCleaner
from tts.speech import SpeechGenerator
from services.pdf_service import PDFService

app = Flask(__name__)

app.secret_key = "project_secret_key"

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf"}

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )
    
@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "pdf" not in request.files:

        flash("No file selected.")

        return redirect("/")

    file = request.files["pdf"]
    voice = request.form.get(
        "voice"
    )


    speed = request.form.get(
        "speed"
    )

    if file.filename == "":

        flash("Please choose a PDF.")

        return redirect("/")

    if not allowed_file(file.filename):

        flash("Only PDF files are allowed.")

        return redirect("/")

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    service = PDFService()
    
    result = service.process(
        filepath,
        voice,
        speed
    )

    return render_template(
        "result.html",
        text=result["text"],
        audio_file=result["audio_file"],
        analysis=result["analysis"],
        document_info=result["document_info"],
        processing_time=result["processing_time"],
    )
@app.route("/audio/<filename>")
def audio(filename):
    return send_from_directory(
        "audio",
        filename
    )


if __name__ == "__main__":

    app.run(debug=True)