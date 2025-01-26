# Image Encryption and Decryption Tool

## Project Description

This Python-based tool allows you to encrypt and decrypt images using pixel manipulation techniques. The program supports two primary methods: **channel swapping** and **mathematical operations**. With its intuitive process, users can secure their images and restore them with ease. The tool is designed for simplicity, ensuring that users can handle image encryption and decryption efficiently.

## Features

- **Encryption Methods**:
  - **Channel Swap**: Swaps the red and blue channels of an image for encryption.
  - **Mathematical Operations**: Uses addition, subtraction, multiplication, or division with a key to alter pixel values.
- **Decryption Support**:
  - Reverses the encryption process using the same method and key.
- **Batch Processing**:
  - Automatically processes all images in a specified folder.
- **Customizable**:
  - Users can choose their preferred encryption method, mathematical operation, and key.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-encryption-tool.git
   cd image-encryption-tool

2. Install the required libraries:
   ```bash
   pip install pillow numpy

## Usage

### Prepare your images:
- Place the images you want to process in the `example_images` folder.

### Run the program:
    ```bash
    python image_encryption_tool.py

### Follow the prompts:
1. Choose an action: `encrypt` or `decrypt`.
2. Select the method: `swap` or `math`.
3. For mathematical operations:
   - Specify the operation: `add`, `subtract`, `multiply`, or `divide`.
   - Provide a key (an integer value).

### Processed images:
- Encrypted or decrypted images will be saved in the `output_images` folder.

### Example

#### Encryption:
- **Input**: `example_images/image1.jpg`
- **Method**: `math`
- **Operation**: `add`
- **Key**: `10`
- **Output**: `output_images/encrypted_image1.jpg`

#### Decryption:
- **Input**: `output_images/encrypted_image1.jpg`
- **Method**: `math`
- **Operation**: `add`
- **Key**: `10`
- **Output**: `output_images/decrypted_image1.jpg`

### Future Improvements
- Add support for more advanced encryption algorithms.
- Implement GUI-based user interaction.
- Enhance performance for larger images or datasets.

### License
This project is licensed under the MIT License.

### Contact
For questions, suggestions, or collaboration opportunities, reach out:

- Email: shrutisjoshi3110@gmail.com
- LinkedIn: [Shruti Joshi](https://www.linkedin.com/in/shruti-joshi-572820297)

Thank you for using this tool! Happy encrypting! 🚀







