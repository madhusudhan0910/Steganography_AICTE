# Secure Data Hiding in Images Using Steganography

## Overview
This project implements **Least Significant Bit (LSB) Steganography** using **Python** to securely hide messages inside images. The encrypted images can later be decrypted using a passcode to extract the hidden message. This method ensures confidentiality while maintaining the image's visual integrity.

## Features
-  **LSB Steganography**: Hides messages in the least significant bits of image pixels.
-  **Passcode Protection**: Decryption requires a user-defined passcode.
-  **Minimal Data Alteration**: Ensures the image remains visually unchanged.
-  **Real-time Encryption & Decryption**: Instantly encrypt and retrieve messages.
-  **Cross-Platform Compatibility**: Works on Windows & Linux.

## Technology Used
- **Programming Language**: Python
- **Libraries**: OpenCV, NumPy, PIL (Pillow)
- **Algorithm**: Least Significant Bit (LSB) Steganography
- **Platform**: Windows/Linux

## Installation
Ensure **Python 3.7+** is installed, then install the required dependencies using:


pip install opencv-python numpy pillow


## Usage
### **1. Encryption (Hiding a Message in an Image)**
Run the script to embed a message into an image:


python encrypt.py

- Enter a **secret message**.
- Provide an **image file** (e.g., `polina-lavor-mIrSgbi0mrc-unsplash.jpg`).
- The **encrypted image** (`encryptedImage.png`) is generated.

### **2. Decryption (Extracting the Message from the Image)**
Retrieve the hidden message from the encrypted image:

python decrypt.py

- Enter the **passcode** to decrypt.
- The **hidden message** is displayed.

## Author
**Developed by:** Yerraguntla Madhu Sudhan  
**Institution:** GITAM University, Bangalore - Computer Science & Engineering (Cyber Security)

## License
This project is open-source under the **MIT License**.


