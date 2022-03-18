from cryptography.fernet import Fernet


class CryptEngine():

    def generate_key(self):
        key  = Fernet.generate_key()
        return key

    def encrypt_message(self, message, key):
        encoded_message = message.encode()
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message).decode()
        return encrypted_message

    def decrypt_message(self, message, key):
        encoded_message = message.encode()
        f = Fernet(key)
        decrypted_message = f.decrypt(encoded_message).decode()
        return decrypted_message
