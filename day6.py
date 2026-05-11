'''
del
remove
pop
clear
'''
# #del
# a = [1,2,3,4,5]
# del a[0]
# print(a)

# #remove
# a =  [1,2,3,4,5,1,1]
# a.remove(5)
# a.remove(1)
# a.remove(1)
# print(a)


# #pop
# a =  [1,2,3,4,5]
# a.pop()
# result = a.pop(0)
# print(a)
# print(result)

# #clear
# a =  [1,2,3,4,5]
# a.clear()
# print(a)

'''
sort()
reverse()
count()
'''
# #sort
# a = [1,5,8,4,66,76,5]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# #reverse
# a = [1,5,8,4,66,76,5]
# a.reverse()
# print(a)

# #count
# a = [1,5,8,4,66,76,5]
# print(a.count(5))

#nested List
# a = [1,2,3,4,[6,7,8]]
# print(a[-1][1])
# print(type(a))

'''
5 inputs for user all in int
add 5 input data in list
find the average of all items number
'''
b = []
a = int(input("Enter a number: "))
b.append(a)

c = int(input("Enter a number: "))
b.append(c)

d = int(input("Enter a number: "))
b.append(d)

e = int(input("Enter a number: "))
b.append(e)

f = int(input("Enter a number: "))
b.append(f)

Average = (b[0]+b[1]+b[2]+b[3]+b[4])/len(b)
print(Average)
