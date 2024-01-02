# calc the average height of a list of heights
height_list = input("Enter the numbers separated by spaces: ").split(" ")
heights_sum = 0
for height in height_list:
    heights_sum += int(height)
average = heights_sum / len(height_list)
print(average)
