
from cryptography.fernet import Fernet

print("Starting script...")
key = Fernet.generate_key()
cipher_suite = Fernet(key)
token = cipher_suite.encrypt(b"this is a really secret message! Not for sharing!")
print(token) 


decrypted = cipher_suite.decrypt(token)
print("decrypted token =", decrypted)
print (decrypted.decode())






