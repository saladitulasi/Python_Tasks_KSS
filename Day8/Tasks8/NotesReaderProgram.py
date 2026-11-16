# Open the file in read mode
with open("notes.txt", "r") as file:
    # Read all contents
    content = file.read()

    # Display the contents
    print("Daily Notes:")
    print(content)