from DiffieHellman import DiffieHellman
from Elgamal import Elgamal
from Hashing import Hashing
import tkinter as tk



def main():
    q_diff = 1021
    a_diff = 2

    q_gamal = 1021
    a_gamal = 2

    message = "Hello World!"
    diff_hellman = DiffieHellman(q_diff, a_diff)
    elgamal = Elgamal(q_gamal, a_gamal)
    elgamal2 = Elgamal(q_gamal, a_gamal)

    hashing = Hashing(q_gamal)

    # Proving that when a different public key is sent the signature verifying failed
    m = hashing.hash(message)
    s1, s2 = elgamal.sign_message(m)
    print(elgamal.verify_signature(m, s1, s2, elgamal.get_public_key()))

def open_second_window():
    second_window = tk.Toplevel(root)
    second_window.title("Second Window")
    label = tk.Label(second_window, text="This is the second window")
    label.pack()

root = tk.Tk()
root.title("Main Window")

label = tk.Label(root, text="This is the main window")
label.pack()

button = tk.Button(root, text="Open Second Window", command=open_second_window)
button.pack()

root.mainloop()
# If the script is executed directly (not imported as a module)
if __name__ == "__main__":
    main()
