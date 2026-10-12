
import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    number_label.config(text=str(count))

def decrease():
    global count
    count -= 1
    number_label.config(text=str(count))

def reset():
    global count
    count = 0
    number_label.config(text=str(count))

window = tk.Tk()
window.title("Counter App")
window.geometry("300x250")

title_label = tk.Label(window, text="Counter", font=("Arial", 18))
title_label.pack(pady=10)

number_label = tk.Label(window, text="0", font=("Arial", 30))
number_label.pack(pady=10)

increase_button = tk.Button(
    window, text="Increase", command=increase
)
increase_button.pack(pady=5)

decrease_button = tk.Button(
    window, text="Decrease", command=decrease
)
decrease_button.pack(pady=5)

reset_button = tk.Button(
    window, text="Reset", command=reset
)
reset_button.pack(pady=5)

window.mainloop()
