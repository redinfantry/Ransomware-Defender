import os
from cryptography.fernet import Fernet

# Reading the file path and key from user input
file_path = input("Enter the file path: ")
key = input("Enter the encryption key: ").encode()

# Loading the key to the Fernet instance
cipher = Fernet(key)

# Opening the encrypted file in binary mode and read its contents
with open(file_path, "rb") as f:
    encrypted_data = f.read()

# Decrypting the data using Fernet encryption
decrypted_data = cipher.decrypt(encrypted_data)

# Generating the file name for the decrypted file
decrypted_file_name = os.path.splitext(os.path.basename(file_path))[0] + "_decrypted.bin"

# Writing the decrypted data to a new file
with open(os.path.join(os.path.dirname(file_path), decrypted_file_name), "wb") as f:
    f.write(decrypted_data)

print(f"The decrypted file has been saved as: {decrypted_file_name}")
