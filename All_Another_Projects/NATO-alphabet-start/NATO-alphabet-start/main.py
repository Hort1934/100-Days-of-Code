student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    # print(key, value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
score = pandas.read_csv("nato_phonetic_alphabet.csv")
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# print(score)
#TODO 1. Create a dictionary in this format:
data = {y.letter: y.code for (x, y) in score.iterrows()}
# print(data)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output = [data[letter] for letter in word]
print(output)

