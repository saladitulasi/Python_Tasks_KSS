def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func(is_logged_in)
        else:
            print("Access Denied! Please Login First.")
    return wrapper


@login_required
def dashboard(is_logged_in):
    print("Welcome to the Dashboard!")


dashboard(True)
dashboard(False)