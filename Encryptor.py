import os
import time
from datetime import datetime
from cryptography.fernet import Fernet

# Read the file path from user input
file_path = input("Enter the file path: ")

# Generating a new encryption key
key = Fernet.generate_key()

# Loading the key to the Fernet instance
cipher = Fernet(key)

# Opening the file in binary mode and read its contents
with open(file_path, "rb") as f:
    data = f.read()

# Encrypting the data using Fernet encryption
encrypted_data = cipher.encrypt(data)

# Getting the current date and time in the desired format
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Generating the file name with timestamp and extension
file_name = f"{timestamp}_encrypted.bin"

# Writing the encrypted data to the new file
with open(os.path.join(os.path.dirname(file_path), file_name), "wb") as f:
    f.write(encrypted_data)

# Printing the encryption key for future reference
print(f"The encryption key is: {key.decode()}")
