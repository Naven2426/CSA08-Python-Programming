n=input("Enter a list of names, separated by commas: ").split(",")
b=input("Enter A for ascending or D for descending: ").upper()
if b=="A":
    sorted_n = sorted(n)
elif b=="D":
    sorted_n=sorted(n,reverse=True)
else:
    print("Invalid choice. Please enter A or D.")
    exit()
print("Sorted names:", ", ".join(sorted_n))
