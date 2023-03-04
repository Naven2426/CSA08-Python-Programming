def calculate_bonus(salary, grade):
    if salary < 10000:
        bonus_percent = 0.12  
    elif grade == "A":
        bonus_percent = 0.05
    elif grade == "B":
        bonus_percent = 0.1
    else:
        bonus_percent = 0
    bonus = salary * bonus_percent
    total_salary = salary + bonus
    return bonus, total_salary
salary = float(input("Enter the employee's salary: "))
grade = input("Enter the employee's grade (A/B): ")
bonus, total_salary = calculate_bonus(salary, grade)
print(f"The bonus for this employee is: ${bonus:.2f}")
print(f"The total salary for this employee is: ${total_salary:.2f}")
