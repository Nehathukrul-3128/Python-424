#set->issuperset(),issubset(),isdisjoin(),union(),difference(),symmetric_difference()

# x={6,89,45,34,90,}
# print(x)

# #add elements
# # print([-1]) 
# x.add(100)
# print(x)
# x.add(50)
# print(x)

# #x.add(11,12)#type-error: set-add(),takes exactly one arguement
# # x.add([11,12])#typeerror: un hashable type:list
# #x.add([11],[12])#Error
# x.add((11,12))
# print(x)
# y={1,2}
# x.update(y)
# print(x)


# colors={"red","green","pink","orange"}
# print(colors)
# colors_new=list(colors)
# print(colors_new)#['orange', 'pink', 'red', 'green']
# i=colors_new.index("red")
# colors_new[i]="Magenta"
# print(colors_new)#['orange', 'pink', 'Magenta', 'green']
# colors_new1=set(colors_new)
# print(colors_new1)#{'Magenta', 'orange', 'pink', 'green'}



#WAp to show give unique elements from below given list
# mylist=[12,12,45,23,76,45,1,1,1]
# print(mylist)
# # new_list=list(set(mylist))
# #print(new_list)

# new_mylist={}
# for i in mylist:
#     if i not in new_mylist:
#         new_mylist.append(i)

# print(new_mylist)

#WAP to create mylist and add number element as entered count
# myset=set()
# print(myset,type(myset))
# count=int(input("enter count for numbers="))
# for i in range(count):
#     number=int(input(f"enter {i+1} number="))
#     myset.add(number)
# print(myset)


#WAP to print 10to 1 in set using comprehension 
# print({i for i in range(10,1,-1)})#{1,2,3.... can't follow set}
# print([i for i in range(10,0,-1)]) #[10,9,8,7,6,5,4,3,2,1]

x={12,-324,56,343,-5,35}
#WAP to show only +ve numbers from above set use comprehension 
print({i for i in x if i>0})

#WAP to show sum of elements of below list
mylist=[12,3,4,5,11]
sum=0
for i in mylist:
    sum+=1
print(sum)

#WAP to show cube of above elements 
print(i**3 for i in mylist)


i=10
while i>=1:
    print(i)
    i+=1