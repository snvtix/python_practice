import pandas as pd
data = pd.read_csv("L26_nato_alphabet/nato_phonetic_alphabet.csv")

alphabet = {row.letter:row.code for (index, row) in data.iterrows()}
print(alphabet)

word = input("please enter a word: ").upper()
print(word)

code = [alphabet[letter] for letter in word if letter in alphabet.keys()]
print(code)