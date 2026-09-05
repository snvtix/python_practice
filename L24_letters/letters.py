with open("L24_letters/Input/names.txt") as file:
    names = file.read()
    names = names.split("\n")

with open("L24_letters/Input/starting_letter.txt") as file:
    letter = file.read()

for name in names:
    new_letter = letter.replace("[name]", name)
    path = "L24_letters/Output/letter_" + name + ".txt"
    with open(path, "w") as file:
        file.write(new_letter)
