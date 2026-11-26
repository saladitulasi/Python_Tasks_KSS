# Store user roles in dictionary
users = {
    "admin": "admin",
    "teacher": "teacher",
    "student": "student"
}

# Decorator to check user role
def check_role(required_role):

    def decorator(func):

        def wrapper(username):

            if username in users:
                if users[username] == required_role:
                    print("Access Granted!")
                    return func(username)
                else:
                    print("Access Denied! Insufficient role.")
            else:
                print("User not found!")

        return wrapper

    return decorator


# Admin function
@check_role("admin")
def delete_records(username):
    print(username, "can delete records.")


# Teacher function
@check_role("teacher")
def add_marks(username):
    print(username, "can add marks.")


# Student function
@check_role("student")
def view_marks(username):
    print(username, "can view marks.")


# Test functions
delete_records("admin")
print()

add_marks("student")
print()

view_marks("student")
print()

add_marks("teacher")