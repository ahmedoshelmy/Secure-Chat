import socketio
from Encryptions import Elgamal, DiffieHellman, Hashing, AESCipher
import json

sio = socketio.Client()

is_verified = False
elgamal_user_pk = None
is_connected = False
aes_cipher = None


# -------------------------------------  Sockets -------------------------------------------------
@sio.event
def connect():
    global is_connected
    is_connected = True
    print('connection established')


@sio.event
def disconnect():
    print('disconnected from server')


@sio.event
def KEY_EXCHANGE(data):
    global is_connected
    while (not is_connected):
        pass
    print('KEY_EXCHANGE received:', data)
    print('Generating Elgamal public key...', elgamal.get_public_key())
    sio.emit('ELGAMAL_PK', str(elgamal.get_public_key()))


@sio.event
def ELGAMAL_PK_BC(data):
    global elgamal_user_pk
    print('ELGAMAL_PK_BC received:', data)
    elgamal_user_pk = data

    # emit deff hellman public key
    data_json = {
        "deff_public_key": diff_hellman.get_public_key(),
        "s1": s1,
        "s2": s2
    }

    message_str = json.dumps(data_json)

    sio.emit('DEFF_HELLMAN_PK', message_str)


@sio.event
def DEFF_HELLMAN_PK_BC(data):
    global deff_hellman_user_pk, deff_user_s1, deff_user_s2, is_verified, hashing, elgamal_user_pk, aes_cipher
    json_data = json.loads(data)
    deff_hellman_user_pk = json_data["deff_public_key"]
    deff_user_s1 = json_data["s1"]
    deff_user_s2 = json_data["s2"]
    print(json_data)

    while (elgamal_user_pk == None):
        pass
    # verify the signature
    m = hashing.hash(message=str(deff_hellman_user_pk))
    is_verified = elgamal.verify_signature(m, deff_user_s1, deff_user_s2, int(elgamal_user_pk))

    if not is_verified:
        print("Signature verification failed")
        sio.disconnect()
    else:
        shared_key = diff_hellman.calculate_shared_secret_key(int(deff_hellman_user_pk))
        print(f"shared_key: {shared_key}")
        key256 = hashing.sha256(str(shared_key).encode())
        aes_cipher = AESCipher.AESCipher(key256)


@sio.event
def received_message(data):
    message = json.loads(data)
    print("JSON MESSAGE RECEIVED", message)
    encrypted_message = message["message"]
    iv = message["iv"]
    decrypted_message = aes_cipher.decrypt(encrypted_message, iv).decode()
    print(f"\nMessage received:{decrypted_message}\nEnter a message")


# -------------------------------------  Sockets -------------------------------------------------


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


if __name__ == '__main__':

    # Reading Public Keys from Files
    q_diff, a_diff = read_key_pair('./Encryptions/diff_hellman_keys.txt')
    q_gamal, a_gamal = read_key_pair('./Encryptions/elgamal_keys.txt')

    # Initializing Encryption
    elgamal = Elgamal.Elgamal(q_gamal, a_gamal)
    diff_hellman = DiffieHellman.DiffieHellman(q_diff, a_diff)
    hashing = Hashing.Hashing(q_gamal)

    m = hashing.hash(message=str(diff_hellman.get_public_key()))
    s1, s2 = elgamal.sign_message(m)
    sio.connect('http://localhost:5000')
    print("Diff,S1,S2", diff_hellman.get_public_key(), s1, s2)
    while 1:
        if is_verified:
            message = input("Enter a message: ")
            if message == 'exit':
                break
            encrypted_message, iv = aes_cipher.encrypt(message)

            print("MESSAGE TO BE SENT", str(encrypted_message))
            message_json = {"message": str(encrypted_message), "iv": iv}
            message_str = json.dumps(message_json)
            sio.emit('message', message_str)
