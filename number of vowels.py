n=input("Enter the String :")
x=0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        x=x+1
print("The vowels in given String are :",x)
