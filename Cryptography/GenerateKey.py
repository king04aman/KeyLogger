from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("encryption_key.txt", 'wb') as file:
  file.write(key)
