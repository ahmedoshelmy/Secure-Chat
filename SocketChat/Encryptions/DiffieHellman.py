import random
from . import NumberTheory


class DiffieHellman:
    """
    A class to represent the Diffie-Hellman key exchange protocol.
    """

    def __init__(self, q, a):
        """
        Initializes the DiffieHellman object with a prime number (q) and a generator (a).

        Args:
          q: A large prime number.
          a: A primitive root modulo the prime number.
        """
        self.number_theory = NumberTheory.NumberTheory()
        self.q = q
        self.a = a
        self.x = random.randint(0, self.q - 1)  # Private Key
        # Binary Exponentiation for large numbers
        self.y = self.number_theory.binary_exponentiation(self.a, self.x, self.q) % self.q  # Public Key


    def calculate_shared_secret_key(self, other_public_key):
        """
        This function is a placeholder for calculating the shared secret key using the Diffie-Hellman algorithm.

        Args:
          other_public_key: The public key of the other party.

        Returns:
          Shared Secret Key
        """
        return self.number_theory.binary_exponentiation(other_public_key, self.x, self.q)

    def get_public_key(self):
        return self.y
