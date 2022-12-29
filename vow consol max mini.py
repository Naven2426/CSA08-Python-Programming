n=input("Enter the String :")
x=y=0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        x=x+1
    elif i.isalpha():
        y=y+1
print("The vowels in given String are :",x)
print("The consonant in given String are :",y)
if x>y:
    print("vowels are in maximum number")
else:
    print("consonant are in maximum number")
