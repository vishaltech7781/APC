# *     1
# **    12
# ***   123
# ****  1234
# ***** 12345

n = int(input("enter the number :"))

def pattern(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()

pattern(n)

# ***** 12345
# ****  1234
# ***   123
# **    12
# *     1
n = int(input("enter the number :"))

def pattern(n):
    for i in range(n):
        for j in range(i,n):
            print(j,end="")
        print()

pattern(n)