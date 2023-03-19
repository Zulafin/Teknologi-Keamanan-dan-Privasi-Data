import tkinter as tk
from tkinter import messagebox

def vigenere_cipher(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_as_int = [ord(i) for i in plaintext]
    ciphertext = ""
    for i in range(len(plaintext_as_int)):
        value = (plaintext_as_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def encrypt():
    plaintext = entry_plaintext.get()
    key = entry_key.get()
    if len(key) < 1:
        messagebox.showwarning("Warning", "Please enter a key!")
        return
    ciphertext = vigenere_cipher(plaintext, key)
    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, ciphertext)

def decrypt():
    ciphertext = entry_ciphertext.get()
    key = entry_key.get()
    if len(key) < 1:
        messagebox.showwarning("Warning", "Please enter a key!")
        return
    plaintext = ""
    for i in range(len(ciphertext)):
        value = (ord(ciphertext[i]) - ord(key[i % len(key)]) + 26) % 26
        plaintext += chr(value + 65)
    entry_plaintext.delete(0, tk.END)
    entry_plaintext.insert(0, plaintext)

# Create GUI
root = tk.Tk()
root.title("Vigenere Cipher")

# Create widgets
label_plaintext = tk.Label(root, text="Plaintext:")
label_key = tk.Label(root, text="Key (use 1, 4, and 0 only):")
label_ciphertext = tk.Label(root, text="Ciphertext:")
entry_plaintext = tk.Entry(root)
entry_key = tk.Entry(root)
entry_ciphertext = tk.Entry(root)
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt)
button_decrypt = tk.Button(root, text="Decrypt", command=decrypt)

# Add widgets to GUI
label_plaintext.grid(row=0, column=0, padx=10, pady=10, sticky="w")
label_key.grid(row=1, column=0, padx=10, pady=10, sticky="w")
label_ciphertext.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_plaintext.grid(row=0, column=1, padx=10, pady=10)
entry_key.grid(row=1, column=1, padx=10, pady=10)
entry_ciphertext.grid(row=2, column=1, padx=10, pady=10)
button_encrypt.grid(row=3, column=0, padx=10, pady=10)
button_decrypt.grid(row=3, column=1, padx=10, pady=10)

# Start GUI
root.mainloop()
