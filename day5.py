#nested if else
# age = 19
# country = "USA"
# if age > 18:
#     if country == "Nepal":
#         print("eligible for liscence")
#     elif country == "india":
#         print("special liscence for saarc")    
#     else:
#         print("must be nepali")
# else:
#     print("under age")   
    

# gender = "M"

# if gender == "M":
#     print("Male")
# else:
#     print("Female")
    
# data = "Male" if gender == "M" else "Female"    
# print(data)        


#list
# a = [1,2,3,4,5,6,7,8]
# print(a)
# print(type(a))
# print(a[0])
# print(a[-1])
# print(len(a))

#slicing
# a = [1,2,3,4,5,6,7,8]
# print(a[0:3])
# print(a[1:])
# print(a[:6])
# print(a[:])

# data = [1, "test", 4.5, None, 1]
# print(type(data[1]))
# print(isinstance(data[1],str))


data = [1, "test", 4.5, None, 1]
data[0] = "new data"
print(data)

'''
append
insert
extend
concat
'''
data = ["hello", "test", 1, 2, 3, 4, "broadway"]
#append
data.append(1.6)
print(data)

#insert
data.insert(1000, "hari")
print(data)

#extend
a = [1,2,3]
b = [4,5,6]
a.extend(b)
b.extend(a)
print(a)
print(b)

#concat(+)
a = [1,2,3]
b = [2,3,4]
print(a+b)
c = a + b
print(c)