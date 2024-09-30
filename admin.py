import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.geometry("600x600")
root.title("Banking System")
root.configure(bg="lightblue")

# Create SQLite3 Database
conn = sqlite3.connect("bankk.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS userr (
    name TEXT NOT NULL,
    lastname TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL,
    password TEXT NOT NULL PRIMARY KEY,
    phone TEXT NOT NULL,
    account INT NOT NULL ,
    email TEXT NOT NULL,
    amount INT NOT NULL
)
""")
conn.commit()

cursor.execute("SELECT MAX(account) FROM userr")
max_account = cursor.fetchone()[0]
if max_account is None:
    max_account = 1000  # Starting point if no accounts exist
account = max_account + 10
conn.close()

def create():
    global account
    name = entry_name.get()
    lastname = entry_lastname.get()
    age = entry_age.get()
    address = entry_address.get()
    password = entry_password.get()
    phone = entry_phone.get()
    email = entry_email.get()
    amount = entry_amount.get()
    
    if not name or not lastname or not age or not address or not password or not phone or not email or not amount:
        messagebox.showerror("Error", "Please fill out all fields")
        return

    try:
        age = int(age)
        amount = int(amount)
        phone=int(phone)
    except ValueError:
        messagebox.showerror("Error", "Age,phone and amount must be numbers")
        return

    try:
        conn = sqlite3.connect("bankk.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO userr (name, lastname, age, address, password, phone, account, email, amount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (name, lastname, age, address, password, phone, account, email, amount))
       
        conn.commit()
        user=cursor.fetchone()
        messagebox.showinfo("Success", "User registered successfully!")
        
        clear()
        update_account_label()
        
    
       
        cursor.execute("SELECT * FROM userr WHERE account=?", (account,))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("User info", f"Name: {user[0]} {user[1]}\nAge: {user[2]}\nAddress: {user[3]}\npassword: {user[4]}\nphone:{user[5]}\nAccount: {user[6]}\nEmail:{user[7]}\nAmount:{user[8]}\n")
            return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "User with this account number already exists")
    conn.close()
def display():
    display_window = tk.Toplevel(root)
    display_window.title("Display Users")
    display_window.geometry("800x800")
    display_window.configure(background="lightblue")

    conn = sqlite3.connect("bankk.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userr")
    users= cursor.fetchall()
    conn.close()

    if users:
        columns = ["Name", "Lastname", "Age", "Address", "Password", "Phone", "Account", "Email", "Amount"]
        tree = ttk.Treeview(display_window, columns=columns, show='headings')
        for x in columns:
            tree.heading(x, text=x)
            tree.column(x, width=100)

        for user in users:
            tree.insert("", "end", values=user)

        tree.pack()
    else:
        ttk.Label(display_window, text="No users found.", background="white", font=("Arial", 10)).pack(pady=20)

def search():
    root.destroy()
    import search_user

def delete():
    root.destroy()
    import close_account

def clear():
    for entry in entry_fields:
        entry.delete(0, tk.END)

def update_account_label():
    account_label_var.set("Account No: ................")
# Create frame and input fields
frame = tk.Frame(root, bg="lightblue")
frame.pack(padx=20,pady=20)

entry_fields = []

name=ttk.Label(frame, text="Name:", background="lightblue", foreground="black", font=("Arial", 10))
name.grid(row=0, column=0, pady=5, padx=10)
entry_name = ttk.Entry(frame)
entry_name.grid(row=0, column=1, pady=5, padx=10)
entry_fields.append(entry_name)

lastname=ttk.Label(frame, text="Lastname:", background="lightblue", foreground="black", font=("Arial", 10))
lastname.grid(row=1, column=0, pady=5, padx=10)
entry_lastname = ttk.Entry(frame)
entry_lastname.grid(row=1, column=1, pady=5, padx=10)
entry_fields.append(entry_lastname)

age=ttk.Label(frame, text="Age:", background="lightblue", foreground="black", font=("Arial", 10))
age.grid(row=2, column=0, pady=5, padx=10)
entry_age = ttk.Spinbox(frame, from_=18, to=100)
entry_age.grid(row=2, column=1, pady=5, padx=10)
entry_fields.append(entry_age)

address=ttk.Label(frame, text="Address:", background="lightblue", foreground="black", font=("Arial", 10))
address.grid(row=3, column=0, pady=5, padx=10)
entry_address = ttk.Entry(frame)
entry_address.grid(row=3, column=1, pady=5, padx=10)
entry_fields.append(entry_address)

password=ttk.Label(frame, text="Password:", background="lightblue", foreground="black", font=("Arial", 10))
password.grid(row=4, column=0, pady=5, padx=10)
entry_password = ttk.Entry(frame, show="*")
entry_password.grid(row=4, column=1, pady=5, padx=10)
entry_fields.append(entry_password)

phone=ttk.Label(frame, text="Phone:", background="lightblue", foreground="black", font=("Arial", 10))
phone.grid(row=5, column=0, pady=5, padx=10)
entry_phone = ttk.Entry(frame)
entry_phone.grid(row=5, column=1, pady=5, padx=10)
entry_fields.append(entry_phone)

email=ttk.Label(frame, text="Email:", background="lightblue", foreground="black", font=("Arial", 10))
email.grid(row=6, column=0, pady=5, padx=10)
entry_email = ttk.Entry(frame)
entry_email.grid(row=6, column=1, pady=5, padx=10)
entry_fields.append(entry_email)

amount=ttk.Label(frame, text="Amount:", background="lightblue", foreground="black", font=("Arial", 10))
amount.grid(row=7, column=0, pady=5, padx=10)
entry_amount = ttk.Entry(frame)
entry_amount.grid(row=7, column=1, pady=5, padx=10)
entry_fields.append(entry_amount)

account_label_var = tk.StringVar()
account_label = ttk.Label(frame, textvariable=account_label_var, background="lightblue", foreground="black", font=("Arial", 10))
account_label.grid(row=8, column=0, pady=5, padx=10)
update_account_label()

registor_button=ttk.Button(frame, text="Register", command=create)
registor_button.grid(row=9, column=0, pady=10)
display_button=ttk.Button(frame, text="Display Users", command=display)
display_button.grid(row=9, column=1, pady=10)
search_button=ttk.Button(frame, text="Search User", command=search)
search_button.grid(row=10, column=0, pady=15)
close_button=ttk.Button(frame, text="Delete user", command=delete)
close_button.grid(row=10, column=1, pady=15)

root.mainloop()
