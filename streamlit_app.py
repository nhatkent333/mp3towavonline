import io
import pathlib

import streamlit as st
from pydub import AudioSegment

filename = None
filestream = io.BytesIO()

st.title('MP3 to WAV Converter test app')

st.markdown("""This is a quick example app for `pydub` on Streamlit Cloud.
There are some issues with `ffmpeg` and `pydub` on Streamlit Cloud.
Quick fix is to use `libav` instead of `ffmpeg` in `packages.txt` file.
Pydub prefers `libav` over `ffmpeg` if it is installed.
This example app uses `libav`.""")

uploaded_mp3_file = st.file_uploader('Upload Your MP3 File', type=['mp3'])

if uploaded_mp3_file:
    uploaded_mp3_file_length = len(uploaded_mp3_file.getvalue())
    if uploaded_mp3_file_length > 0:
        st.text(f'Size of uploaded mp3 file: {uploaded_mp3_file_length} bytes')
        # do some more processing here with the mp3 file(?)
        song = AudioSegment.from_mp3(uploaded_mp3_file)
        handler = song.export(filestream, format="wav")
        filename = pathlib.Path(uploaded_mp3_file.name).stem

if filestream and filename:
    content = filestream.getvalue()
    length = len(content)
    if length > 0:
        st.download_button(label="Download wav file",
                data=content,
                file_name=f'{filename}.wav',
                mime='audio/wav')
        st.text(f'Size of "{filename}.wav" file to download: {length} bytes')
