# Grocery List Manager

file = open("grocery.txt", "w")

n = int(input("How many grocery items do you want to enter? "))

for i in range(n):
    item = input("Enter grocery item: ")
    file.write(item + "\n")

file.close()

print("Grocery items saved successfully in grocery.txt!")