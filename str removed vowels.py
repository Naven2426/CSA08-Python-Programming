a=input("Enter the string :")
b=""
for i in a:
    if i not in 'AEIOUaeiou':
        b=b+i
print("The string after removing vowels :",b)
