import tkinter as tk
import math

def press(event):
    current = display.get()
    text = event.widget.cget("text")

    if text == 'C':
        display.delete(0, tk.END)
    elif text == '=':
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except ZeroDivisionError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Division by zero")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, f"Error: {str(e)}")
    elif text in ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', '^', '%']:
        try:
            if text == 'sin':
                result = math.sin(math.radians(float(current)))
            elif text == 'cos':
                result = math.cos(math.radians(float(current)))
            elif text == 'tan':
                result = math.tan(math.radians(float(current)))
            elif text == 'log':
                result = math.log10(float(current))
            elif text == 'ln':
                result = math.log(float(current))
            elif text == 'sqrt':
                result = math.sqrt(float(current))
            elif text == '^':
                display.insert(tk.END, '**')
                return
            elif text == '%':
                result = float(current) / 100
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, f"Error: {str(e)}")
    else:
        display.insert(tk.END, text)

screen = tk.Tk()
screen.title("Scientific Calculator")

display = tk.Entry(screen, font=("Arial", 20), justify="right")
display.pack(fill=tk.X, padx=20, pady=10, ipadx=5, ipady=10)

button_frame = tk.Frame(screen)
button_frame.pack()

button_key = [
    "7", "8", "9", "*",
    "4", "5", "6", "+",
    "1", "2", "3", "-",
    "C", "0", "=", "/",
    "sin", "cos", "tan", "sqrt",
    "log", "ln", "^", "%"
]

i = 0

for keys in button_key:
    button = tk.Button(button_frame, text=keys, font=("Arial", 20), padx=20, pady=20)
    button.grid(row=i//4, column=i%4, padx=10, pady=10)
    button.bind("<Button-1>", press)
    i += 1

screen.mainloop()
