student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO: 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

letters = pd.read_csv('/Users/kim-youngho/Desktop/python_1_100/NATO_alphabet/nato_phonetic_alphabet.csv')

new_letter = {row.letter:row.code for (index, row) in letters.iterrows()}
#print(new_letter)


#TODO: 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = list(input("Enter your message : ").upper())
cleaned_user_input = [char for char in user_input if char != ' ']

print(type(cleaned_user_input))


result = []
for char in cleaned_user_input:
    result.append(new_letter[char])

print(result)