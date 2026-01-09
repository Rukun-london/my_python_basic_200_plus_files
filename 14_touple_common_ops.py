
#my_tuple can be various type
my_tuple=()      #empty tuple
my_tuple=(1,2,3)
my_tuple=('cat',[3,4,6],"robin", (3,9,4), 2.6)
my_tuple=3,5,4.6, 'dog'
print(my_tuple)
my_tuple=(3,6,'r','o','a','s','t')
print(my_tuple[-2])
print(my_tuple[1:4])        #slicing elements from 2nd to 4th
print(my_tuple[:-3])        #slicing elements from start to 4th
print(my_tuple[:])
    #tuple elements cannot be changed like lists but if there is a list inside a tuple that can be changed
print(my_tuple+(9,8,7,6))
    #we can not delete elements of tuple but we can delete the whole tuple
result=my_tuple.count(6)
print("result :",result)
