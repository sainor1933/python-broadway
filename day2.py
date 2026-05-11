# a = 10
# b = "ok"
# c = True
# d = None
# e = 1.2
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

a = "2"
print("before type casting" , type(a) , a)

b = float(a)
print("after type casting", type(b) , b)

print(isinstance(b,float))