import tkinter as tk  # Mengimpor pustaka Tkinter untuk membuat GUI
from math import sqrt, sin, cos, tan, log  # Mengimpor fungsi matematika yang akan digunakan

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Python")  # Menetapkan judul jendela
        self.expression = ""  # Menyimpan ekspresi matematika yang sedang dibangun

        # Membuat widget entry untuk menampilkan input dan hasil
        self.entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.entry.bind("<Key>", self.validate_keypress)  # Mengikat fungsi validasi ke input keyboard

        # Daftar label tombol yang akan dibuat
        button_labels = [
            '7', '8', '9', '/', 'C',  # Baris pertama tombol
            '4', '5', '6', '*', 'sqrt',  # Baris kedua tombol
            '1', '2', '3', '-', '^',  # Baris ketiga tombol
            '0', '.', '=', '+', 'log',  # Baris keempat tombol
            '(', ')', 'sin', 'cos', 'tan'  # Baris kelima tombol
        ]

        row = 1  # Baris awal untuk penempatan tombol
        col = 0  # Kolom awal untuk penempatan tombol
        for label in button_labels:
            # Membuat tombol dengan label yang sesuai
            button = tk.Button(root, text=label, padx=20, pady=20, font=('Arial', 12))
            if label not in ['C', '=', 'sqrt', 'log', 'sin', 'cos', 'tan']:
                button.config(command=lambda l=label: self.on_button_click(l))  # Mengatur fungsi tombol biasa
            elif label == 'C':
                button.config(command=self.on_clear)  # Fungsi tombol Clear
            elif label == '=':
                button.config(command=self.on_equal)  # Fungsi tombol sama dengan
            else:
                button.config(command=lambda l=label: self.on_function_click(l))  # Fungsi tombol fungsi matematika khusus
            
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')  # Menempatkan tombol di grid
            col += 1
            if col > 4:  # Pindah ke baris berikutnya jika kolom melebihi 4
                col = 0
                row += 1

        # Mengatur bobot grid untuk membuat tombol bersifat responsif
        for i in range(5):
            root.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            root.grid_rowconfigure(i, weight=1)

    def validate_keypress(self, event):
        valid_keys = "0123456789+-*/().^"  # Karakter yang diizinkan
        if event.char in valid_keys:
            return True  # Mengizinkan karakter yang valid
        elif event.keysym in ('Return', 'BackSpace'):
            return True  # Mengizinkan tombol Enter dan BackSpace
        else:
            return "break"  # Menghentikan input karakter yang tidak valid

    def on_button_click(self, char):
        self.expression += str(char)  # Menambahkan karakter ke ekspresi
        self.entry.delete(0, tk.END)  # Menghapus isi entry
        self.entry.insert(tk.END, self.expression)  # Menampilkan ekspresi yang diperbarui

    def on_function_click(self, func):
        if func == 'sqrt':
            self.expression += 'sqrt('  # Menambahkan 'sqrt(' ke ekspresi
        elif func == 'log':
            self.expression += 'log('  # Menambahkan 'log(' ke ekspresi
        elif func == 'sin':
            self.expression += 'sin('  # Menambahkan 'sin(' ke ekspresi
        elif func == 'cos':
            self.expression += 'cos('  # Menambahkan 'cos(' ke ekspresi
        elif func == 'tan':
            self.expression += 'tan('  # Menambahkan 'tan(' ke ekspresi
        self.entry.delete(0, tk.END)  # Menghapus isi entry
        self.entry.insert(tk.END, self.expression)  # Menampilkan ekspresi yang diperbarui

    def on_clear(self):
        self.expression = ""  # Mengosongkan ekspresi
        self.entry.delete(0, tk.END)  # Menghapus isi entry

    def on_equal(self):
        try:
            self.expression = self.expression.replace('^', '**')  # Mengganti '^' dengan '**' untuk eksponen
            result = eval(self.expression)  # Mengevaluasi ekspresi matematika
            self.entry.delete(0, tk.END)  # Menghapus isi entry
            self.entry.insert(tk.END, str(result))  # Menampilkan hasil
            self.expression = str(result)  # Menyimpan hasil sebagai ekspresi baru
        except Exception as e:
            self.entry.delete(0, tk.END)  # Menghapus isi entry
            self.entry.insert(tk.END, "Error")  # Menampilkan pesan error
            self.expression = ""  # Mengosongkan ekspresi

if __name__ == "__main__":
    root = tk.Tk()  # Membuat instance Tkinter
    calculator = Calculator(root)  # Membuat instance kalkulator
    root.mainloop()  # Memulai loop utama Tkinter
