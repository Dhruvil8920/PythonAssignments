"""
You are given a 3D NumPy array representing the scores of students in multiple subjects.
Each row represents a student, and each column represents a subject.
Write a program that takes the array as input and calculates the average score for each student.
The program should then output the average scores.

Example:

Input:
scores = np.array([
    [[80, 90, 75], [85, 92, 88]],
    [[77, 82, 79], [90, 85, 88]],
    [[92, 88, 95], [78, 85, 90]],
    [[85, 90, 88], [82, 79, 90]]
])

Output: Average Scores:
[[ 82.5  91.   81.5]
 [ 83.5  83.5  83. ]
 [ 85.   86.5  92.5]
 [ 83.5  84.5  89. ]]

"""

def calculate_average_scores(scores):
    "Write your logic here"