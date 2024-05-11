
# CTF-8: Morse Code
### ***Problem Statement:***

The terrorists have caught someone in danger, can you find out where they are to help them ?

### ***Flag:***

THE RUSSIAN TERRORISTS ARE THE ONES WHO STARTED THIS, THEY ARE THE KEY. PLEASE YOU MUST EXTRACT ME


### ***Solution Walkthrough:***

Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations.
The flag in this problem was encoded using morse code and it was in the form of text after decoding the sent message using an online tool the following message was found:
```
THE RUSSIAN TERRORISTS ARE THE ONES WHO STARTED THIS, THEY ARE THE KEY. PLEASE YOU MUST EXTRACT ME.
```
At first i thought this would be the answer but it was suspicioud, the message clearly states that the russian terrorists are the key but how could they be a key ?!

This was super confusing a key to what ? there's no cipher text to be decrypted.

Now i have a key and nothing to open with so there must be cipher text hidden somewhere,
what better way to hide a message than steganography for sure the message was hidden in the audio file.

I used an online tool to find the embedded message in the audio file and voila here it is:
```
https://en.wikipedia.org/wiki/Nihilist_cipher?keyword=polybius

96 57 47 66 62 38 55 67 55 35 68 44 48 95 66 65 57 65 53 75 78 77 55 36 47 55 45 66 87 34 46 48 33 77
```
Now this should be easy to solve i have the cipher text and the key, after reading about the cipher everything started to make sense, this is a cipher made by a russian scientest to organize terrorism which matched the theme of the problem.

One last problem is that i couldn't build the matrix to solve the problem as i didn't know which word to use to build the matrix.

I tried ZEBRA, RUSSIAN and TERRORIST but none of them worked, then i looked back at the given link and found *polybius* , I thought there's no way this would work but to my surprise it was actually correct.

        1	2	3	4	5
    1	P	O	L	Y	B
    2	I	U	S	A	C
    3	D	E	F	G	H
    4	K	M	N	Q	R
    5	T	V	W	X	Y

Now manually decrypting the message we get:
```
CT:  96 57 47 66 62 38 55 67 55 35 68 44 48 95 66 65 57 65 53 75 78 77 55 36 47 55 45 66 87 34 46 48 33 77
KEY: 45 22 23 23 21 24 43 45 22 23 23 21 24 43 45 22 23 23 21 24 43 45 22 23 23 21 24 43 45 22 23 23 21 24 
PT:  51 35 24 43 41 47 14 22 33 12 45 23 24 52 21 23 34 42 32 51 35 32 33 13 24 34 21 23 42 12 23 25 12 53

```

And this plain text translates to :
```
THANK YOU FOR SAVING ME THE FLAG IS MOSCOW

```
![image](https://github.com/ahmedoshelmy/Secure-Chat/assets/36341168/f9044ce3-25a2-46f3-8d6f-3631bfbc62b7)
![WhatsApp Image 2024-05-11 at 03 00 52_7fa3e4f7](https://github.com/ahmedoshelmy/Secure-Chat/assets/36341168/49ea17ef-2223-482b-884f-93fcb833548b)
![image](https://github.com/ahmedoshelmy/Secure-Chat/assets/36341168/f9bfe1f6-04e8-4ae0-b060-f69c36a564e4)

***Tools:*** 

DataBorder Morse Code Sound & Vibration Listener (https://databorder.com/transfer/morse-sound-receiver/)

Steganographic Decoder (https://futureboy.us/stegano/decinput.html)
