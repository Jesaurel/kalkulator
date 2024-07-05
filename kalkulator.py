import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            result = format_result(result)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "←":
        current_text = entry.get()
        entry.delete(len(current_text) - 1, tk.END)
    else:
        entry.insert(tk.END, text)

def format_result(result):
    if "." in result:
        result = result.rstrip("0").rstrip(".")
    return result

root = tk.Tk()
root.title("Simple Calculator")

# Mengatur gaya latar belakang dengan warna solid yang lembut
root.configure(bg='#F0F0F0')

# Membuat frame utama
frame = tk.Frame(root, bg='#F0F0F0')
frame.grid(padx=10, pady=10)

# Entry dengan gaya khusus
entry = tk.Entry(frame, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify='right', bg='#FFFFFF', fg='#333333', insertbackground='#333333')
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    '←'
]

row_val = 1
col_val = 0

# Mengatur warna tombol
button_bg = '#4CAF50'  # Hijau lembut
button_active_bg = '#45A049'  # Hijau lebih gelap untuk efek aktif
button_fg = '#FFFFFF'  # Warna teks putih

for button in buttons:
    btn = tk.Button(frame, text=button, font=('Arial', 18), width=4, height=2, relief='flat', bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_fg)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Menambahkan gaya modern pada tombol
for widget in frame.winfo_children():
    if isinstance(widget, tk.Button):
        widget.config(highlightthickness=0, bd=0, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_fg)
        widget.bind("<Enter>", lambda e: e.widget.config(bg=button_active_bg))
        widget.bind("<Leave>", lambda e: e.widget.config(bg=button_bg))

# Mengatur gaya window
root.geometry("350x500")
root.resizable(False, False)

root.mainloop()
