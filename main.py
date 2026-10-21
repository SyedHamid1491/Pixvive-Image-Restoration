import argparse
import cv2
import os
#  `python main.py --input ./images/2.jpg --colorized-out ./output/color.jpg --enhanced-out ./output/enhanced.jpg`
from models.colorizer import load_colorization_model, colorize_image
from models.enhancer import load_upsampler, enhance_image

def main(args):
    # Validate input image
    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Input image not found: {args.input}")

    # Load colorization model
    colorizer = load_colorization_model(
        'weights/colorization_deploy_v2.prototxt',
        'weights/colorization_release_v2.caffemodel',
        'weights/pts_in_hull.npy'
    )

    # Colorize the input image
    print("🎨 Colorizing image...")
    colorized_img = colorize_image(colorizer, args.input)
    cv2.imwrite(args.colorized_out, colorized_img)
    print(f"✅ Colorized image saved  to: {args.colorized_out}")

    # Load Real-ESRGAN model
    print("🔧 Enhancing image...")
    upsampler = load_upsampler('weights/RealESRGAN_x4plus.pth')
    enhanced_img = enhance_image(upsampler, colorized_img)
    cv2.imwrite(args.enhanced_out, enhanced_img)
    print(f"✅ Enhanced image saved to: {args.enhanced_out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Colorization + Enhancement CLI")
    parser.add_argument("--input", required=True, help="Path to grayscale input image")
    parser.add_argument("--colorized-out", default="colorized.jpg", help="Output path for colorized image")
    parser.add_argument("--enhanced-out", default="enhanced.jpg", help="Output path for enhanced image")
    
    args = parser.parse_args()
    main(args)