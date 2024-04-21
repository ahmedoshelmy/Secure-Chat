from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import base64


class AESCipher:
    """
    A class for AES encryption and decryption using PyCryptodome.
    """

    def __init__(self, key):
        """
        Initializes the AES object with a 32-byte key.

        Args:
            key: The 32-byte key for AES-256 encryption (bytes).
        """
        if len(key) != 32:
            raise ValueError("Key must be 32 bytes for AES-256.")

        self.key = key

    def encrypt(self, data):
        """
        Encrypts data using AES-256 in CBC mode with PKCS#7 padding.

        Args:
            data: The data to encrypt (bytes).

        Returns:
            The encrypted ciphertext (bytes) and the initialization vector (IV).
        """
        # Ensure data is bytes
        if not isinstance(data, bytes):
            data = data.encode()

        iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_data = pad(data, AES.block_size)  # PKCS#7 padding
        ciphertext = cipher.encrypt(padded_data)
        print("Enc", iv, ciphertext)
        print("Enc", self.key)
        return base64.b64encode(ciphertext).decode(), base64.b64encode(iv).decode()  # Encode IV to string

    def decrypt(self, ciphertext, iv):
        """
        Decrypts ciphertext using AES-256 in CBC mode with PKCS#7 unpadding.

        Args:
            ciphertext: The encrypted data (bytes).
            iv: The initialization vector (IV) used for encryption (bytes).

        Returns:
            The decrypted plaintext (bytes).
        """
        iv = base64.b64decode(iv)  # Decode IV from string
        ciphertext = base64.b64decode(ciphertext)
        if len(iv) != 16:
            raise ValueError("Initialization vector (IV) must be 16 bytes.")
        print("Dec", iv, ciphertext)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(ciphertext)
        print("Dec", self.key)
        return unpad(decrypted_data, AES.block_size)
