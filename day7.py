#python dict
data = {
    "name":"sabin",
    "age":"23",
    "address":"dang",
    "phone":[9856354353],
    "percentage":"76.23%"
}

# print(data)
# print(type(data))
# print(len(data))
# print(data.keys())
# print(data.values())
# print(data["age"])

#update or addd method1
# data["age"]=32
# data["percentage"]=79.43
# data["temp_num"]=12434

# print(data)

# #method2
# data.update({
#     "age":"23",
#     "name":"sabin",
#     "thau":"lamahi"
# })
# print(data)

# #del
# del data["name"]
# print(data)

# #pop-> arguement needs to be passed and can remove any item acc to key
# data.pop("age")
# print(data)

# #popitem-> only remove last item, arguement cannot be passed
# data.popitem()
# print(data)

# #clear
# data.clear()
# print(data)

data = {
    "name": "hari",
    "address": "nepal",
    "age": 1,
    "phone": [
        {
            "type":"ntc",
            "num":9855
        },
        {
            "type":"ncell",
            "num":980
        },
    ],
    "percentage": 100,
    "temp_num": 1,
}

# a = (data["name"])
# b = (data["phone"][0]["type"])
# c = (data["phone"][0]["num"])

# d = (data["name"])
# e = (data["phone"][1]["type"])
# f = (data["phone"][1]["num"])



# print(a,b,"num","is",c)
# print(d,e,"num","is",f)

#f string
print(f"{data['name']} {data['phone'][0]['type']} number is {data['phone'][0]['num']} ")
print(f"{data['name']} {data['phone'][1]['type']} number is {data['phone'][1]['num']} ")
