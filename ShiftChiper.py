from tkinter import *

# Function to encrypt plaintext using shift cipher
def encrypt():
    plaintext = entry1.get().upper()
    key = int(entry2.get())
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            ciphertext += char
    entry3.delete(0, END)
    entry3.insert(0, ciphertext)

# Function to decrypt ciphertext using shift cipher
def decrypt():
    ciphertext = entry1.get().upper()
    key = int(entry2.get())
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += chr((ord(char) - 65 - key) % 26 + 65)
        else:
            plaintext += char
    entry3.delete(0, END)
    entry3.insert(0, plaintext)

# Create GUI window
root = Tk()
root.title("Shift Cipher")

# Create labels
label1 = Label(root, text="Plaintext/Ciphertext:")
label1.grid(row=0, column=0, padx=5, pady=5)
label2 = Label(root, text="Key:")
label2.grid(row=1, column=0, padx=5, pady=5)
label3 = Label(root, text="Result:")
label3.grid(row=2, column=0, padx=5, pady=5)

# Create text entry boxes
entry1 = Entry(root, width=30)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2 = Entry(root, width=30)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry3 = Entry(root, width=30)
entry3.grid(row=2, column=1, padx=5, pady=5)

# Create encrypt and decrypt buttons
encrypt_button = Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=3, column=0, padx=5, pady=5)
decrypt_button = Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=3, column=1, padx=5, pady=5)

# Run the GUI window
root.mainloop()
