#Defining varibales
def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100 #convert cm to metres
    bmi = weight_kg / (height_m ** 2) #formula for bmi
    return bmi
    
#Bmi Analysis
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "UNDERWEIGHT"
    elif 18.5 <= bmi < 25:
        return "NORMAL WEIGHT"
    elif 25 <= bmi < 30:
        return "OVERWEIGHT"
    else:
        return "OBESE"

#Main Program
print("BMI CALCULATOR USING PYTHON")

try:
    weight = float(input("Enter your weight in kg : "))
    height = float(input("Enter your height in cm : "))
    
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    print("Category of BMI :", category)
    
except ValueError:
    print("Please enter valid numbers only!")
    
