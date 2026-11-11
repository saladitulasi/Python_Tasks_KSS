employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# 1. Employee with highest salary
highest = max(employees, key=lambda x: x["salary"])

print("Highest salary employee:", highest)

# 2. Employees with salary greater than 35000
filtered = []

for emp in employees:
    if emp["salary"] > 35000:
        filtered.append(emp)

print("\nEmployees with salary > 35000:")

for emp in filtered:
    print(emp)

# 3. Calculate average salary
total_salary = sum(emp["salary"] for emp in employees)

average = total_salary / len(employees)

print("\nAverage salary:", average)

# 4. List containing only employee names
names = [emp["name"] for emp in employees]

print("\nEmployee names:", names)