a=str(input("Enter the Character to be printed :"))
b=int(input("Max number of time printed :"))
for i in range(b):
    for j in range(i+1):
        print(a,end="")
    print()

