import tkinter as tk
from tkinter import messagebox
import sqlite3


def clear():
    for entry in entry_fields:
        entry.delete(0, tk.END)


def deposit():
    account = account_entry.get()
    amount = amount_entry.get()

    try:
        amount = int(amount)
    except ValueError:
        messagebox.showerror("Error", "Invalid amount type.")
        return

    conn = sqlite3.connect("bankk.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userr WHERE account=?", (account,))
    user = cursor.fetchone()

    if user:
        updated_money = user[8] + amount  # user[8] is the amount field
        cursor.execute("UPDATE userr SET amount=? WHERE account=?", (updated_money, account))
        conn.commit()
        messagebox.showinfo("Success", f"Deposit successful! New balance for account {account}: {updated_money}")
    else:
        messagebox.showerror("Error", "User not found.")
    conn.close()
    clear()
def withdraw():
    account = withdraw_account_entry.get()
    amount = withdraw_amount_entry.get()

    try:
        account = int(account)
        amount = int(amount)
    except ValueError:
        messagebox.showerror("Error", "account and amount must be a number.")
        return

    conn = sqlite3.connect("bankk.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userr WHERE account=?", (account,))
    user = cursor.fetchone()

    if user:
        if user[8]-25>= amount:
            updated_money = user[8] - amount
            cursor.execute("UPDATE userr SET amount=? WHERE account=?", (updated_money, account))
            conn.commit()
            messagebox.showinfo("Success", f"Withdrawal successful! New balance for account {account}: {updated_money}")
        else:
            messagebox.showerror("Error", "Insufficient funds.")
    else:
        messagebox.showerror("Error", "User not found.")
    conn.close()
    clear()

# Function to handle transfer operation
def transfer():
    sender_account = sender_account_entry.get()
    receiver_account = receiver_account_entry.get()
    amount = transfer_amount_entry.get()

    try:
        amount = int(amount)
    except ValueError:
        messagebox.showerror("Error", "amount must be integer.")
        return

    conn = sqlite3.connect("bankk.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userr WHERE account=?", (sender_account,))
    sender = cursor.fetchone()
    cursor.execute("SELECT * FROM userr WHERE account=?", (receiver_account,))
    receiver = cursor.fetchone()

    if sender and receiver:
        if sender[8]-25 >= amount and amount > 0:
            updated_sender_money = sender[8] - amount
            updated_receiver_money = receiver[8] + amount

            cursor.execute("UPDATE userr SET amount=? WHERE account=?", (updated_sender_money, sender_account))
            cursor.execute("UPDATE userr SET amount=? WHERE account=?", (updated_receiver_money, receiver_account))
            conn.commit()
            messagebox.showinfo("Success", f"Transfer successful!\nNew balance for sender account {sender_account}: {updated_sender_money}")
        else:
            messagebox.showerror("Error", "Insufficient funds.")
    else:
        messagebox.showerror("Error", "Sender or receiver account not found.")
    conn.close()
    clear()

# Function to search for user by password
def search():
    password = search_password_entry.get()

    conn = sqlite3.connect("bankk.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userr WHERE password=?", (password,))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("User Found", f"Name: {user[0]} {user[1]}\nAge: {user[2]}\nAddress: {user[3]}\nPhone:{user[5]}\nPassword: {user[4]}\nAccount:{user[6]}\nEmail: {user[7]}\nAmount:{user[8]}")
    else:
        messagebox.showerror("Error", "User not found.")
    conn.close()
    clear()

def update_password():
    password = old_password_entry.get()
    new_password = new_password_entry.get()
    if not password or not new_password:
        messagebox.showerror("Error", "Please fill in the fields to change the password .")
        return

    conn = sqlite3.connect("bankk.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userr WHERE password=?", (password,))
    user = cursor.fetchone()

    if user:
        cursor.execute("UPDATE userr SET password=? WHERE password=?", (new_password, password))
        conn.commit()
        messagebox.showinfo("Success", f"Password updated successfully.{password} change to {new_password}")
    else:
        messagebox.showerror("Error", "Incorrect old password.")
    conn.close()
    clear()
root = tk.Tk()
root.geometry("800x600")
root.title("Banking System")

