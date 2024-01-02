# calc the sum of even numbers between 1,100 including 1 and 100
summ = 0
for i in range(2, 101, 2):
    summ += i

print(f"sum = {summ}")
