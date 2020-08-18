number=[1,2,6,5,3,8,9]
print(number)
#2D list 
matrix=[
    [1,2,3] ,
    [4,5,6] ,
    [7,8,9]

]
#print 2 
print(matrix[0][1])
#list methods 
number.append(20) #add 20 in the last index
number.insert(0,9) # in index 0 will add 9 
number.remove(5) # delete 5  
number.pop() # delete last index
print(number.index(5))
print(number.count(7)) # counts of 7 
number.sort()
number.reverse()
number2= number.copy()
print(3 in number)
number.clear()  #delete all 


