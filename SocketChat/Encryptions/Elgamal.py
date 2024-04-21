import random
from . import NumberTheory


class Elgamal:
    def __init__(self, q, a):
        self.q = q  # Prime number
        self.a = a  # Element in multiplicative group modulo q
        self.x = random.randint(1, self.q - 1)  # Private key
        self.y = pow(self.a, self.x, self.q)  # Public key

    def sign_message(self, message):
        """Encrypts a message (plaintext) using the public key."""
        if message >= self.q:
            raise ValueError("Message cannot be greater than or equal to q.")

        number_theory = NumberTheory.NumberTheory()
        k = number_theory.get_coprime_number(self.q - 1)
        k_inverse = number_theory.mod_inverse(k, self.q - 1)
        s1 = pow(self.a, k, self.q)
        s2 = k_inverse * (message - self.x * s1) % (self.q - 1)
        return s1, s2

    def verify_signature(self, message, s1, s2, y):
        """Verifies the signature of a message (plaintext)

            Args:
          message: Encrypted message
          s1 and s2: signature
          y: public key of sender
        Returns:
          Message: Decrypted message
        """
        v1 = pow(self.a, message, self.q)
        v2 = pow(y, s1, self.q) * pow(s1, s2, self.q) % self.q
        return v1 == v2

    def get_public_key(self):
        return self.y
