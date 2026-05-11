# a = [1,2,3,4,5,6,7,8]
# #in , not in
# print(5 in a)

# #for loop
# for i in [1,2,3,4,5,6,7,8]:
#     print(i)
    
# data = {
#     "name":"sabin",
#     "age":"23",
#     "thau":"lamahi"
# }    
    
# for j in  data:
#     print(f"{j} = {data[j]}")
    
# print(data.items())
# for key, value in data.items():
#     print(key,value)   
    
# items = ["apple", "orange", "banana", "coconut"]
# for index , data in enumerate(items):
#     print(index , data)
    
# #range 1st is
# for i in range(1,20,1):
#     print(i)
    
# print("----------------*2")
# for i in range(20,1,-1):
#     print(i)
    

# for i in range(1,20,1):
#     if i % 2 == 0:
#         print(i)
        
# even = []
# odd = []
# for i in range(1,20,1):
#     if i%2 ==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)
    
for i in range(1,10,1):
    if i == 5:
        break
    print(i)



for i in range(1,10,1):
    if i == 5:
        continue
    print(i)