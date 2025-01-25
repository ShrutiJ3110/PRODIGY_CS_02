# Image Encryption and Decryption Tool

This is a Python-based tool developed as part of my Cyber Security internship at Prodigy InfoTech. The tool allows users to encrypt and decrypt images using different cryptographic methods.

## Features
- **Channel Swap Method**: Swaps the red and blue channels of an image for encryption.
- **Mathematical Operations**: Performs encryption/decryption on pixel values using basic mathematical operations (addition, subtraction, multiplication, division) with a user-defined key.
- **Supports batch processing** for multiple images (PNG, JPG, JPEG).
- Provides flexibility for encrypting and decrypting images in a folder.

## Installation
To use this tool, ensure you have Python 3.x installed on your machine.

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/PRODIGY_CS_02.git
cd PRODIGY_CS_02

**### Step 2: Install Required Libraries**
Ensure you have Python installed on your system. Install the necessary libraries by running:
```bash
pip install -r requirements.txt

**### Step 3: Run the Tool**

You can use the following commands to encrypt or decrypt images in a folder.

#### To encrypt images:
```bash
python image_encryption_decryption.py encrypt

#### To decrypt images:
```bash
python image_encryption_decryption.py decrypt



### **Method Choices**

When running the tool, you will be prompted to choose between the following encryption methods:

- **swap**: Swaps the red and blue channels of the image.
- **math**: Performs a mathematical operation (add, subtract, multiply, divide) with a user-defined key.

### **Supported Image Formats**
- PNG
- JPG
- JPEG

### **Example**
After running the script, encrypted or decrypted images will be saved in the `output_images` folder.


### **Code Walkthrough**

#### **Functions:**

- **encrypt_image**: Encrypts the image based on the selected method and key.
- **decrypt_image**: Decrypts the image using the reverse process of encryption.
- **process_images**: Processes all images in a specified folder based on the chosen action (encrypt or decrypt).

## Let's Connect!

Dive into the repository, share your thoughts, or reach out for discussions on programming, algorithms, or any related topics. I'm excited to learn and grow together with like-minded individuals!

## Contact Information

For questions, feedback, or collaboration opportunities, feel free to reach out.

- **Email:** [shrutisjoshi3110@gmail.com](mailto:shrutisjoshi3110@gmail.com)  
- **LinkedIn:** [linkedin.com/in/shruti-joshi-572820297/](https://www.linkedin.com/in/shruti-joshi-572820297))


Thank you for your interest in this project. Happy coding! 🚀




