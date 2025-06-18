# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:43:56 2025

@author: Νικος Μπισμπιγιαννης
"""

import tkinter as tk

# Δημιουργία παραθύρου
root = tk.Tk()
root.title("Αριθμομηχανή")
root.geometry("320x500")
root.minsize(320, 500)
root.resizable(False, False)

# Κάνει τις στήλες & γραμμές επεκτάσιμες
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    
# Πεδίο εισαγωγής
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="groove", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Πεδίο Ιστορικού
history = tk.Text(root, height=8, width=25, font=("Arial", 12))
history.grid(row=1, column=0, columnspan=4, padx=10, pady=(0, 10))
history.config(state='disabled')  # Το κάνουμε μόνο για ανάγνωση

# Συνάρτηση για πάτημα κουμπιών
def button_click(value):
    current = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
        history.config(state='normal')
        history.delete('1.0', tk.END)
        history.config(state='disabled')
    elif value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))

            # Προσθήκη στο ιστορικό
            history.config(state='normal')
            history.insert(tk.END, f"{current} = {result}\n")
            history.config(state='disabled')
            history.see(tk.END)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, value)

# Πλήκτρα αριθμομηχανής
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Δημιουργία κουμπιών
for row_index, row in enumerate(buttons):
    for col_index, value in enumerate(row):
        button = tk.Button(
            root,
            text=value,
            font=("Arial", 18),
            width=5,
            height=2,
            command=lambda v=value: button_click(v)
        )
        button.grid(row=row_index + 2, column=col_index, padx=5, pady=5)  # Ξεκινάει από row 2 λόγω entry + ιστορικού

# Χειρισμός πληκτρολογίου
def key_press(event):
    key = event.char
    if key in '0123456789+-*/':
        entry.insert(tk.END, key)
    elif key == '\r':  # Enter
        button_click('=')
    elif key.lower() == 'c':
        button_click('C')
    elif key == '\x08':  # Backspace
        current = entry.get()
        if current:
            entry.delete(len(current)-1)

# Σύνδεση event πληκτρολογίου
root.bind('<Key>', key_press)

# Εκκίνηση του GUI
root.mainloop()
