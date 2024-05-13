# End-To-End Encrypted Secure Messaging

## Client Implementation

This Python script implements a secure messaging client using custom functions for El-Gamal and Diffie-Hellman
cryptography.

## Steps to send End-To-End Encrypted Data


### 1. Key Generation

-   **Client-Side:**
    
    -   Each client generates a unique pair of cryptographic keys for two algorithms:
        
        -   **Elgamal:** This algorithm is used for digital signatures, ensuring message authenticity. It generates a public key (used for verification) and a private key (kept secret for signing).
        -   **Diffie-Hellman:** This algorithm establishes a shared secret key for secure communication. It also generates a public-private key pair.
        
    

### 2. Key Exchange Initiated by Server

-   **Server-Side:**
    
    -   Once two clients connect to the server, the server initiates a secure communication handshake by sending a `KEY EXCHANGE` event to both clients.
    

### 3. Sending Elgamal Public Key

-   **Client-Side:**
    
    -   Upon receiving the `KEY EXCHANGE` event, each client sends its Elgamal public key to the server. This public key will be used by the recipient to verify the authenticity of future messages.
    

### 4. Diffie-Hellman Key Exchange with Signature

-   **Client-Side:**
    
    -   After sending the Elgamal public key, each client performs the following:
        
        1.  It uses the generated Diffie-Hellman public key.
        2.  Hashes the Diffie-Hellman public key using a secure hashing algorithm like SHA-1.
        3.  Signs the hashed value using its Elgamal private key.
        4.  Sends both the Diffie-Hellman public key and the Elgamal signature to the server.
        
    

### 5. Signature Verification

-   **Client-Side:**
    
    -   Upon receiving the message from the server containing the other client's Diffie-Hellman public key and Elgamal signature, each client performs the following:
        
        1.  Uses the previously received Elgamal public key of the sender to verify the signature.
        2.  If the signature verification fails, the message is rejected as it might be tampered with.
        
    

### 6. Shared Secret Key Generation

-   **Client-Side:**
    
    -   If the signature verification is successful, the client can proceed with generating the shared secret key for secure communication.
    -   This shared secret key is derived using the Diffie-Hellman algorithm, combining its private key with the received Diffie-Hellman public key from the other client.
    

**Important Note:** Due to the mathematical properties of Diffie-Hellman, both clients will end up with the same shared secret key, allowing them to encrypt and decrypt messages securely.

### 7. Secure Communication with AES

-   **Client-Side:**
    -   The established shared secret key is used to encrypt messages using the Advanced Encryption Standard (AES) algorithm.
    -   Before encryption, the message is hashed using a secure hashing algorithm like SHA-256 to ensure data integrity and that the key length is always 256 since we use in AES 256-bit long key. 
**Features:**

- **Key Exchange:**

    - Diffie-Hellman key exchange (implemented in `DiffieHellman.DiffieHellman`) for establishing a shared secret key
      between client and server.

- **Digital Signatures:**

    - ElGamal digital signatures (implemented in `Elgamal.Elgamal`) to ensure message authenticity and non-repudiation.

- **Hashing:**

    - Hashing messages for signing with ElGamal (potentially implemented in a separate function) using SHA1 and SHA256.

- **Symmetric Encryption:**

    - Advanced Encryption Standard (AES) in Cipher Feedback Mode (CFB) for message confidentiality (likely using an
      external library like `pycryptodome`).

- **WebSockets:**

    - Socket.IO for real-time communication with the server.

## Server Implementation

This server script utilizes Socket.IO to facilitate communication between clients in a secure messaging application. It
complements the client-side script implementing ElGamal and Diffie-Hellman cryptography for end-to-end encryption.

**Functionality:**

- Manages connections and disconnections of clients.
- Broadcasts key exchange initiation (`KEY_EXCHANGE`) when two clients connect.
- Facilitates relaying messages between connected clients while maintaining confidentiality through end-to-end
  encryption (implemented on the client-side).
- Handles receiving and broadcasting ElGamal public keys (`ELGAMAL_PK`) and Diffie-Hellman public
  keys (`DEFF_HELLMAN_PK`) used for encryption on the client-side.

**End-to-End Encryption:**

The server itself doesn't perform any encryption or decryption. The actual encryption and decryption of messages happen
on the client-side using the established keys from the Diffie-Hellman key exchange and ElGamal digital signatures. This
ensures only the sender and receiver can access the message content.

## Instructions:

1. **Prerequisites:**

    - Install required libraries:  `socket.io-client`,  `json` , `Cryptodome` ,`base64`, `hashlib`

2. **Running the Server:**
    - Open a terminal and navigate to the directory containing this script.
    - Run the script using `python server.py`.
    - The server will listen for connections on port 5000.

3. **Key Setup:**

    - Ensure the server has corresponding Diffie-Hellman and ElGamal key pairs generated beforehand.
    - Replace the file paths (`./Encryptions/diff_hellman_keys.txt` and `./Encryptions/elgamal_keys.txt`) with comments
      indicating they are no longer used (or remove them if applicable).

4. **Running the Script:**
    - Open a terminal and navigate to the directory containing this script.
    - Run the script using `python client.py`.
    - To test the messaging run only 2 instances of the client and one server instance at the same time.
    - Run the server using  `python server.py`.

5. **Sending Messages:**
    - The script connects to the server at `http://localhost:5000`.
    - Enter messages to send.
    - Type "exit" to terminate the connection.
