#  print the highest score from scores list

scores_list = input("Enter the scores separated by commas: ").split(",")
highest_score = 0
for score in scores_list:
    score = int(score)
    if score > highest_score:
        highest_score = score

print(highest_score)
