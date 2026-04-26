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


#main