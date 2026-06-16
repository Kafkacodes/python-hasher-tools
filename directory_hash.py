directory = input("Enter the directory path: ")

import os
files = os.listdir(directory)  # List all files in the specified directory
print(files)

import hashlib

for file in files:  # Print the name of each file in the directory
    filepath = os.path.join(directory, file)  # Get the full path of the file
    
    if os.path.isfile(filepath):
        print(filepath)

        with open(filepath, 'rb') as f:  # Open the file in binary read mode
            file_data = f.read()  # Read the contents of the file

        hash_value = hashlib.sha256(file_data).hexdigest()  # Hash the file contents using SHA-256
        print(f"Hash value: {hash_value}")