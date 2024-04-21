from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad


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
        iv = get_random_bytes(16)  # Generate a random IV
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        print(type(data))
        padded_data = pad(data.encode(), AES.block_size)  # PKCS#7 padding
        ciphertext = cipher.encrypt(padded_data)
        return ciphertext, iv

    def decrypt(self, ciphertext, iv):
        """
        Decrypts ciphertext using AES-256 in CBC mode with PKCS#7 unpadding.

        Args:
            ciphertext: The encrypted data (bytes).
            iv: The initialization vector (IV) used for encryption (bytes).

        Returns:
            The decrypted plaintext (bytes).
        """
        if len(iv) != 16:
            raise ValueError("Initialization vector (IV) must be 16 bytes.")

        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(ciphertext)
        return unpad(decrypted_data, AES.block_size)  # PKCS#7 unpadding
