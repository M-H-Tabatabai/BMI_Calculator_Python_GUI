# imports and define global variable
import tkinter as tk
from tkinter import ttk


# get user inputs
def user_input():
    weight = float(input("please enter your weight (kg) : "))
    height = float(input("please enter your height (m.cm) : "))
    return weight, height


# calculate bmi
def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi


# show results
def show_result(bmi):
    if bmi < 18.5:
        return "under weight"
    elif bmi < 25:
        return "normal weight"
    elif bmi < 30:
        return "over wight"
    elif bmi < 35:
        return "obese"
    else:
        return "extremely obese"


# main
def main():

    weight, height = user_input()
    bmi = calculate_bmi(weight, height)
    result = show_result(bmi)
    bmi_txt, result_txt = bmi, result
    print(f"{bmi_txt}, {result_txt}")
    root = tk.Tk()
    root.title("Results")
    root.geometry("300x300")

    label1 = ttk.Label(root, text=f"{bmi:.2f}", font=("Arial", 14), anchor="center")
    label2 = ttk.Label(root, text=result_txt, font=("Arial", 14), anchor="center")

    label1.place(relx=0.5, rely=0.4, anchor="center")
    label2.place(relx=0.5, rely=0.5, anchor="center")

    btn_close = ttk.Button(root, text="Exit", command=root.destroy)
    btn_close.place(relx=0.5, rely=0.6, anchor="center")

    root.mainloop()


if __name__ == "__main__":
    main()
