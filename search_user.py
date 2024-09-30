import tkinter as tk
import sqlite3
from tkinter import messagebox

def search():
    account = search_account_entry.get()

    conn = sqlite3.connect("bankk.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userr WHERE account=?", (account,))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("User Found", f"Name: {user[0]} {user[1]}\nAge: {user[2]}\nAddress: {user[3]}\npassword: {user[4]}\nphone:{user[5]}\nAccount: {user[6]}\nEmail:{user[7]}\nAmount:{user[8]}\n")
    else:
        messagebox.showerror("Error", "User not found.")
    
    conn.close()
    clear()  # Clear the search entry field after displaying the messagebox

def clear():
    search_account_entry.delete(0, tk.END)

root = tk.Tk()
root.geometry("400x400")
root.configure(bg="lightblue")
root.title("Search User")

entry_fields = []

frame = tk.Frame(root, bg="lightblue")
frame.pack_propagate(False)

welcome = tk.Label(frame, text="SEARCH ACCOUNT INFO", font=("arial", 18), bg="lightblue", fg="black")
welcome.grid(row=0, column=0, columnspan=10, pady=20)

searchaccount = tk.Label(frame, text="Account No:", fg="black", bg="lightblue", font=("arial", 13), pady=5)
searchaccount.grid(row=1, column=0, pady=5, padx=5)

search_account_entry = tk.Entry(frame, font=("arial", 10))
search_account_entry.grid(row=1, column=1, pady=5, padx=5)
entry_fields.append(search_account_entry)

search_button = tk.Button(frame, text="Search", font=("arial", 16), command=search)
search_button.grid(row=2, columnspan=2, pady=10)

frame.pack()
root.mainloop()
