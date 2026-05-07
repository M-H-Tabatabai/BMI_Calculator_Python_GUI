# Imports
import tkinter as tk
from tkinter import ttk, messagebox


# Calculate BMI
def calculate_bmi(entry_weight, entry_height, label_bmi_value, label_category_value):
    try:
        # Read user inputs
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        # Validate inputs
        if height <= 0 or weight <= 0:
            raise ValueError

        # BMI formula
        bmi = weight / (height**2)

        # Get BMI category
        category = show_category(bmi)
        category, color = show_category(bmi)

        # Update output boxes
        label_bmi_value.config(text=f"{bmi:.2f}")
        label_category_value.config(text=category, fg=color)

    except ValueError:
        # Show error if the input is invalid
        messagebox.showerror("Error", "Please enter valid numeric values.")


# BMI Category Function
def show_category(bmi):
    """
    Returns BMI classification based on the BMI value.
    """
    if bmi < 18.5:
        return "Under weight", "blue"
    elif bmi < 25:
        return "Normal weight", "green"
    elif bmi < 30:
        return "Over weight", "orange"
    elif bmi < 35:
        return "Obese", "darkorange"
    else:
        return "Extremely obese", "red"

# Main GUI Window
def main():

    # Create main window
    root = tk.Tk()
    root.title("BMI Calculator")

    # Center the window on the screen
    window_width = 1000
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x, y position for centering
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    # Apply window size and position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Input fields: Weight and Height
    label_weight = ttk.Label(root, text="Weight (kg):", font=("Arial", 12))
    label_weight.place(relx=0.1, rely=0.35, anchor="w")

    entry_weight = ttk.Entry(root, width=20)
    entry_weight.place(relx=0.3, rely=0.35, anchor="center")

    label_height = ttk.Label(root, text="Height (m):", font=("Arial", 12))
    label_height.place(relx=0.1, rely=0.55, anchor="w")

    entry_height = ttk.Entry(root, width=20)
    entry_height.place(relx=0.3, rely=0.55, anchor="center")

    # Output Boxes: BMI and Category
    label_bmi = ttk.Label(root, text="BMI:", font=("Arial", 12))
    label_bmi.place(relx=0.72, rely=0.35, anchor="w")

    label_bmi_value = tk.Label(
        root,
        text="",
        font=("Arial", 12),
        width=15,
        height=1,
        relief="solid",
        bd=1,
        bg="white",
        anchor="center",
    )
    label_bmi_value.place(relx=0.9, rely=0.35, anchor="center")

    label_category = ttk.Label(root, text="Category:", font=("Segoe UI Emoji", 12))
    label_category.place(relx=0.7, rely=0.55, anchor="w")

    label_category_value = tk.Label(
        root,
        text="",
        font=("Arial", 12),
        width=15,
        height=1,
        relief="solid",
        bd=1,
        bg="white",
        anchor="center",
    )
    label_category_value.place(relx=0.9, rely=0.55, anchor="center")

    # Buttons
    # Calculate Button
    
    btn_calc = ttk.Button(
        root,
        text="Calculate",
        command=lambda: calculate_bmi(
            entry_weight, entry_height, label_bmi_value, label_category_value
        ),
    )
    btn_calc.place(relx=0.5, rely=0.45, anchor="center")

    # Exit Button
    style = ttk.Style()
    style.configure("exit.TButton", foreground="red")
    btn_close = ttk.Button(root, text="Exit", command=root.destroy, style="exit.TButton")
    btn_close.place(relx=0.5, rely=0.9, anchor="center")

    # Run the application loop
    root.mainloop()


# Run program
if __name__ == "__main__":
    main()
