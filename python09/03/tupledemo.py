#tuple->collecting different data elements enclosed into () paranthesis
#it is seperated,index,follow,referred immutable mans can't do curd operation

#create tuple
tup=()
print(tup,type(tup))
t1=tuple()
print(t1,type(t1))

t2=(500)
print(t2,type(t1))

t3=(500,100,"hello",True,5j,89.968795)
print(t3,type(t3))

# t4=tuple(78,89,90) #error
t4=tuple((78,89,90))
print(t4,type(t4))

my_tuple=(3,45,64,6764,34,100)
print(my_tuple)

#index
print("first element=",my_tuple[0])
print("last element=",my_tuple[-1])

#sclicing
print(my_tuple[::-1])
print(my_tuple[2:5])

#operation
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2)
# print(tuple1+100) # type error: can only concentrate tuple(noy 'int') to tuple

#tuple function 
tuple3=(1,4,5,2,3)
print(tuple3)
print(sorted(tuple3))
print(sorted(tuple3)[::-1])
print(sorted(tuple3,reverse=True))

#tuple method-index(),count()
tuple4=("hello","red","orange","green",1000,300,700)
# print(tuple4.index(3)) #if element not present than valueerror
print(tuple4.count(300))#1
print(tuple4.index(300))#5

#immutability
#tuple4[0]="welcome" # typeerror:"tuple" object does not support item assignment
print(tuple4)

#travesing of tuple
my_tup=(100,200,300,400,1,2,3)
for i in my_tup:
    print(i)

#reverse
for i in my_tup[::-1]:
    print(i)
    
#ascending
for i in sorted(my_tup):
    print(i)

#descending
for i in sorted(my_tup)[::-1]:
    print(i)

    