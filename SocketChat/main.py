from DiffieHellman import DiffieHellman


def main():
    q = 1021
    a = 2
    alice = DiffieHellman(q, a)
    bob = DiffieHellman(q, a)

    # Exchange public keys
    alice_public_key = alice.get_public_key()
    bob_public_key = bob.get_public_key()

    print(f"Alice's public key: {alice_public_key}")
    print(f"Bob's public key: {bob_public_key}")

    # Calculate shared secret keys
    alice_shared_key = alice.calculate_shared_secret_key(bob_public_key)
    bob_shared_key = bob.calculate_shared_secret_key(alice_public_key)

    print(f"Alice's shared secret key: {alice_shared_key}")
    print(f"Bob's shared secret key: {bob_shared_key}")


# If the script is executed directly (not imported as a module)
if __name__ == "__main__":
    main()
