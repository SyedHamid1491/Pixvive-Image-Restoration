import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as compare_psnr

# === Configure your image paths here ===
original_path = r'C:\pjs\res\Project-Work1\Img_ClrPlusEnchancer\images\2.jpg'
enhanced1_path = r'C:\pjs\res\Project-Work1\Img_ClrPlusEnchancer\output\color.jpg'
enhanced2_path = r'C:\pjs\res\Project-Work1\Img_ClrPlusEnchancer\output\enhanced.jpg'

def print_stats(name, orig, enh):
    # Resize enhanced to match original  if needed
    if orig.shape != enh.shape:
        enh = cv2.resize(enh, (orig.shape[1], orig.shape[0]))

    diff = cv2.absdiff(orig, enh)
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    mean_diff = np.mean(diff_gray)
    max_diff = np.max(diff_gray)
    psnr = compare_psnr(orig, enh, data_range=255)

    print(f"--- {name} ---")
    print(f"Mean pixel difference: {mean_diff:.2f}")
    print(f"Max pixel difference: {max_diff}")
    print(f"PSNR: {psnr:.2f} dB")

    # Plot histogram of pixel differences
    plt.figure(figsize=(6,4))
    plt.hist(diff_gray.ravel(), bins=50, color='blue', alpha=0.7)
    plt.title(f'Pixel Difference Histogram: {name}')
    plt.xlabel('Pixel difference (0-255)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def compare_three_images(original_path, enhanced1_path, enhanced2_path):
    orig = cv2.imread(original_path)
    enh1 = cv2.imread(enhanced1_path)
    enh2 = cv2.imread(enhanced2_path)

    if orig is None or enh1 is None or enh2 is None:
        print("Error: One or more image paths are invalid.")
        return

    print_stats('Original vs colored', orig, enh1)
    print_stats('Original vs Enhanced2', orig, enh2)
    print_stats('colored vs Enhanced2', enh1, enh2)

# === Run the comparison ===
compare_three_images(original_path, enhanced1_path, enhanced2_path)
