import streamlit as st
from predict import predict_emotion
import tempfile
import os

st.set_page_config(
    page_title="Emotion Detection",
    page_icon="🎤"
)

st.title("🎤 Human Emotion Detection from Voice")

uploaded_file = st.file_uploader(
    "Upload WAV or MP3",
    type=["wav", "mp3"]
)

if uploaded_file:

    st.audio(uploaded_file)

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(uploaded_file.name)[1]
    ) as tmp:

        tmp.write(uploaded_file.read())
        file_path = tmp.name

    emotion, confidence = predict_emotion(file_path)

    emoji_map = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😡",
        "fearful": "😨",
        "calm": "😌",
        "surprised": "😲",
        "disgust": "🤢"
    }

    emoji = emoji_map.get(emotion, "🎭")

    st.success(f"{emoji} Emotion: {emotion.title()}")
    st.metric("Confidence", f"{confidence}%")