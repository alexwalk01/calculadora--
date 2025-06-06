import tkinter as tk
from tkinter import messagebox

# Función para sumar
def sumar():
    try:
        resultado = float(entry1.get()) + float(entry2.get())
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

# Función para restar
def restar():
    try:
        resultado = float(entry1.get()) - float(entry2.get())
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Calculadora Suma y Resta")
ventana.geometry("300x250")
ventana.config(bg="#f0f0f0")

# Título
tk.Label(ventana, text="Calculadora", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

# Entrada de números
entry1 = tk.Entry(ventana, font=("Arial", 12))
entry1.pack(pady=5)

entry2 = tk.Entry(ventana, font=("Arial", 12))
entry2.pack(pady=5)

# Botones
tk.Button(ventana, text="Sumar", command=sumar, width=10, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Restar", command=restar, width=10, bg="#f44336", fg="white").pack(pady=5)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado:", font=("Arial", 12), bg="#f0f0f0")
resultado_label.pack(pady=10)

ventana.mainloop()
