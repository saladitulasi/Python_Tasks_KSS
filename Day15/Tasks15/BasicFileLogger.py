try:
    while True:
        print("\n1. Add Log")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            log = input("Enter user action: ")

            with open("log.txt", "a") as file:
                file.write(log + "\n")

            print("Log saved successfully!")

        elif choice == "2":
            print("Exiting Logger...")
            break

        else:
            print("Invalid choice!")

except FileNotFoundError:
    print("File not found!")

except PermissionError:
    print("Permission denied!")

except Exception as e:
    print("Error:", e)