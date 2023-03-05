num = input("Enter the number: ")
choice = input("Enter your choice (A/D/B): ")
digits = list(num)
if choice == 'A':
    digits.sort()
    print("Ascending order =", ' '.join(digits))
elif choice == 'D':
    digits.sort(reverse=True)
    print("Descending order =", ' '.join(digits))
elif choice == 'B':
    digits.sort()
    print("Ascending order =", ' '.join(digits))
    digits.sort(reverse=True)
    print("Descending order =", ' '.join(digits))
else:
    print("Invalid choice! Please enter either A or D or B.")
