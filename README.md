# Pixvive: AI Image Restoration Pipeline

**Project by Syed Hamid**

## Overview
Pixvive is an AI-powered image restoration tool that combines two CNN models to colourise and upscale old or grayscale images.

## Features
- Colourises images using Caffe in LAB colour space.
- Upscales images 2× using Real-ESRGAN.
- Provides a web interface built with Flask, React, and Tailwind CSS.

## Technologies
- **AI / Deep Learning:** CNN, Caffe, Real-ESRGAN
- **Backend:** Flask
- **Frontend:** React, Tailwind CSS
- **Evaluation:** PSNR, SSIM

## Results
- Processing time reduced by **15%**.
- Processes **5 images in approximately 80 seconds**.
- Reported **40% improvement in image quality** (PSNR/SSIM) over baseline grayscale inputs.
- Tested by **10 users** on a dataset of **100+ images**.

## Publication
Published as **“Pixvive: Reconstruction of Old Images Using a Dual CNN Pipeline”** in *IJIRT*, Volume 12, Issue 1 (2025).

## Disclaimer
This project was developed for learning and portfolio purposes. The reported performance results are based on the project's evaluation and should be interpreted in the context of its dataset and testing setup.
