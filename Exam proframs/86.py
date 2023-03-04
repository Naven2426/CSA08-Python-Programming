word = input("Enter the word: ")
repeated = set()
count = 0
for letter in word:
    if letter in repeated:
        continue
    if word.count(letter) > 1:
        count += 1
        repeated.add(letter)
print("Number of repeated letters =", count)
