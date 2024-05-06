
# CTF-7: Steganograogy
### ***Problem Statement:***

Steganography is to hide some file or data inside another file or data. In the given image
something is HIDING.

### ***Flag:***

CMPN{Spring2024}.


### ***Solution Walkthrough:***

I first tried to solve the problem with the traditional approach of LSB steganography trying to decode the message by concatenating the LSB of each pixel in the RGB channels, I tried to decode all the channels together and tried to decode each channel individually , the code for one of the trials can be found in `stegano.ipynb`.

After multiple trials and workarounds, the result never made sense and it didn’t seem to have any meaning.

I thought that maybe the message was encrypted as the output text from decoding seemed to be encrypted.

Also, throughout the whole process I was thinking of the “HIDING” key written in caps so I tried an online tool for decrypting steganographic images it asked for a password, this was the only word I had in mind so I tried it and VOILA it worked.

### ***Tools:***

These online tools were used to decrypt the steganographic image 
1. Aperi'Solve (aperisolve.com)
2. Steganographic Decoder (futureboy.us)
