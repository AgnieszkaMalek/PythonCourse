# Create a list of test score
scores = [50, 75, 85, 95, 100]

# Use floor division to calculate the average score
total_score = sum(scores) # scores in total 405
num_tests = len(scores) # 5 scores in the list
average_score = total_score // num_tests # average 81
grade = ""

# Use comparison operators to determine the grade based on the average score.
if average_score == 100:
    grade = "A+"
elif average_score >= 95:
    grade = "A"
elif average_score >= 85:
    grade = "B"
elif average_score >= 75:
    grade = "C"
elif average_score >= 50:
    grade = "D"
elif average_score <= 50:
    grade = "F"

# Use assignment operators to update the student's grade.
if average_score % 10 >= 5:
    grade += "+"

# Displaying student's grade
print("The student's average score is", average_score, "and the grade is",grade)

#Use membership operators to check if a specific score exists in the list of scores.
specific_score = 75
if specific_score in scores:
    print("The score", specific_score, "exists in scores")
else:
    print(("The score", specific_score, "doesn't exist in scores"))

# Use identity operators to compare objects.
copy_of_scores = scores

if scores is copy_of_scores:
    print("Object \"scores\" and \"copy_of_scores\" are the same objects")
else:
    print("The object \"score\" is different from object \"copy_of_score\"")

# Use bitwise operators to perform bitwise operations on the scores.
bitwise_and_operation = scores[0] & scores [-1] # first score 50 last score 100
print("Bitwise AND operation on the first and the last score is", bitwise_and_operation)

bitwise_or_operation = scores[0] | scores [-1] # first score 50 last score 100
print("Bitwise OR operation on the first and the last score is", bitwise_or_operation)


