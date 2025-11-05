# Download Kaggle dataset: speech-emotion-recognition

This repository helper includes a script to download the Kaggle dataset `shivamburnwal/speech-emotion-recognition`.

Prerequisites
- Python 3.8+ (you already have a notebook kernel configured)
- pip
- A Kaggle account and API token

Steps
1. Install the kaggle package:

   python -m pip install kaggle

2. Place your Kaggle API token JSON file at `~/.kaggle/kaggle.json` with permissions 600:

   mkdir -p ~/.kaggle
   # move the downloaded kaggle.json into ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json

3. Run the download script:

   python scripts/download_kaggle_dataset.py --dest datasets/kaggle_speech_emotion

The script will download and unzip the dataset into the destination directory.

Notes
- I cannot download datasets on your behalf. You must provide your own Kaggle API token.
- If you prefer using the Kaggle web UI, you can also download manually and place the files in `datasets/kaggle_speech_emotion/`.
