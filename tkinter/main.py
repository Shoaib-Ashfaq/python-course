import tkinter as tk
from tkinter import messagebox
import requests

# API endpoints
register_url = "http://127.0.0.1:8000/users/"
login_url = "http://127.0.0.1:8000/login"

def register_user():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    password = password_entry.get()

    if not name or not email or not age or not password:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        response = requests.post(register_url, json={
            "name": name,
            "email": email,
            "age": age,
            "hashed_password": password
        })
        if response.status_code == 200:
            messagebox.showinfo("Success", "Registered successfully!")
            clear_form()
        else:
            messagebox.showerror("Error", f"Registration failed: {response.text}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", str(e))

def login_user():
    email = login_email_entry.get()
    password = login_password_entry.get()

    if not email or not password:
        messagebox.showwarning("Login Error", "Please enter both email and password")
        return

    try:
        response = requests.post(login_url, json={
            "email": email,
            "password": password
        })
        if response.status_code == 200:
            messagebox.showinfo("Login Successful", "You are now logged in!")
            root.destroy()
            open_success_window()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", str(e))

def open_success_window():
    win = tk.Tk()
    win.title("Welcome")
    win.geometry("300x150")
    tk.Label(win, text="Login Successful!", font=("Arial", 14)).pack(pady=40)
    tk.Button(win, text="Close", command=win.destroy).pack()
    win.mainloop()

def clear_form():
    for widget in register_frame.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
    for widget in login_frame.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)

def show_login_form():
    register_frame.pack_forget()
    login_frame.pack(pady=20)

def show_register_form():
    login_frame.pack_forget()
    register_frame.pack(pady=20)

# --- Main Window ---
root = tk.Tk()
root.title("User Auth")
root.geometry("400x400")

# --- Register Frame ---
register_frame = tk.Frame(root)

tk.Label(register_frame, text="--- Register ---", font=("Arial", 12, "bold")).grid(row=0, columnspan=2, pady=10)
tk.Label(register_frame, text="Name").grid(row=1, column=0, sticky="w", padx=10)
name_entry = tk.Entry(register_frame, width=30)
name_entry.grid(row=1, column=1)

tk.Label(register_frame, text="Email").grid(row=2, column=0, sticky="w", padx=10)
email_entry = tk.Entry(register_frame, width=30)
email_entry.grid(row=2, column=1)

tk.Label(register_frame, text="Age").grid(row=3, column=0, sticky="w", padx=10)
age_entry = tk.Entry(register_frame, width=30)
age_entry.grid(row=3, column=1)

tk.Label(register_frame, text="Password").grid(row=4, column=0, sticky="w", padx=10)
password_entry = tk.Entry(register_frame, show="*", width=30)
password_entry.grid(row=4, column=1)

tk.Button(register_frame, text="Register", command=register_user).grid(row=5, column=1, pady=10, sticky="e")
tk.Button(register_frame, text="Go to Login", command=show_login_form).grid(row=6, column=1, pady=5, sticky="e")

register_frame.pack(pady=20)

# --- Login Frame ---
login_frame = tk.Frame(root)

tk.Label(login_frame, text="--- Login ---", font=("Arial", 12, "bold")).grid(row=0, columnspan=2, pady=10)

tk.Label(login_frame, text="Email").grid(row=1, column=0, sticky="w", padx=10)
login_email_entry = tk.Entry(login_frame, width=30)
login_email_entry.grid(row=1, column=1)

tk.Label(login_frame, text="Password").grid(row=2, column=0, sticky="w", padx=10)
login_password_entry = tk.Entry(login_frame, show="*", width=30)
login_password_entry.grid(row=2, column=1)

tk.Button(login_frame, text="Login", command=login_user).grid(row=3, column=1, pady=10, sticky="e")
tk.Button(login_frame, text="Go to Register", command=show_register_form).grid(row=4, column=1, sticky="e")

# Start with registration form
show_register_form()

root.mainloop()
