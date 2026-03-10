# list->collecting different data elements enclosed into []
#it is seperated,index,follow,referred immutable means can do curd operation

#create list
list1=[]
print(list1,type(list1))
list2=[100]
print(list2,type(list2))
list3=["hello",100,True,100j,None,(100,200)]
print(list3,type(list3))

#index
print(list[0])
print(list[-1])

#imutable
list3[-1]=55555
print(list)