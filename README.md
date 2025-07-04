# 🎙️ Audio Recorder with Python

A simple Python script to record audio from your microphone and save it as a `.wav` file using the `sounddevice` and `wavio` libraries.

---

## 📌 Features

- Records audio in stereo (2 channels)
- Sampling frequency of 44.1 kHz (CD quality)
- Saves output as `recording1.wav`
- Easy to modify for custom duration or sample width

---

## 🛠️ Requirements

- Python 3.x  
- [sounddevice](https://pypi.org/project/sounddevice/)  
- [wavio](https://pypi.org/project/wavio/)

Install them using pip:

```bash
pip install sounddevice wavio

