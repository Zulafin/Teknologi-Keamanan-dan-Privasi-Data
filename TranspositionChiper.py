import tkinter as tk

class TranspositionCipherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Transposition Cipher")

        # Create input and output text boxes
        self.input_label = tk.Label(master, text="Input:")
        self.input_label.pack()
        self.input_textbox = tk.Text(master, height=5, width=50)
        self.input_textbox.pack()

        self.output_label = tk.Label(master, text="Output:")
        self.output_label.pack()
        self.output_textbox = tk.Text(master, height=5, width=50, state="disabled")
        self.output_textbox.pack()

        # Create encrypt and decrypt buttons
        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack()

    def encrypt(self):
        input_text = self.input_textbox.get("1.0", tk.END).strip()
        key = len(input_text) // 2
        output_text = self.transpose(input_text, key)
        self.output_textbox.configure(state="normal")
        self.output_textbox.delete("1.0", tk.END)
        self.output_textbox.insert(tk.END, output_text)
        self.output_textbox.configure(state="disabled")

    def decrypt(self):
        input_text = self.input_textbox.get("1.0", tk.END).strip()
        key = len(input_text) // 2
        output_text = self.transpose(input_text, key)
        self.output_textbox.configure(state="normal")
        self.output_textbox.delete("1.0", tk.END)
        self.output_textbox.insert(tk.END, output_text)
        self.output_textbox.configure(state="disabled")

    def transpose(self, text, key):
        transposed_text = [""] * key
        for i in range(key):
            j = i
            while j < len(text):
                transposed_text[i] += text[j]
                j += key
        return "".join(transposed_text)

root = tk.Tk()
my_gui = TranspositionCipherGUI(root)
root.mainloop()
