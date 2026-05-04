# imports and define global variable
import tkinter as tk
from tkinter import ttk,messagebox


# get user inputs
# def user_input():
#     weight = float(input("please enter your weight (kg) : "))
#     height = float(input("please enter your height (m.cm) : "))
#     return weight, height


# calculate bmi
def calculate_bmi(entry_weight, entry_height, label_bmi_value,label_category_value ):
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if height <= 0 or weight <= 0:
            raise ValueError

        bmi = weight / (height ** 2)
        category = show_category(bmi)


        label_bmi_value.config(text=f"{bmi:.2f}")
        label_category_value.config(text=category)

    except ValueError:
        messagebox.showerror("خطا", "لطفاً مقادیر معتبر وارد کنید.")


# show results
def show_category(bmi):
    if bmi < 18.5:
        return "under weight"
    elif bmi < 25:
        return "normal weight"
    elif bmi < 30:
        return "over weight"
    elif bmi < 35:
        return "obese"
    else:
        return "extremely obese"


# main
def main():

    root = tk.Tk()
    root.title("BMI Calculator")
    root.geometry("1000x500")

    label_weight = ttk.Label(root, text="Weight (kg):", font=("Arial", 12))
    label_weight.place(relx=0.1, rely=0.35, anchor="w")
    entry_weight = ttk.Entry(root, width=20)
    entry_weight.place(relx=0.3, rely=0.35, anchor="center")

    label_height = ttk.Label(root, text="Height (m):", font=("Arial", 12))
    label_height.place(relx=0.1, rely=0.55, anchor="w")
    entry_height = ttk.Entry(root, width=20)
    entry_height.place(relx=0.3, rely=0.55, anchor="center")

    # weight, height = entry_weight, entry_height
    # bmi = calculate_bmi(weight, height, label_bmi_value, label_category_value)

    label_bmi_value = ttk.Label(root, text="---", font=("Arial", 12), anchor="center")
    label_category_value = ttk.Label(root, text="---", font=("Arial", 12), anchor="center")

    label_bmi_value.place(relx=0.9, rely=0.35, anchor="center")
    label_category_value.place(relx=0.9, rely=0.55, anchor="center")

    btn_calc = ttk.Button(
    root,
    text="محاسبه",
    command=lambda: calculate_bmi(entry_weight, entry_height, label_bmi_value, label_category_value))

    btn_calc.place(relx=0.5, rely=0.5, anchor="center")


    btn_close = ttk.Button(root, text="Exit", command=root.destroy)
    btn_close.place(relx=0.5, rely=0.9, anchor="center")
    root.mainloop()


if __name__ == "__main__":
    main()
