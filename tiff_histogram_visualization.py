import numpy as np
import matplotlib.pyplot as plt
import rasterio

# --- 1. Load SAR TIFF Data ---
# Open the SAR satellite TIFF file and read the single grayscale band
tiff_file_path = 'your_sar_image.tif'
with rasterio.open(tiff_file_path) as src:
    # Read the first (and usually only) band representing backscatter intensity
    sar_masked = src.read(1) 

# (Assumed preprocessing step from your pipeline)
# sar_masked[(land_mask | other_masks)] = 0

# --- 2. Prepare Data for Histogram ---
# Flatten the array and filter out the 0 values (masked areas)
# This prevents the '0' values from skewing the histogram scale.
valid_sar_pixels = sar_masked[sar_masked > 0].flatten()

# --- 3. Define Bins ---
# Grouping pixel intensities. 
# (Keep as 1-255 if your SAR image is scaled to 8-bit)
hist_bins = np.arange(1, 256, 5)

# --- 4. Plot the Histogram ---
plt.figure(figsize=(10, 6))

# Updated to use a gray color palette appropriate for SAR backscatter
plt.hist(valid_sar_pixels, bins=hist_bins, color='dimgray', edgecolor='black', alpha=0.7)

# --- 5. Add Adaptive Threshold Lines ---
# (These are hardcoded here for visualization, but would be dynamic in your loop)
ow_cut_min = 35 
ow_cut_max = 70 

# Draw the vertical lines indicating the open water cuts
# Using bright colors (blue/cyan) so they stand out against the gray histogram
plt.axvline(x=ow_cut_min, color='blue', linestyle='dashed', linewidth=2, label=f'ow_cut_min ({ow_cut_min})')
plt.axvline(x=ow_cut_max, color='cyan', linestyle='dashed', linewidth=2, label=f'ow_cut_max ({ow_cut_max})')

# --- 6. Format and Save Graph ---
plt.title('SAR Backscatter Intensity Histogram')
plt.xlabel('Pixel Intensity (Backscatter)')
plt.ylabel('Frequency (Pixel Count)')
plt.legend()
plt.grid(axis='y', alpha=0.5)

# Save the output
plt.savefig('ice_mask_hist_sar.png', bbox_inches='tight')
plt.show()