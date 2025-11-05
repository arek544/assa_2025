#%%
import os
import pandas as pd
import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Set your target directory
# directory = '/path/to/your/aiff/files'  # Change this to your actual path
directory_right_whale = r"\ASSA - Oct 2025\whale-detection-challenge\small_data_sample_revised\small_data_sample\right_whale"
directory_no_right_whale = r"\ASSA - Oct 2025\whale-detection-challenge\small_data_sample_revised\small_data_sample\no_right_whale"

def read_aiff_in_directory_to_dataframe(directory):
    # List to collect data
    data = []

    # Loop through files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith('.aiff'):
            filepath = os.path.join(directory, filename)
            try:
                # Read audio file
                audio_data, samplerate = sf.read(filepath)
                num_channels = audio_data.shape[1] if audio_data.ndim > 1 else 1
                num_frames = audio_data.shape[0]

                # Store metadata and waveform preview
                data.append({
                    'filename': filename,
                    'samplerate': samplerate,
                    'channels': num_channels,
                    'frames': num_frames,
                    # 'waveform_preview': audio_data[:100]  # First 100 samples
                    'waveform': audio_data  # First 100 samples
                })
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    # Create DataFrame
    df = pd.DataFrame(data)
    return df

df_right_whale = read_aiff_in_directory_to_dataframe(directory_right_whale)
df_no_right_whale = read_aiff_in_directory_to_dataframe(directory_no_right_whale)
# Display the DataFrame
print(df_right_whale.head())
#%%

# Play the audio
audio = np.row_stack(df_no_right_whale['waveform'].values)[4]
sample_rate = df_right_whale['samplerate'].values[4]
sd.play(audio, samplerate=sample_rate)
sd.wait()  # Wait until playback is finished
