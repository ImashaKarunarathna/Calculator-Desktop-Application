import tkinter as tk
from tkinter import messagebox

# Function to create a gradient background
def create_gradient(canvas, width, height, color1, color2):
    canvas.delete("gradient")  # Remove any previous gradient lines
    for i in range(height):
        r1, g1, b1 = [int(color1[j:j+2], 16) for j in (1, 3, 5)]
        r2, g2, b2 = [int(color2[j:j+2], 16) for j in (1, 3, 5)]
        r = int(r1 + (r2 - r1) * i / height)
        g = int(g1 + (g2 - g1) * i / height)
        b = int(b1 + (b2 - b1) * i / height)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color, width=1, tags="gradient")

# Function to update the background color of the OptionMenu based on the selected operator
def update_operator_color(*args):
    operator = operation_var.get()
    color_map = {
        '+': '#FFB6C1',  # Light pink
        '-': '#FF69B4',  # Hot pink
        '*': '#FFB6C1',  # Orange red
        '/': '#FF69B4',  # Gold
        '**': '#FFB6C1', # Goldenrod
        '%': '#FF69B4',  # Light salmon
    }
    color = color_map.get(operator, '#BA55D3')  # Default to existing color if operator not found
    operation_menu.config(bg=color)

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        elif operation == '**':
            result = num1 ** num2
        elif operation == '%':
            result = num1 % num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to clear input fields
def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("800x600")

# Update the main window background color
root.configure(bg="#add8e6")  # Change to a light blue background

# Create a canvas for the gradient background
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Draw the initial gradient
create_gradient(canvas, root.winfo_width(), root.winfo_height(), "#8A2BE2", "#4B0082")

# Create a frame to hold the content and center it
frame = tk.Frame(root, bg="#6A0DAD", bd=5, width=500, height=400)  # Set a fixed size for the frame
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

# Input fields for numbers with custom font
entry1 = tk.Entry(frame, width=15, font=("Arial", 12), bg="#D8BFD8", fg="black")
entry1.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
entry2 = tk.Entry(frame, width=15, font=("Arial", 12), bg="#D8BFD8", fg="black")
entry2.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

# Labels for input fields with custom font and color
tk.Label(frame, text="First Number:", font=("Arial", 12), fg="white", bg="#6A0DAD").grid(row=0, column=0, padx=20, pady=20)
tk.Label(frame, text="Second Number:", font=("Arial", 12), fg="white", bg="#6A0DAD").grid(row=1, column=0, padx=20, pady=20)

# Dropdown menu for operation selection
operation_var = tk.StringVar(root)
operation_var.set('+')  # Default value
operation_var.trace_add("write", update_operator_color)  # Update color on change

operation_menu = tk.OptionMenu(frame, operation_var, '+', '-', '*', '/', '**', '%')
operation_menu.config(bg="#BA55D3", fg="white", font=("Arial", 12))  # Menu color
operation_menu.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

tk.Label(frame, text="Operation:", font=("Arial", 12), fg="white", bg="#6A0DAD").grid(row=2, column=0)

# Button to perform the calculation with custom font and color
calculate_button = tk.Button(frame, text="Calculate", font=("Arial", 12), fg="white", bg="#8A2BE2", command=calculate)
calculate_button.grid(row=3, column=1, padx=20, pady=20, sticky="ew")

# Clear button
clear_button = tk.Button(frame, text="Clear", font=("Arial", 12), fg="white", bg="#D8BFD8", command=clear_fields)
clear_button.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

# Label to display the result with custom font and color
result_label = tk.Label(frame, text="Result: ", font=("Arial", 34), fg="white", bg="#6A0DAD")
result_label.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

# Redraw the gradient after changing the background
canvas.bind("<Configure>", lambda event: create_gradient(canvas, event.width, event.height, "#8A2BE2", "#4B0082"))

# Run the main loop
root.mainloop()
