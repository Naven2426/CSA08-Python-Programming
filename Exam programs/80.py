n = int(input("Enter the number of terms: "))
a, b = -1, -1
print(a)
print(b)
for i in range(2, n):
    c = a - b
    print(c)
    a, b = b, c
