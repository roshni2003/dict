dict1={"name":"Roshni","age":18}
key=input("enter a key to check")
if key in dict1.keys():
    print("exist")
    print(dict1[key])
else:
    print("not exist")