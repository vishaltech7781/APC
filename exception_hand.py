list = ["maruti","audi","rolls_royce","pagani"]
x = int(input("enter the index for acccesing the items from the list: "))
try:
    print(f"the {x} brand is :",list[x])
   

except IndexError as ex:
    print("index entered is,",ex)

else:
    print ("enter the correct index for accesing the itmes correctly.")

finally:
    print("end of the program...")


# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a / b)
# except ZeroDivisionError:
#     print("Error: You can’t divide by zero!")
# except ValueError:
#     print("Error: Please enter only numbers!")
# except Exception as e:
#     print("Unknown Error:", e)


# try:
#     n = int(input("Enter a number: "))
#     print("Square:", n**2)
# except ValueError:
#     print("Invalid input! Please enter a number.")
# else:
#     print("No error occurred.")
# finally:
#     print("Execution completed.")
