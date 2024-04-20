import string

START = ord("a")
CHARSET = string.ascii_lowercase[:16]


def __decode_b16(cipher: str) -> str:
    """
    Decode a binary 16 string.

    Args:
    - cipher (str): The binary string to decode.

    Returns:
    - str: The decoded message.
    """
    msg = ""
    
    for i in range(0, len(cipher), 2):
        b1 = "{0:04b}".format(ord(cipher[i]) - START) 
        b2 = "{0:04b}".format(ord(cipher[i+1]) - START) 
    
        msg += chr(int(b1 + b2, 2))
        
    return msg
        
def decrypt(cipher: str, key: str) -> str:
    """
    Decrypt a cipher text using a key.

    Args:
    - cipher (str): The cipher text to decrypt.
    - key (str): The key to use for decryption.

    Returns:
    - str: The decrypted message.
    """
    msg_b16 = ""

    # loop on cipher text
    for i, c in enumerate(cipher):
        shift = (ord(c) - ord(key[i % len(key)])) % len(CHARSET)
        msg_b16 += CHARSET[shift]
        
    return __decode_b16(msg_b16)


