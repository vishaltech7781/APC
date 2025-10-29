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