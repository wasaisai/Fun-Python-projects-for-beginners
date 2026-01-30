import tkinter as tk
import calc
import cli

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
        
    #关闭gui
    def switch_to_cli():
        root.destroy()
    
    button = tk.Button(root, text="计算", command= on_click)
    button.pack(pady=10)
    
    but_switch = tk.Button(root, text="切换到 CLI", command=switch_to_cli)
    but_switch.pack(pady=10)

    root.mainloop()
    cli.run_cli()