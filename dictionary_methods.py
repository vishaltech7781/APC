info={
    "Age":21,
    "Subjects":["Maths","English","Marathi"],
    "Name":"vishal"
}

print(info)

#Get value
print(info.get("Subjects"))
print(info["Name"])

#keys
print(info.keys())

#values
print(info.values())

#update
info.update({"Age":26})
print(info)

info["Name"]="Prathamesh"
print(info)