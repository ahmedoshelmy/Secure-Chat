import random


class Elgamal:
    def __init__(self, q, a):
        self.q = q  # Prime number
        self.a = a  # Element in multiplicative group modulo q
        self.x = random.randint(1, self.q - 1)  # Private key
        self.y = pow(self.a, self.x, self.q)  # Public key

    def encrypt(self, message):
        """Encrypts a message (plaintext) using the public key."""
        if message >= self.q:
            raise ValueError("Message cannot be greater than or equal to q.")

        k = random.randint(1, self.q - 1)  # Random key
        c1 = pow(self.a, k, self.q)
        c2 = message * pow(self.y, k, self.q) % self.q
        return c1, c2

    def decrypt(self, ciphertext):
        """Decrypts a ciphertext using the private key (x)
        Returns:
          Message: Decrypted message
        """
        if not self.x:
            raise ValueError("Private key not generated. Please generate a key first.")
        c1, c2 = ciphertext
        return pow(c2, -self.x, self.q) % self.q
