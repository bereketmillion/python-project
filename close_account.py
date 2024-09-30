import tkinter as tk
import sqlite3
from tkinter import messagebox

def delete():
    account = entry_account.get()
    name = entry_name.get()
    if not account or not name:
        messagebox.showerror("Error", "Please enter both account number and name")
        return
    
    try:
        account = int(account)
    except ValueError:
        messagebox.showerror("Error", "Account number must be a number")
        return
    
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this user?"):
        conn = sqlite3.connect("bankk.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM userr WHERE account=? AND name=?", (account, name))
        if cursor.rowcount == 0:
            messagebox.showerror("Error", "No matching user found")
        else:
            conn.commit()
            messagebox.showinfo("Success", "User deleted successfully")
        conn.close()

root = tk.Tk()
root.geometry("400x400")
root.title("Delete User Account")
root.configure(bg="lightblue")


frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=20)

account_label = tk.Label(frame, text="Account:", font=('Arial', 14), bg="lightblue")
account_label.grid(row=1, column=0, padx=10, pady=10)
entry_account = tk.Entry(frame, font=('Arial', 14))
entry_account.grid(row=1, column=1, padx=10, pady=10)

name_label = tk.Label(frame, text="Name:", font=('Arial', 14), bg="lightblue")
name_label.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(frame, font=('Arial', 14))
entry_name.grid(row=0, column=1, padx=10, pady=10)


delete_button = tk.Button(frame, text="Delete user ", bg="lightgray", fg="black", font=('Arial', 14), command=delete)
delete_button.grid(row=2, columnspan=2, pady=20)

root.mainloop()

