a= input("Enter Date (dd/mm/yyyy): ")
b = a.split("/")
y= int(b[2])
if (y%4 == 0 and y%100!= 0) or y % 400 == 0:
    print("Given year is Leap Year")
else:
    print("Given year is Non Leap Year")
