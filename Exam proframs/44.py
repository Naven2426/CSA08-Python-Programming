import math
n = int(input("Enter a perfect square number: "))
if int(math.sqrt(n))**2 == n:
    sqrt_n = math.sqrt(n)
    print("The square root of", n, "is", sqrt_n, "or", -sqrt_n)
else:
    print(n, "is not a perfect square number.")
