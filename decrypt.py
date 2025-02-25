import cv2
import string

# Load encrypted image
img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Encrypted image not found!")
    exit()

password = input("Enter passcode for Decryption: ")

# Create mapping (Include NULL character)
ascii_chars = '\x00' + string.printable
int_to_char = {i: char for i, char in enumerate(ascii_chars)}

h, w, _ = img.shape  # Get image dimensions
message = ""
n, m, z = 0, 0, 0

print("\nExtracting message...")  

# Decryption loop
while True:
    if n >= h or m >= w:
        break

    char_index = int(img[n, m, z])  # Retrieve ASCII index
    char = int_to_char.get(char_index, '')  # Convert back to character

    if char == '\x00':  # Stop at NULL marker
        break
    message += char

    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= w:
            m = 0
            n += 1

print("\nDecrypted message:", message)
