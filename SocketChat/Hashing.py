import hashlib, math


class Hashing:
    """
    A class to represent the SHA1 hashing algorithm
    """

    def __init__(self, q):
        """
        Initializes the Object with q to pick a hash that is from 0 to q-1

        Args:
          q: A large prime number.
        """
        self.q = q
        self.mask = (1 << (int(math.log(q, 2)))) - 1

    def hash(self, message):
        sha1_hash = hashlib.sha1(message.encode()).digest()
        digest_int = int.from_bytes(sha1_hash, byteorder='big')
        chosen_bits = digest_int & self.mask
        return chosen_bits

    def sha256(self, message):
        """
        Hashes the message using SHA-256 algorithm and returns the full digest (bytes).

        Args:
          message: The data to hash (bytes).

        Returns:
          The SHA-256 hash digest as bytes.
        """

        hash_function = hashlib.sha256()
        hash_function.update(message)
        return hash_function.digest()
