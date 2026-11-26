# Create sample log file
with open("logfile.txt", "w") as file:
    file.write("INFO: System started\n")
    file.write("ERROR: File not found\n")
    file.write("INFO: User logged in\n")
    file.write("ERROR: Database failed\n")
    file.write("WARNING: Low memory\n")
    file.write("ERROR: File not found\n")

# Generator to read file line by line
def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

# Dictionary to count errors
error_count = {}

try:
    # Process logs
    for log in read_logs("logfile.txt"):

        if "ERROR" in log:
            print("Error Found:", log)

            error_type = log.split(":", 1)[1].strip()

            if error_type in error_count:
                error_count[error_type] += 1
            else:
                error_count[error_type] = 1

    print("\nError Summary:")

    for error, count in error_count.items():
        print(error, ":", count)

except FileNotFoundError:
    print("Log file not found!")

except Exception as e:
    print("Error:", e)