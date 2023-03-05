import math
def isPerfectSquare(n):
    return int(math.sqrt(n))**2 == n
def getSumOfDigits(n):
    return sum(map(int, str(n)))
start = 1
end = 100
result = []
for i in range(start, end+1):
    if isPerfectSquare(i) and getSumOfDigits(i) < 10:
        result.append(i)
print("Perfect squares with sum of digits less than 10:")
print(result)
