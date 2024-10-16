import tkinter as tk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Secure Password Generator")

        self.length_var = tk.IntVar(value=12)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        # Length input
        tk.Label(master, text="Password Length:").pack(pady=5)
        tk.Entry(master, textvariable=self.length_var).pack(pady=5)

        # Character type checkboxes
        tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.uppercase_var).pack(pady=5)
        tk.Checkbutton(master, text="Include Numbers", variable=self.numbers_var).pack(pady=5)
        tk.Checkbutton(master, text="Include Symbols", variable=self.symbols_var).pack(pady=5)

        # Generate button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Generated password display
        self.password_label = tk.Label(master, text="", font=('Helvetica', 14))
        self.password_label.pack(pady=10)

        # Copy button
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()
        use_uppercase = self.uppercase_var.get()
        use_numbers = self.numbers_var.get()
        use_symbols = self.symbols_var.get()

        characters = string.ascii_lowercase  # Always include lowercase letters
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if len(characters) == 0:
            self.password_label.config(text="Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=f"Generated Password: {password}")

    def copy_to_clipboard(self):
        password = self.password_label.cget("text").replace("Generated Password: ", "")
        if password:
            pyperclip.copy(password)
            self.password_label.config(text="Password copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
