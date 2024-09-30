import tkinter as tk
import sqlite3

def connect():
    root.destroy()#out connect function
    import to_admin#go to admin interface/next page

def users():
    root.destroy()#out users function
    import to_user#go to user interface/netpage interface

root = tk.Tk()
root.geometry("500x600")
root.configure(bg="lightblue")
root.title("login page")

frame = tk.Frame(root, bg="lightblue")
ad = tk.Label(frame, bg="lightblue", text="Welcome to our bank, please select your role", fg="black", font=("arial", 15))
ad.grid(row=0, column=0, columnspan=2, pady=10)

admin = tk.Button(frame, bg="black", text="Admin", command=connect, fg="white", font=("arial", 9), pady=15, padx=15)
admin.grid(row=1, column=0, pady=5)

user = tk.Button(frame, bg="black", fg="white", command=users, text="User", font=("arial", 9), pady=15, padx=15)
user.grid(row=1, column=1, pady=5)
 
frame.place(relx=0.5, rely=0.5, anchor='center') 

root.mainloop()
