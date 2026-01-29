import tkinter as tk
import calc

def run_gui():
    root = tk.Tk()
    root.title("计算器")
    root.geometry("300x200")
    
    entry = tk.Entry(root, font=("Arial", 14))
    entry.pack(pady=20)
    
    label = tk.Label(root, text="")
    label.pack(pady=10)
    
    def on_click():
        expr = entry.get()
        result = calc.calculate_express(expr)
        label.config(text=str(result))

    
    button = tk.Button(root, text="计算", command= on_click)
    button.pack()

    root.mainloop()