# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# print(squared_numbers)


# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num % 2 == 0 and num != 0]
# print(result)

# with open('file1.txt', 'r',) as f:
#     file1 = [int(line.strip()) for line in f.readlines()]
# print(file1)

# with open('file2.txt','r') as f:
#     file2 = [int(line.strip()) for line in f.readlines()]
# print(file2)

# result = [num for num in file1 if num in file2]  

# print(result)


# import random

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
 
# students_score = {student : random.randint(1, 100)  for student in names}

# passed_students = {student : score for (student, score) in students_score.items() if score >= 60}

# print(passed_students)

student_dic = {
    'student' : ['Angela', 'James', 'Lily'],
    'score' : [56, 76, 98]
}

import pandas as pd

student_data_frame = pd.DataFrame(student_dic)
print(student_data_frame)

