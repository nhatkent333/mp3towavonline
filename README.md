# Streamlit Pydub Test

Streamlit App for testing Pydub on Streamlit Cloud.

## Issues

There are some issues with `ffmpeg` and `pydub` on Streamlit Cloud.
Quick fix is to use `libav` instead of `ffmpeg` in `packages.txt` file.
Pydub prefers `libav` over `ffmpeg` if it is installed.

## Status

This is just a quick example project to test Pydub on Streamlit Cloud.
Further improvement would be to make it also work with `ffmpeg`.

> Last changes: 18.03.2022
