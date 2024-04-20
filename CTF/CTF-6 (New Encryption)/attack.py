import string
from decrypt import decrypt


def attack_one_char_key(cipher: str) -> list:
    """
    Attempt to decrypt a cipher text using all possible single character keys.

    Args:
    - cipher (str): The cipher text to decrypt.

    Returns:
    - list: A list of possible decrypted messages.
    """
    possible_msgs = []
    
    for i in string.ascii_lowercase[:16]: # iterate only on first 16 characters (as it only needed)
        msg = decrypt(cipher, i) # attempt decryption using this character
        
        # check if attempt is valid by checking if output msg is ascii
        if msg.isascii():
            possible_msgs.append(msg)
        
    return possible_msgs
        
if __name__ == "__main__":
    with open("cipher.txt", "r") as cipher_file:
        cipher = cipher_file.read()
        
        possible_msgs = attack_one_char_key(cipher)

        with open("possible_results.txt", "w") as out_file:
            out_file.write("\n".join(possible_msgs))
        