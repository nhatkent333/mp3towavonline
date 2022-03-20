# Streamlit Pydub Test

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/franky1/streamlit-pydub-test/main)

Streamlit App for testing **pydub** on Streamlit Cloud.

## Issues

There are some issues with `ffmpeg` and `pydub` on Streamlit Cloud.
Quick fix is to use `libav` instead of `ffmpeg` in `packages.txt` file.
Pydub prefers `libav` over `ffmpeg` if it is installed.

## Status

This is just a quick example project to test Pydub on Streamlit Cloud.

> Last changes: 20.03.2022
