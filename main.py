#Data Types

print("Hello"[4])

print(123 + 345)



#fstring
score = 0
height = 1.8
isWinning = True
#f-string 
print(f"your score is{score}, your height is {height}, you are winning is {isWinning}")

# time left calculator
age = input("What is your current age? ")
yearsleft = int(90) - int(age)
monthsleft = yearsleft * 12
weeksleft = yearsleft * 52)
daysleft = yearsleft * 365
print(f"You have {daysleft} days, {weeksleft} weeks, and {monthsleft} months left.")

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round((weight / height ** 2))
if BMI < 18.50:
    print(f"Your BMI is {BMI}, you are underweight")
elif 18.50 < BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight") 
elif 25 < BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight") 
elif 30 < BMI < 35:
    print(f"Your BMI is {BMI}, you are obese")
elif 35 < BMI:
    print(f"Your BMI is {BMI}, you are clinically obese") 
