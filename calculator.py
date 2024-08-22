import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

# Applies weight so bozes stretch evenly when stretching app window
root.grid_columnconfigure((1, 2, 3, 4), weight=1)  # Add equal weight to all button columns except 0
root.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)  # Add equal weight to all rows except 0

# Result Box
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(row=1, column=1, columnspan=5, sticky="nsew")  # Make result box stretch fully

# Buttons
btn_text = [
    ('1', 2, 1), ('2', 2, 2), ('3', 2, 3), 
    ('4', 3, 1), ('5', 3, 2), ('6', 3, 3), 
    ('7', 4, 1), ('8', 4, 2), ('9', 4, 3), 
    ('0', 5, 2), ('+', 2, 4), ('-', 3, 4),
    ('*', 4, 4), ('/', 5, 4), ('(', 5, 1), 
    (')', 5, 3), ('=', 6, 1), ('C', 6, 3)
]

# Place buttons
for (text, row, col) in btn_text:
    if text == '=':
        btn = tk.Button(root, text=text, command=evaluate_calculation, width=11, font=("Arial", 14))
        btn.grid(row=row, column=col, columnspan=2, sticky="nsew")
    elif text == 'C':
        btn = tk.Button(root, text=text, command=clear_field, width=11, font=("Arial", 14))
        btn.grid(row=row, column=col, columnspan=2, sticky="nsew")
    else:
        btn = tk.Button(root, text=text, command=lambda x=text: add_to_calculation(x), width=5, font=("Arial", 14))
        btn.grid(row=row, column=col, sticky="nsew")

root.mainloop()