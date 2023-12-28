import random

names = input("Enter the names of people who will be paying (separated by space): ")
names_list = names.split(" ")
random_int=random.randint(0,len(names_list)-1)
print(f"{names_list[random_int]} should be paying this bill")
