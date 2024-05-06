# End-To-End Encrypted Secure Messaging 

## Client Implementation

This Python script implements a secure messaging client using custom functions for El-Gamal and Diffie-Hellman cryptography.

**Features:**

-   **Key Exchange:**
    
    -   Diffie-Hellman key exchange (implemented in `DiffieHellman.DiffieHellman`) for establishing a shared secret key between client and server.
    
-   **Digital Signatures:**
    
    -   ElGamal digital signatures (implemented in `Elgamal.Elgamal`) to ensure message authenticity and non-repudiation.
    
-   **Hashing:**
    
    -   Hashing messages for signing with ElGamal (potentially implemented in a separate function) using SHA1 and SHA256. 
    
-   **Symmetric Encryption:**
    
    -   Advanced Encryption Standard (AES) in Cipher Feedback Mode (CFB) for message confidentiality (likely using an external library like `pycryptodome`).
    
-   **WebSockets:**
    
    -   Socket.IO for real-time communication with the server.
    




## Server Implementation 

This server script utilizes Socket.IO to facilitate communication between clients in a secure messaging application. It complements the client-side script implementing ElGamal and Diffie-Hellman cryptography for end-to-end encryption.

**Functionality:**

-   Manages connections and disconnections of clients.
-   Broadcasts key exchange initiation (`KEY_EXCHANGE`) when two clients connect.
-   Facilitates relaying messages between connected clients while maintaining confidentiality through end-to-end encryption (implemented on the client-side).
-   Handles receiving and broadcasting ElGamal public keys (`ELGAMAL_PK`) and Diffie-Hellman public keys (`DEFF_HELLMAN_PK`) used for encryption on the client-side.

**End-to-End Encryption:**

The server itself doesn't perform any encryption or decryption. The actual encryption and decryption of messages happen on the client-side using the established keys from the Diffie-Hellman key exchange and ElGamal digital signatures. This ensures only the sender and receiver can access the message content.

## Instructions:

1.  **Prerequisites:**

    -   Install required libraries:  `socket.io-client`,  `json` , `Cryptodome` ,`base64`, `hashlib`
    
2.  **Running the Server:**
    -   Open a terminal and navigate to the directory containing this script.
    -   Run the script using `python server.py`.
    -   The server will listen for connections on port 5000.
    
3.  **Key Setup:**
    
    -   Ensure the server has corresponding Diffie-Hellman and ElGamal key pairs generated beforehand.
    -   Replace the file paths (`./Encryptions/diff_hellman_keys.txt` and `./Encryptions/elgamal_keys.txt`) with comments indicating they are no longer used (or remove them if applicable).
    
4.  **Running the Script:**
    -   Open a terminal and navigate to the directory containing this script.
    -   Run the script using `python client.py`.
    - To test the messaging run only 2 instances of the client and one server instance at the same time.
    - Run the server using  `python server.py`.
    
5.  **Sending Messages:**
    -   The script connects to the server at `http://localhost:5000`.
    -   Enter messages to send.
    -   Type "exit" to terminate the connection.
