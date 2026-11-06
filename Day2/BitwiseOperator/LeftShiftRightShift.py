a = int(input("Enter a number: "))
n = int(input("Enter shift positions: "))
left = a << n
right = a >> n
print("Left Shift =", left)
print("Right Shift =", right)