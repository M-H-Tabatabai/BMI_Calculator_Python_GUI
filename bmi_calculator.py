#imports and define global variable


#get user inputs
def user_input():
    weight = input("please enter your weight (kg) : ")
    height = input("please enter your height : (m.cm)")
    return weight, height

#calculate bmi
def calculate_bmi(weight, height):
    bmi = weight // (height**2)
    return bmi

#show results
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


#main