import random

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_list = [i for i in alpha]
number_list = [str(i) for i in range(10)]
symbol_list = [i for i in "!@#$%^&*+-"]

length = int(input("How many char do you want in your password?"))
number = int(input("How many number do you want?"))
symbol = int(input("How many symbol do you want?"))

choice_list = []
choice_list.extend(random.choices(number_list, k=number))
choice_list.extend(random.choices(symbol_list, k=symbol))
choice_list.extend(random.choices(alpha_list, k=length - number - symbol))

random.shuffle(choice_list)

password = ""
for i in choice_list:
    password += i

print(password)
