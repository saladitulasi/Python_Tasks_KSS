import time

def calculate_time(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print("Execution Time:", end - start, "seconds")

    return wrapper


@calculate_time
def display():
    time.sleep(2)
    print("Function Executed Successfully")


display()