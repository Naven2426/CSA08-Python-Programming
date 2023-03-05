n=input("Enter the string :")
x=0
for i in n:
    if i in 'aeiouAEIOU':
        x+=1
print("Vowel in given string :",x)
