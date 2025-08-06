list= []
list1= ["lion","tiger","cheetah"]
n = int(input("how many elements u want to append?"))

for i in range(0,n):
    items = input(f"enter the element no{i}:")
    list.append(items)

print(list)
var1 = input("enter the item to be insterted:")
list.insert(2,var1)
print(list)
list1.remove("tiger")
print(list1)
list.pop()
print(list)
list.reverse()
print(list)
copy_list = list.copy()
print(copy_list)
list_2 = ["appple","banana"]
list.extend(list_2)
print(list)
list.index("biradar")
list_3 = [1,5,8,3,4,7]
print(list_3.sort())