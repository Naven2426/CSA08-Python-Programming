word = input("Enter the word: ").upper()
vowels = []
consonants = []
for letter in word:
    if letter in "AEIOU":
        vowels.append(letter)
    else:
        consonants.append(letter)
vowels.sort()
consonants.sort()
print("Vowels in alphabetical order: " + ", ".join(vowels))
print("Consonants in alphabetical order: " + ", ".join(consonants))
