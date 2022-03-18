import io
import streamlit as st
from pydub import AudioSegment

filestream = io.BytesIO()
uploaded_mp3_file = st.file_uploader('Upload Your MP3 File', type=['mp3'])

if uploaded_mp3_file:
    if len(uploaded_mp3_file.getvalue()) > 0:
        st.text(f'uploaded_mp3_file: {len(uploaded_mp3_file.getvalue())} bytes')
        # do some processing here with the mp3 file
        song = AudioSegment.from_mp3(uploaded_mp3_file)
        handler = song.export(filestream, format="wav")

if filestream:
    if len(filestream.getvalue()) > 0:
        st.download_button(label="Download wav file",
                data=filestream.getvalue(),
                file_name="newaudio.wav",
                mime='audio/wav')
        st.text(f'filestream: {len(filestream.getvalue())} bytes')
