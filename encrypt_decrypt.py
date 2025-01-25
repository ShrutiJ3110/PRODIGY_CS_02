import os
from PIL import Image
import numpy as np

def encrypt_image(img, method, operation=None, key=None):
    """Encrypt the image based on the chosen method."""
    img_array = np.array(img)
    
    if method == "swap":
        # Swap red and blue channels for encryption
        img_array[:, :, [0, 2]] = img_array[:, :, [2, 0]]
    elif method == "math" and operation and key is not None:
        img_array = img_array.astype(np.int32)  # Convert to avoid overflow
        if operation == "add":
            img_array = (img_array + key) % 256
        elif operation == "subtract":
            img_array = (img_array - key) % 256
        elif operation == "multiply":
            img_array = (img_array * key) % 256
        elif operation == "divide":
            if key == 0:
                raise ValueError("Division by zero is not allowed.")
            img_array = (img_array // key) % 256
        img_array = img_array.astype(np.uint8)  # Convert back to uint8
    
    return Image.fromarray(img_array)

def decrypt_image(img, method, operation=None, key=None):
    """Decrypt the image based on the chosen method."""
    img_array = np.array(img)
    
    if method == "swap":
        # Swap red and blue channels back for decryption
        img_array[:, :, [0, 2]] = img_array[:, :, [2, 0]]
    elif method == "math" and operation and key is not None:
        img_array = img_array.astype(np.int32)  # Convert to avoid overflow
        if operation == "add":
            img_array = (img_array - key) % 256  # Reverse addition with subtraction
        elif operation == "subtract":
            img_array = (img_array + key) % 256  # Reverse subtraction with addition
        elif operation == "multiply":
            try:
                inverse_key = pow(key, -1, 256)  # Ensure key has an inverse under mod 256
                img_array = (img_array * inverse_key) % 256  # Reverse multiplication
            except ValueError:
                print("Error: The key is not invertible for multiplication!")
                return img
        elif operation == "divide":
            img_array = (img_array * key) % 256  # Reverse division with multiplication
        img_array = img_array.astype(np.uint8)  # Convert back to uint8
    
    return Image.fromarray(img_array)

def process_images(action, folder="example_images", output_folder="output_images"):
    """Encrypt or decrypt all images in the folder."""
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    
    # Ensure the user selects a method and a key for the operation
    method = input("Choose a method ('swap' or 'math'): ").strip().lower()
    
    operation = None
    key = None

    if method == "math":
        operation = input("Choose a mathematical operation ('add', 'subtract', 'multiply', 'divide'): ").strip().lower()
        key = int(input("Enter the key (integer): "))
    
    # Ensure the same method and key are used for both encryption and decryption
    if action == "encrypt":
        print(f"Encrypting images using method '{method}' and key '{key}'...")
    elif action == "decrypt":
        print(f"Decrypting images using method '{method}' and key '{key}'...")
    
    for filename in os.listdir(folder):
        if filename.lower().endswith(("png", "jpg", "jpeg")):
            input_path = os.path.join(folder, filename)
            try:
                img = Image.open(input_path).convert("RGB")
                if action == "encrypt":
                    output_path = os.path.join(output_folder, f"encrypted_{filename}")
                    encrypted_img = encrypt_image(img, method, operation, key)
                    encrypted_img.save(output_path)
                    print(f"Encrypted '{filename}' -> '{output_path}'")
                elif action == "decrypt":
                    output_path = os.path.join(output_folder, f"decrypted_{filename}")
                    decrypted_img = decrypt_image(img, method, operation, key)
                    decrypted_img.save(output_path)
                    print(f"Decrypted '{filename}' -> '{output_path}'")
            except Exception as e:
                print(f"Error processing file '{filename}': {e}")
    
    print(f"All {action}ed images are saved in '{output_folder}'.")

# Main program
print("Do you want to encrypt or decrypt images?")
action = input("Enter 'encrypt' or 'decrypt': ").strip().lower()

# Process all images based on user action
process_images(action)