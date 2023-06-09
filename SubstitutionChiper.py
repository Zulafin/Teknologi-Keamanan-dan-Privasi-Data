import tkinter as tk
from tkinter import ttk
import string

# Membuat dictionary huruf yang diganti
substitution_dict = {
    'a': 'q',
    'b': 'w',
    'c': 'e',
    'd': 'r',
    'e': 't',
    'f': 'y',
    'g': 'u',
    'h': 'i',
    'i': 'o',
    'j': 'p',
    'k': 'a',
    'l': 's',
    'm': 'd',
    'n': 'f',
    'o': 'g',
    'p': 'h',
    'q': 'j',
    'r': 'k',
    's': 'l',
    't': 'z',
    'u': 'x',
    'v': 'c',
    'w': 'v',
    'x': 'b',
    'y': 'n',
    'z': 'm'
}

# Membuat fungsi untuk melakukan penggantian huruf
def substitution_cipher(text):
    result = ""
    for char in text.lower():
        if char in string.ascii_lowercase:
            result += substitution_dict[char]
        else:
            result += char
    return result

# Membuat fungsi untuk menangani tombol "Encrypt"
def encrypt():
    plaintext = plaintext_entry.get()
    ciphertext = substitution_cipher(plaintext)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

# Membuat fungsi untuk menangani tombol "Decrypt"
def decrypt():
    ciphertext = ciphertext_entry.get()
    plaintext = substitution_cipher(ciphertext)
    plaintext_entry.delete(0, tk.END)
    plaintext_entry.insert(0, plaintext)

# Membuat window
root = tk.Tk()
root.title("Substitution Cipher")

# Membuat label "Plaintext"
plaintext_label = ttk.Label(root, text="Plaintext:")
plaintext_label.grid(column=0, row=0, padx=5, pady=5)

# Membuat entry untuk plaintext
plaintext_entry = ttk.Entry(root, width=30)
plaintext_entry.grid(column=1, row=0, padx=5, pady=5)

# Membuat label "Ciphertext"
ciphertext_label = ttk.Label(root, text="Ciphertext:")
ciphertext_label.grid(column=0, row=1, padx=5, pady=5)

# Membuat entry untuk ciphertext
ciphertext_entry = ttk.Entry(root, width=30)
ciphertext_entry.grid(column=1, row=1, padx=5, pady=5)

# Membuat tombol "Encrypt"
encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(column=0, row=2, padx=5, pady=5)

# Membuat tombol "Decrypt"
decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(column=1, row=2, padx=5, pady=5)

# Menjalankan window
root.mainloop()
