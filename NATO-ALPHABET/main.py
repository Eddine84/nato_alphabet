student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
imported_csv = pandas.read_csv("./nato_phonetic_alphabet.csv")
result = pandas.DataFrame(imported_csv)
new_data = {row.letter:row.code for (index,row) in result.iterrows()}

def generate_phonetic():

    question_name = input("please provide your name").upper()
    try:
        question_name_chars_list = [new_data[char] for char in question_name]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:   
        print(question_name_chars_list)

generate_phonetic()