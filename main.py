#Basic python program
def get_average_score(scores_list):
    """Calculates the average of all numbers in a list."""
    total = sum(scores_list)
    average = total / len(scores_list)
    return round(average, 1)

# Variables and List
student_name = "Maya"
quiz_scores = [88, 92, 79, 95]

# Using the function
average_score = get_average_score(quiz_scores)

# Conditional check using variables
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
else:
    letter_grade = "C"

# Loop to display individual scores
print(f"--- Grade Report for {student_name} ---")
for index, score in enumerate(quiz_scores, start=1):
    print(f"Quiz {index}: {score}")

print(f"Final Average: {average_score} ({letter_grade})")