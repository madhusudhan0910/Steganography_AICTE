import cv2
import string

# Load image
img = cv2.imread("polina-lavor-mIrSgbi0mrc-unsplash.jpg")  # Replace with actual image
if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create ASCII mapping (Add NULL character '\x00' at the start)
ascii_chars = '\x00' + string.printable  
char_to_int = {char: i for i, char in enumerate(ascii_chars)}

h, w, _ = img.shape  # Get image dimensions
msg += '\x00'  # Add NULL character to mark end of message

n, m, z = 0, 0, 0

# Encrypt the message
for char in msg:
    if n >= h or m >= w:
        print("Error: Message too long for image!")
        exit()
    
    img[n, m, z] = char_to_int[char]  # Store ASCII index
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= w:
            m = 0
            n += 1

cv2.imwrite("encryptedImage.png", img)
print("Encryption complete. Encrypted image saved as 'encryptedImage.png'.")
