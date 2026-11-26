import numpy as np
import pandas as pd
import time

# Decorator to measure execution time
def calculate_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("\nExecution Time:", end - start, "seconds")

        return result

    return wrapper


# Generator to read numbers from file
def read_numbers(filename):

    with open(filename, "r") as file:

        for line in file:
            try:
                number = float(line.strip())
                yield number

            except ValueError:
                print("Invalid data skipped:", line.strip())


# Data processing function
@calculate_time
def process_data():

    try:
        # Read numbers using generator
        numbers = list(read_numbers("numbers.txt"))

        if len(numbers) == 0:
            print("No valid numbers found!")
            return

        # Convert into NumPy array
        arr = np.array(numbers)

        # Calculate statistics
        mean = np.mean(arr)
        std = np.std(arr)

        # Convert results into DataFrame
        data = pd.DataFrame({
            "Statistic": ["Mean", "Standard Deviation"],
            "Value": [mean, std]
        })

        print("\nOriginal Numbers:", arr)

        print("\nData Analysis:")
        print(data)

        # Save results
        data.to_csv("results.csv", index=False)

        print("\nResults saved successfully!")

    except FileNotFoundError:
        print("Numbers file not found!")

    except Exception as e:
        print("Error:", e)


# Create input file
with open("numbers.txt", "w") as file:
    file.write("10\n20\n30\n40\n50\nabc\n60\n")

# Execute pipeline
process_data()