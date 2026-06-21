from flask import Flask, render_template, request
from predict import predict_emotion
import os
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def home():

    emotion = None
    confidence = None

    if request.method == "POST":

        audio_file = request.files["audio"]

        if audio_file.filename != "":

            filepath = os.path.join(
                UPLOAD_FOLDER,
                audio_file.filename
            )

            audio_file.save(filepath)

            emotion, confidence = predict_emotion(filepath)

    return render_template(
        "index.html",
        emotion=emotion,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)
