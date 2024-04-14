filename = 'bits.txt'

def convert_bits_msg(msg_bits):
    msg = ""
    for i in range(0, len(msg_bits), 8):
        msg += chr(int(msg_bits[i: i + 8], 2))
    return msg


with open(filename, 'rb') as infile:
    data = infile.read()
    flag = ""
    s = ""
    # shift all msg 1 bit to right
    msg_bits = ""
    for i in data:
        bits = bin(i)[2:].zfill(8)
        msg_bits += bits

    msg_bits_left = msg_bits[1:]
    msg_bits_left += "1"

    print(convert_bits_msg(msg_bits_left))
