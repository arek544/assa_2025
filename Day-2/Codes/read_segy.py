#%%
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


from obspy.io.segy.segy import _read_segy

file_folder = r"D:\Latop_Oct_2025\MATLAB\Marmousi"
file_name = "\data.segy"

# Load the SEGY file
stream = _read_segy(file_folder +file_name)
print(stream)


data = [trace.data for trace in stream.traces]
df = pd.DataFrame(data)

k = 1 # Shot number
plt.imshow(df.values[(96*(k-1)):(96*k),:700],aspect='auto',cmap = 'gray');
plt.grid()