root.configure(bg="gray")
conn = sqlite3.connect("bankk.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS userr (
                name TEXT,
                lastname TEXT,
                age INTEGER,
                address TEXT,
                phone TEXT,
                account TEXT,
                password TEXT,
                amount INTEGER
                )''')
conn.commit()

frame = tk.Frame(root, bg="gray")
frame.pack(pady=20)

entry_fields = []

# Deposit Widgets
deposit_frame = tk.LabelFrame(frame, text="Deposit", bg="lightblue", fg="black", padx=10, pady=10)
deposit_frame.grid(row=0, column=0, padx=10, pady=10)

account_label = tk.Label(deposit_frame, text="Account:", bg="lightblue", fg="black")
account_label.grid(row=0, column=0)
account_entry = tk.Entry(deposit_frame)
account_entry.grid(row=0, column=1)
entry_fields.append(account_entry)

amount_label = tk.Label(deposit_frame, text="Amount:", bg="lightblue", fg="black")
amount_label.grid(row=1, column=0)
amount_entry = tk.Entry(deposit_frame)
amount_entry.grid(row=1, column=1)
entry_fields.append(amount_entry)

deposit_button = tk.Button(deposit_frame, text="Deposit", bg="black", fg="white", command=deposit)
deposit_button.grid(row=2, columnspan=2, pady=5)

# Withdrawal Widgets
withdraw_frame = tk.LabelFrame(frame, text="Withdrawal", bg="lightblue", fg="black", padx=10, pady=10)
withdraw_frame.grid(row=0, column=1, padx=10, pady=10)

withdraw_account_label = tk.Label(withdraw_frame, text="Account:", bg="lightblue", fg="black")
withdraw_account_label.grid(row=0, column=0, padx=5, pady=5)
withdraw_account_entry = tk.Entry(withdraw_frame)
withdraw_account_entry.grid(row=0, column=1, padx=5, pady=5)
entry_fields.append(withdraw_account_entry)

withdraw_amount_label = tk.Label(withdraw_frame, text="Amount:", bg="lightblue", fg="black")
withdraw_amount_label.grid(row=1, column=0, padx=5, pady=5)
withdraw_amount_entry = tk.Entry(withdraw_frame)
withdraw_amount_entry.grid(row=1, column=1, padx=5, pady=5)
entry_fields.append(withdraw_amount_entry)

withdraw_button = tk.Button(withdraw_frame, text="Withdraw", bg="black", fg="white", command=withdraw)
withdraw_button.grid(row=2, columnspan=2, pady=5)

# Transfer Widgets
transfer_frame = tk.LabelFrame(frame, text="Transfer", bg="lightblue", fg="black", padx=10, pady=10)
transfer_frame.grid(row=1, column=0, padx=10, pady=10)

sender_account_label = tk.Label(transfer_frame, text="Sender Account:", bg="lightblue", fg="black")
sender_account_label.grid(row=0, column=0, padx=5, pady=5)
sender_account_entry = tk.Entry(transfer_frame)
sender_account_entry.grid(row=0, column=1, padx=5, pady=5)
entry_fields.append(sender_account_entry)

receiver_account_label = tk.Label(transfer_frame, text="Receiver Account:", bg="lightblue", fg="black")
receiver_account_label.grid(row=1, column=0, padx=5, pady=5)
receiver_account_entry = tk.Entry(transfer_frame)
receiver_account_entry.grid(row=1, column=1, padx=5, pady=5)
entry_fields.append(receiver_account_entry)

transfer_amount_label = tk.Label(transfer_frame, text="Amount:", bg="lightblue", fg="black")
transfer_amount_label.grid(row=2, column=0, padx=5, pady=5)
transfer_amount_entry = tk.Entry(transfer_frame)
transfer_amount_entry.grid(row=2, column=1, padx=5, pady=5)
entry_fields.append(transfer_amount_entry)

transfer_button = tk.Button(transfer_frame, text="Transfer", bg="black", fg="white", command=transfer)
transfer_button.grid(row=3, columnspan=2, pady=5)

# Search Widgets
search_frame = tk.LabelFrame(frame, text="Search User", bg="lightblue", fg="black", padx=10, pady=10)
search_frame.grid(row=1, column=1, padx=10, pady=10)

search_password_label = tk.Label(search_frame, text="Password:", bg="lightblue", fg="black")
search_password_label.grid(row=0, column=0, padx=5, pady=5)
search_password_entry = tk.Entry(search_frame, show="*")
search_password_entry.grid(row=0, column=1, padx=5, pady=5)
entry_fields.append(search_password_entry)

search_button = tk.Button(search_frame, text="Search", bg="black", fg="white", command=search)
search_button.grid(row=1, columnspan=2, pady=5)

# Update Password Widgets
update_password_frame = tk.LabelFrame(frame, text="Update Password", bg="lightblue", fg="black", padx=10, pady=10)
update_password_frame.grid(row=1, column=2, padx=10, pady=10)

old_password_label = tk.Label(update_password_frame, text="Old Password:", bg="lightblue", fg="black")
old_password_label.grid(row=0, column=0, padx=5, pady=5)
old_password_entry = tk.Entry(update_password_frame, show="*")
old_password_entry.grid(row=0, column=1, padx=5, pady=5)
entry_fields.append(old_password_entry)

new_password_label = tk.Label(update_password_frame, text="New Password:", bg="lightblue", fg="black")
new_password_label.grid(row=1, column=0, padx=5, pady=5)
new_password_entry = tk.Entry(update_password_frame, show="*")
new_password_entry.grid(row=1, column=1, padx=5, pady=5)
entry_fields.append(new_password_entry)

update_password_button = tk.Button(update_password_frame, text="Update Password", bg="black", fg="white", command=update_password)
update_password_button.grid(row=2, columnspan=2, pady=5)

root.mainloop()
