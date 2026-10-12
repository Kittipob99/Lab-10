import tkinter as tk

def convert():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9 / 5) + 32
        result_label.config(
            text=f"Fahrenheit: {fahrenheit:.2f}"
        )
    except ValueError:
        result_label.config(
            text="Please enter a valid number!"
        )

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("350x200")

title_label = tk.Label(
    window, text="Celsius to Fahrenheit",
    font=("Arial", 16)
)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

input_label = tk.Label(window, text="Celsius:")
input_label.grid(row=1, column=0, padx=10, pady=5)

entry_celsius = tk.Entry(window)
entry_celsius.grid(row=1, column=1, padx=10, pady=5)

convert_button = tk.Button(
    window, text="Convert", command=convert
)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="Fahrenheit: ")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()
