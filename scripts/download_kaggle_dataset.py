"""
Helper script to download the Kaggle dataset `shivamburnwal/speech-emotion-recognition`.

Usage:
  1. Install the kaggle CLI or Python package: pip install kaggle
  2. Place your Kaggle API token at ~/.kaggle/kaggle.json (or set KAGGLE_USERNAME and KAGGLE_KEY env vars)
  3. Run: python scripts/download_kaggle_dataset.py --dest datasets/kaggle_speech_emotion

This script will attempt to use the `kaggle` CLI to download and unzip the dataset.
"""

import argparse
import os
import shutil
import subprocess
import sys

DATASET_SLUG = "ejlok1/toronto-emotional-speech-set-tess"


def check_kaggle_available():
    # try kaggle CLI directly
    try:
        subprocess.check_call(["kaggle", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


def download_dataset(dest_dir: str, force: bool = False):
    dest_dir = os.path.abspath(dest_dir)
    os.makedirs(dest_dir, exist_ok=True)

    if os.listdir(dest_dir) and not force:
        print(f"Destination '{dest_dir}' is not empty. Use --force to re-download.")
        return

    if not check_kaggle_available():
        print("ERROR: The kaggle package/CLI is not available. Install it with: python -m pip install kaggle")
        return

    # run kaggle datasets download
    print(f"Downloading dataset {DATASET_SLUG} to {dest_dir} (this requires your Kaggle API token)...")
    try:
        # Use the kaggle CLI command directly
        subprocess.check_call(["kaggle", "datasets", "download", "-d", DATASET_SLUG, "-p", dest_dir, "--unzip"])
        print("Download complete.")
    except subprocess.CalledProcessError as e:
        print("ERROR: kaggle download failed:", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Kaggle dataset: speech-emotion-recognition")
    parser.add_argument("--dest", default="datasets/kaggle_speech_emotion", help="Destination directory for the dataset")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files in dest")
    args = parser.parse_args()

    download_dataset(args.dest, force=args.force)
