# Student Marks File Analyzer

file = open("marks.txt", "r")

total = 0
count = 0

print("Student Records:")
print("----------------")

for line in file:
    name, marks = line.split()
    marks = int(marks)

    print(name, marks)

    total = total + marks
    count = count + 1

file.close()

if count > 0:
    average = total / count
    print("----------------")
    print("Average Marks:", average)
else:
    print("No student records found.")