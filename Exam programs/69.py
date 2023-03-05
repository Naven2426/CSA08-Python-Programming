import random
A = int(input("Enter A Value: "))
B = int(input("Enter B Value: "))
num_elements = int(input("Enter number of elements: "))
rand_list = [random.randint(A, B) for i in range(num_elements)]
print("Randomized list is:", rand_list)
