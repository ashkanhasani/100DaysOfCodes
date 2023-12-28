# in this exercise we want to love calculate with
# https://www.buzzfeed.com/sarathompson1/ai-love-compatibility-calculator-quiz formula

your_name = input("What is your name? ")
partner_name = input("What is your partner name? ")
combine_name = (your_name + partner_name).lower()
t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")
first_score_digit = t + r + u + e
l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")
second_score_digit = l + o + v + e
love_score = first_score_digit * 10 + second_score_digit
if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score} , you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score} , you are all right together")
else:
    print(f"Your score is {love_score}")
