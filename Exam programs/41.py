import math
n = int(input("Enter the number of values: "))
nums = []
for i in range(n):
    num = int(input("Enter number " + str(i+1) + ": "))
    nums.append(num)
lcm = nums[0]
gcd = nums[0]
for i in range(1, n):
    lcm = (lcm * nums[i]) // math.gcd(lcm, nums[i])
    gcd = math.gcd(gcd, nums[i])
print("LCM =", lcm)
print("GCD =", gcd)
