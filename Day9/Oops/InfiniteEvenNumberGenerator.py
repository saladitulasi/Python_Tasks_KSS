def even_numbers():
    num = 2

    while True:
        yield num
        num += 2


N = int(input("Enter how many even numbers: "))

gen = even_numbers()

print("Even Numbers:")

for i in range(N):
    print(next(gen))