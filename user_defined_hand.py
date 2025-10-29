class AgeTooLowError(Exception):
    pass

def register_user(age):
    if age < 18:
        raise AgeTooLowError("Age must be at least 18 to register.")
    else:
        print(" Registration successful!")

try:
    age = int(input("Enter your age: "))
    register_user(age)
except AgeTooLowError as e:
    print(" Custom Exception Caught:", e)
finally:
    print("End of program.")
