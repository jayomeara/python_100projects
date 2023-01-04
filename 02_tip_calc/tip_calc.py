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