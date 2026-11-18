def number_generator(N):
    for i in range(1, N + 1):
        yield i

N = int(input("Enter the value of N: "))

print("Generated Numbers:")
for num in number_generator(N):
    print(num)