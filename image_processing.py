# image_processing.py
from PIL import Image
import os
import matplotlib.pyplot as plt

def load_image_as_grayscale(image_path):
    """
    Load an image as grayscale.
    
    Args:
        image_path (str): Path to the input image.
        
    Returns:
        PIL.Image: Grayscale image.
    """
    image = Image.open(image_path).convert('L')  # 'L' mode ensures the image is in grayscale
    return image

def downsample_image(image, factor):
    """
    Downsample the grayscale image by a given factor.
    
    Args:
        image (PIL.Image): Grayscale input image to downsample.
        factor (int): The downsampling factor (1, 2, 3, 4).
        
    Returns:
        PIL.Image: Downsampled grayscale image.
    """
    if factor == 1:
        return image  # No downsampling
    width, height = image.size
    new_size = (width // factor, height // factor)
    downsampled_image = image.resize(new_size, Image.ANTIALIAS)
    return downsampled_image

def quantize_image(image, factor):
    """
    Quantize the grayscale image by a given factor (reduce color depth).
    
    Args:
        image (PIL.Image): Grayscale input image to quantize.
        factor (int): Quantization factor (1, 2, 4, 8).
        
    Returns:
        PIL.Image: Quantized grayscale image.
    """
    if factor == 1:
        return image  # No quantization
    quantized_image = image.quantize(colors=256 // factor)
    return quantized_image.convert('L')  # Convert back to grayscale after quantization

def downsample_and_quantize(image, downsample_factor, quantize_factor):
    """
    Downsample and quantize the grayscale image by given factors.
    
    Args:
        image (PIL.Image): Grayscale input image to process.
        downsample_factor (int): Downsampling factor (1, 2, 3, 4).
        quantize_factor (int): Quantization factor (1, 2, 4, 8).
        
    Returns:
        PIL.Image: Processed grayscale image.
    """
    downsampled = downsample_image(image, downsample_factor)
    result_image = quantize_image(downsampled, quantize_factor)
    return result_image

def process_image(input_path, downsample_factor, quantize_factor, save=False, output_path=None):
    """
    Load a grayscale image, apply downsampling and quantization, and optionally save the result.
    
    Args:
        input_path (str): Path to input image.
        downsample_factor (int): Downsampling factor (1, 2, 3, 4).
        quantize_factor (int): Quantization factor (1, 2, 4, 8).
        save (bool): Whether to save the processed image.
        output_path (str): Path to save the output image.
        
    Returns:
        None
    """
    image = load_image_as_grayscale(input_path)
    processed_image = downsample_and_quantize(image, downsample_factor, quantize_factor)
    plt.imshow(processed_image, cmap='gray')
    plt.axis('off')
    plt.show()
    
    if save and output_path:
        processed_image.save(output_path)
        print(f"Processed image saved at {output_path}")

def process_directory(input_dir, output_dir, downsample_factor, quantize_factor):
    """
    Process all images in a directory by applying downsampling and quantization.
    
    Args:
        input_dir (str): Path to the input directory containing images.
        output_dir (str): Path to the output directory to save processed images.
        downsample_factor (int): Downsampling factor (1, 2, 3, 4).
        quantize_factor (int): Quantization factor (1, 2, 4, 8).
    
    Returns:
        None
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            print(f"Processing {filename}...")
            process_image(input_path, downsample_factor, quantize_factor, save=True, output_path=output_path)
