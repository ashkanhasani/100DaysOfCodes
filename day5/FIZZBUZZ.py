for i in range(100):
    if i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    elif i % 15 == 0:
        print("FIZZBUZZ")
    else:
        print(i)
