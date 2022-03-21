[![Open in Streamlit Cloud](https://img.shields.io/badge/Open%20in-Streamlit%20Cloud-F24747?logo=streamlit)](https://share.streamlit.io/franky1/streamlit-pydub-test/main) 
![License](https://img.shields.io/github/license/Franky1/Streamlit-Pydub-Test?logo=github) 
![Language](https://img.shields.io/github/languages/top/Franky1/Streamlit-Pydub-Test?logo=python) 
![Python Version](https://img.shields.io/badge/Python-3.7%20|%203.8%20|%203.9-blue?logo=python) 
![Issues](https://img.shields.io/github/issues/Franky1/Streamlit-Pydub-Test?logo=github) 
![Last Commit](https://img.shields.io/github/last-commit/Franky1/Streamlit-Pydub-Test?logo=github)

# Streamlit Pydub Test

Streamlit App for testing **pydub** on Streamlit Cloud.

## Issues

There are some issues with `ffmpeg` and `pydub` on Streamlit Cloud.
Quick fix is to use `libav` instead of `ffmpeg` in `packages.txt` file.
Pydub prefers `libav` over `ffmpeg` if it is installed.

## Status

This is just a quick example project to test Pydub on Streamlit Cloud.

> Last changes: 20.03.2022
