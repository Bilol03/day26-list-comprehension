# NATO Alphabet help project
import pandas as pd

file = pd.read_csv('./nato_phonetic_alphabet.csv')

csv_dict = {values.letter: values.code for (keys, values) in file.iterrows()}
# print(csv_dict)

user_input = input("Enter your name: ")

NATO = [csv_dict[letter.upper()] for letter in user_input]
print(NATO)



# number_list = [number for number in range(1,5)]
# print(number_list)
#
# names = ["Bilol", "Shahzod", "Elyor", "Bunyod", "Asad", "Doni"]
#
# short_name = [name for name in names if len(name) < 6f]
# print(short_name)

# file = open()

