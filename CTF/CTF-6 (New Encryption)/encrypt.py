import string

START = ord("a")
CHARSET = string.ascii_lowercase[:16]

def encode_b16(plain):
	encoded = ""
	for c in plain:
		# output 8 bit binary of order of character
		binary = "{0:08b}".format(ord(c)) 
		# encoded(char) = CHARSET[int(MSB)] + CHARSET[int(LSB)]
		encoded += (CHARSET[int(binary[:4], 2)] + CHARSET[int(binary[4:], 2)])
	return encoded

def caesar_shift(c, k):
    # input: character, key_character[i]
    # shift righ by (k)
	return CHARSET[(ord(c) + ord(k) - 2 * START) % len(CHARSET)]



flag = "secretkey"
# hint: key is a single letter
key = "b"

# encoded(char) = CHARSET[int(MSB_4)] | CHARSET[int(LSB_4)]
b16 = encode_b16(flag)
print(b16)
enc = ""
for i, c in enumerate(b16):
	enc += caesar_shift(c, key[i % len(key)])
print(enc)