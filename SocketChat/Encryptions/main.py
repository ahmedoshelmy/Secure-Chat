from DiffieHellman import DiffieHellman
from Elgamal import Elgamal
from Hashing import Hashing
from AESCipher import AESCipher


def read_key_pair(filename):
    """
    Reads 'q' and 'a' values for a DH or ElGamal key pair from a file.

    Args:
        filename: The name of the file containing the key pair information.

    Returns:
        A tuple containing (q, a) if successful, None otherwise.
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if len(lines) != 2:
                print(f"Error: Invalid key pair format in file {filename}")
                return None
            q = int(lines[0].strip())  # Assuming q is on the first line
            a = int(lines[1].strip())  # Assuming a is on the second line
            return q, a
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading key pair file {filename}: {e}")
        return None


def main():
    q_diff, a_diff = read_key_pair('diff_hellman_keys.txt')
    q_gamal, a_gamal = read_key_pair('elgamal_keys.txt')
    message = "Hello World!"
    diff_hellman = DiffieHellman(q_diff, a_diff)
    elgamal = Elgamal(q_gamal, a_gamal)
    elgamal2 = Elgamal(q_gamal, a_gamal)
    hashing = Hashing(q_gamal)

    key = diff_hellman.calculate_shared_secret_key(elgamal2.get_public_key())
    key256 = hashing.sha256(str(key).encode())
    aes_cipher = AESCipher(key256)
    encrypted_message, iv = aes_cipher.encrypt(message)
    print(encrypted_message)
    decrypted_message = aes_cipher.decrypt(encrypted_message, iv)
    print(decrypted_message)

    # Proving that when a different public key is sent the signature verifying failed
    m = hashing.hash(message)
    s1, s2 = elgamal.sign_message(m)
    print(elgamal.verify_signature(m, s1, s2, elgamal2.get_public_key()))


# If the script is executed directly (not imported as a module)
if __name__ == "__main__":
    main()
