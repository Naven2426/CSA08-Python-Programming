x=[]
a=int(input("Enter the length of list :"))
for i in range(a):
    x.append(int(input("Enter element "+str(i+1)+":")))
x.sort()
m=int(input("Enter value of M maximum:"))
n=int(input("Enter value of N maximum:"))
print("M th maximum :",x[-1*m])
print("N th maximum :",x[n-1])
print("Sum :",x[-1*m]+x[n-1])
print("Difference :",x[-1*m]-x[n-1])
print("Product :",x[-1*m]*x[n-1])
