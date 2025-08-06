list= []

n = int(input("how many elements u want to append?"))

for i in range(0,n):
    items = input(f"enter the elements no.{i}:")
    list.append(items)

print(list)