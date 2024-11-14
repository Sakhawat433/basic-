scores = [70, 90, 60, 50, 25, 65, 85]
sum_score= 0
max_score = scores[0]
for score in scores:
    sum_score = sum_score + score
    if score > max_score:
        max_score = score
ave = sum_score/ len(scores)
print("The sum of the scores is:", sum_score)
print("The Average of the scores is:", ave)
print(f"The maximum score is:", max_score)




