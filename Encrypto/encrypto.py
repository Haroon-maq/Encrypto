import subprocess

def encrypt(text, key):
    """Encrypts a string using OpenSSL AES-256-CBC with salt."""
    command = f'echo "{text}" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass pass:"{key}" -base64'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def decrypt(encrypted_text, key):
    """Decrypts an OpenSSL AES-256-CBC encrypted string."""
    command = f'echo "{encrypted_text}" | openssl enc -aes-256-cbc -d -salt -pbkdf2 -pass pass:"{key}" -base64'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        return "Decryption failed. Incorrect key or corrupted data."
    
    return result.stdout.strip()

print("Welcome to the Encryption/Decryption Tool!")
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

if choice == "e":
    text = input("Enter the text to encrypt: ")
    key = input("Enter a secure key: ")
    encrypted_text = encrypt(text, key)
    print(f"\nEncrypted Text:\n{encrypted_text}")

elif choice == "d":
    encrypted_text = input("Enter the encrypted text: ")
    key = input("Enter the key: ")
    decrypted_text = decrypt(encrypted_text, key)
    print(f"\nDecrypted Text:\n{decrypted_text}")

else:
    print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

