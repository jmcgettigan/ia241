"""
Lab 7 - While Loops
"""


#3.2
i = 1
result =1
while i <=5:
    result = result *i
    i = i +1    
print(result)  

#3.3
i = 1
result =0
while i <=5:
    result = result +i
    i = i +1    
print(result) 
    
#3.4
i = 3
result =1
while i <= 8:
    result = result *i
    i = i +1    
print(result) 


#3.5
i = 4
result =1
while i <= 8:
    result = result *i
    i = i +1    
print(result) 

#3.6

num_list =[12,32,43,35]
while num_list:
    print(num_list)
    num_list.remove(num_list[0])
print(num_list)
