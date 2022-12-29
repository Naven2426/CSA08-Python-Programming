str1=input("Enter the First String :")
str2=input("Enter the Second String :")
str1=str1.lower()
str2=str2.lower()
if len(str1)==len(str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
if(sorted_str1 == sorted_str2):
    print("The given value are anagram")
else:
    print("The given value are not anagram")
