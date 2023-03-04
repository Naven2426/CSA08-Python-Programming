word = input("Enter a word: ")
vowels = ""
consonants = ""
for i in word:
    if i.isalpha():
        if i in "aeiouAEIOU":
            vowels += i + " "
        else:
            consonants += i + " "
print("Consonants:", consonants)
print("Vowels:", vowels)
