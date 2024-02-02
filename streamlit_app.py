import io
import pathlib

import streamlit as st
from pydub import AudioSegment

filename = None
filestream = io.BytesIO()

st.title('Chuyển đổi file MP3 sang WAV online')

st.markdown("""Công cụ chuyển đổi file MP3 sang WAV online. Thuộc dự án 1001 công cụ online [ViecLamVui.com](https://vieclamvui.com/ "tìm việc làm, tuyển dụng miễn phí") hỗ trợ cho hơn 100 ngành nghề.""")

uploaded_mp3_file = st.file_uploader('Upload Your MP3 File', type=['mp3'])

if uploaded_mp3_file:
    uploaded_mp3_file_length = len(uploaded_mp3_file.getvalue())
    if uploaded_mp3_file_length > 0:
        st.text(f'Size of uploaded mp3 file: {uploaded_mp3_file_length} bytes')
        audio_segment = AudioSegment.from_mp3(uploaded_mp3_file)
        # do some more processing here with the mp3 file(?)
        handler = audio_segment.export(filestream, format="wav")  # handler not needed
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
