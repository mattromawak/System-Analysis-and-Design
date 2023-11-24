import tkinter as tk
import os

def run_fingercount():
    root.destroy() 
    os.system('python "./screens/fingercount.py"') 

def run_main():
    root.destroy() 
    os.system('python "./screens/main.py"')

root = tk.Tk()
root.title("Choose Hand Detection") 
root.geometry("300x200") 
root.configure(bg='#ADD8E6') 

label = tk.Label(root, text="Select mode:", font=("Arial", 14), bg='#ADD8E6')
label.pack(pady=20)

button1 = tk.Button(root, text="Fingercount", command=run_fingercount, font=("Arial", 12), bg='#ADD8E6', fg='#000000')
button1.pack(pady=10)

button2 = tk.Button(root, text="Hand Gesture Recognition", command=run_main, font=("Arial", 12), bg='#ADD8E6', fg='#000000')
button2.pack(pady=10)

root.mainloop()
