import tkinter as tk
from tkinter import messagebox
import sqlite3

def sign():
    account = entry_username.get()
    password = entry_password.get()
    conn = sqlite3.connect("bankk.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM userr WHERE account=? AND password=?", (account, password))
    userr = cursor.fetchone()

    if userr: 
        messagebox.showinfo("Success", "Login successful")
        root.destroy()
        import user 
    else:
        messagebox.showerror("Error", "Wrong account or password")

    conn.close()

root = tk.Tk()
root.geometry("400x400")
root.title("Login")
root.configure(bg="lightblue")

frame = tk.Frame(root,bg="lightblue")

label_username = tk.Label(frame, text="Account No:", font=("Arial", 10))
label_username.grid(row=0, column=0, padx=5, pady=5)

entry_username = tk.Entry(frame, font=("Arial", 10))
entry_username.grid(row=0, column=1, padx=5, pady=5)

label_password = tk.Label(frame, text="Password:", font=("Arial", 10))
label_password.grid(row=1, column=0, padx=5, pady=5)

entry_password = tk.Entry(frame, show="*", font=("Arial", 10))
entry_password.grid(row=1, column=1, padx=5, pady=5)

button_login = tk.Button(frame, text="Login", command=sign)
button_login.grid(row=2, columnspan=2, pady=10)

frame.pack(pady=20)

root.mainloop()
