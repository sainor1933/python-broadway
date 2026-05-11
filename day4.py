#if condition
# if(2==1):
#     print("ok it is true")
# else:
#     print("its not true")
    
# age = 13
# if(age >= 18):
#     print("you can vote")
# else:
#     print("you cannot vote")        
    
# GPA = 2
# if GPA > 4 or GPA < 0:
#     print("invalid GPA")
# elif GPA >= 3.6:
#     print("A+")
# elif GPA >= 2.6:
#     print("B+")
# else:
#     print("fail")
    
GPA = 2
if GPA > 4 or GPA < 0:
    print("invalid GPA")
elif GPA >= 2.6 and GPA <= 3.6:
    print("B+")    
elif GPA >= 3.6 and GPA <= 4.0:
    print("A+")
else:
    print("fail")
             