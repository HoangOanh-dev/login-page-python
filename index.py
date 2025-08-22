import tkinter as tk
from tkinter import messagebox

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text='👁')
    else:
        password_entry.config(show='')
        toggle_btn.config(text='🙈')

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both fields")
    elif username == "admin" and password == "12345":
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# Tạo cửa sổ
root = tk.Tk()
root.title("Login UI")
root.geometry("350x400")
root.config(bg="#f0f5f5")

# Avatar
avatar = tk.Label(root, text="👤", font=("Arial", 50), bg="#f0f5f5", fg="#006666")
avatar.pack(pady=20)

# Ô nhập Username
username_entry = tk.Entry(root, font=("Arial", 12), bd=2, relief="groove")
username_entry.insert(0, "Enter username")
username_entry.pack(pady=10, ipadx=10, ipady=5)

# Frame cho mật khẩu + nút ẩn/hiện
password_frame = tk.Frame(root)
password_frame.pack(pady=10)

password_entry = tk.Entry(password_frame, font=("Arial", 12), bd=2, relief="groove", show="*")
password_entry.insert(0, "Enter password")
password_entry.pack(side=tk.LEFT, ipadx=10, ipady=5)

toggle_btn = tk.Button(password_frame, text="👁", command=toggle_password)
toggle_btn.pack(side=tk.LEFT, padx=5)

# Nút đăng nhập
login_btn = tk.Button(root, text="Login", font=("Arial", 14), bg="#006666", fg="white", width=15, command=login)
login_btn.pack(pady=20)

root.mainloop()

