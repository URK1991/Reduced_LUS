# main.py
from image_processing import process_image, process_directory

def main():
    # Input and output paths
    input_path = " "  # Change this to your input image or directory
    output_path = " "  # Change this to your output directory or image path
    
    # Specify the downsampling and quantization factors
    downsample_factor = 2  # Change to 1, 2, 3, or 4
    quantize_factor = 4    # Change to 1, 2, 4, or 8
    
    # Flag indicating whether the input is a directory
    is_directory = True  # Change to True if input_path is a directory

    # Process directory or single image based on the is_directory flag
    if is_directory:
        process_directory(input_path, output_path, downsample_factor, quantize_factor)
    else:
        process_image(input_path, downsample_factor, quantize_factor, save=True, output_path=output_path)

if __name__ == "__main__":
    main()
