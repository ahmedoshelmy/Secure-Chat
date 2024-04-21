import socketio
import eventlet
from Encryptions import Elgamal, DiffieHellman, Hashing
import json

sio = socketio.Client()

isVerified = False
elgamal_user_pk = None
isConnected = False


@sio.event
def connect():
    global isConnected
    isConnected = True
    print('connection established')


@sio.event
def disconnect():
    print('disconnected from server')


@sio.event
def KEY_EXCHANGE(data):
    global isConnected
    while (not isConnected):
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
    global deff_hellman_user_pk, deff_user_s1, deff_user_s2, isVerified, hashing, elgamal_user_pk
    print('DEFF_HELLMAN_PK_BC received:', data)
    json_data = json.loads(data)
    print(json_data["deff_public_key"])
    deff_hellman_user_pk = json_data["deff_public_key"]
    deff_user_s1 = json_data["s1"]
    deff_user_s2 = json_data["s2"]

    while (elgamal_user_pk == None):
        pass
    # verify the signature
    m = hashing.hash(message=str(deff_hellman_user_pk))
    print(f"m : {m}")
    isVerified = elgamal.verify_signature(m, deff_user_s1, deff_user_s2, int(elgamal_user_pk))

    if not isVerified:
        print("Signature verification failed")
        sio.disconnect()


@sio.event
def received_message(data):
    print(f"\nMessage received:{data}\nEnter a message")


if __name__ == '__main__':

    q_gamal = 1021
    a_gamal = 2
    elgamal = Elgamal.Elgamal(q_gamal, a_gamal)

    q_diff = 1021
    a_diff = 2
    diff_hellman = DiffieHellman.DiffieHellman(q_diff, a_diff)
    hashing = Hashing.Hashing(q_gamal)
    m = hashing.hash(message=str(diff_hellman.get_public_key()))
    s1, s2 = elgamal.sign_message(m)
    sio.connect('http://localhost:5000')

    while (1):
        if isVerified:
            message = input("Enter a message: ")
            if message == 'exit':
                break
            sio.emit('message', message)
