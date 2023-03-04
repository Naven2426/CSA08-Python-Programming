a= input("Enter a list of integers: ")
b= [int(x) for x in a.split(",")]
N = int(input("Enter the value of N: "))
b.sort(reverse=True)
print(N, "Largest number:", b[N-1])
