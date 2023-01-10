# Day 2 / Exercise 1 - Data Types

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
a = int(two_digit_number[0])
b = int(two_digit_number[1])

print(a+b)

# Day 2 / Exercise 2 - BMI Calculator 

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(int(int(weight) / (float(height) * float(height))))

# Age in weeks challenge

age = input("What is your current age")
years = 90 - int(input)
days = years * 365
weeks = years * 52
months = years * 12

print(f"You have {days} days, {weeks} weeks, {months} months left.")

# Bill Calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print(f"Welcome to the tip calculator!")
bill_total = input("What was the total? $")
tip_perc = input("How much would you like to leave as tip? ")
num_people = input("How many people are paying? ")
bill = float(bill_total)
people = int(num_people)
tip = int(tip_perc)
bill_plus_tip = bill * 1+tip
split = "{:.2f}".format(bill_plus_tip / people)
print(f"Each person should pay ${split}")