# in this project that for second day of 100DaysOfCodes,
# We want to write a program that calculate How much will each person pay?
# We should do it with  bill amount, number of person and tip amount.
# version 1: with set variables for calculating


bill = float(input("Enter the total cost of bill: "))
tip_percent = float(input("Enter the percent of tip you would like to give: "))
people = int(input("Enter the number of people to split the bill: "))
total = bill * (1 + tip_percent / 100)
print("each person should pay: ", total / people)
