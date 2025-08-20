info={
    "Age":23,
    "Subjects":["Maths","English","Hindi","Marathi"],
    "Name":"Prajval"
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