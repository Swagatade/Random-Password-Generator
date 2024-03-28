import tkinter as tk
import random
import string
import pyperclip
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.complexity_label = tk.Label(root, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=10)

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")

        self.complexity_menu = tk.OptionMenu(root, self.complexity_var, "Low", "Medium", "High")
        self.complexity_menu.grid(row=1, column=1, padx=10, pady=10)

        self.rules_label = tk.Label(root, text="Rules:")
        self.rules_label.grid(row=2, column=0, padx=10, pady=10)

        self.rules_text = tk.Text(root, height=4, width=50)
        self.rules_text.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.password_label = tk.Label(root, text="")
        self.password_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.set_default_rules()

    def set_default_rules(self):
        rules_low = "- Only alphanumeric characters"
        rules_medium = "- Alphanumeric characters\n- Special characters"
        rules_high = "- Alphanumeric characters\n- Special characters\n- Upper and lower case letters"
        self.rules_text.insert(tk.END, f"Low Complexity:\n{rules_low}\n\nMedium Complexity:\n{rules_medium}\n\nHigh Complexity:\n{rules_high}")

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")

            complexity = self.complexity_var.get()

            if complexity == "Low":
                charset = string.ascii_letters + string.digits
            elif complexity == "Medium":
                charset = string.ascii_letters + string.digits + string.punctuation
            else:
                charset = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase

            password = ''.join(random.choice(charset) for _ in range(length))
            self.password_label.config(text=f"Generated Password: {password}")

        except ValueError as e:
            self.password_label.config(text=str(e))

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        if password.startswith("Generated Password: "):
            password = password[len("Generated Password: "):]
            pyperclip.copy(password)
            messagebox.showinfo("Info", "Password copied to clipboard.")
        else:
            messagebox.showerror("Error", "No password generated yet.")

root = tk.Tk()
app = PasswordGenerator(root)
root.mainloop()
