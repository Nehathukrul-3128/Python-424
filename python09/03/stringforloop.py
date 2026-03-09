#methods-count,find,replace,join,index,split,splitline

#iterate string
name="ITvedant"
# for i in name:
#     print(i)

# #reverse string 
# # print("reverse string:",name[::-1])

# newstr=""
# for i in name:
#     newstr=i+newstr

# print(newstr)

#WAP newstring without vowels
# withoutvowels_str=""
# for i in name:
#     if i not in "aeiouAEIOU":
#         withoutvowels_str=withoutvowels_str+i

# print(withoutvowels_str)

#WAP to print no of occurances of entered character from any string

# str=input("enter string=")
# char=input("enter character=")
# count=0
# for i in str:
#     if char==i:
#         count+=1

# print(f"{char} character count into {str} is {count}")

#WAP to print number of occurances of entered 
# character or word from any string

# str=input("enter string=")
# chkstr=input("enter char/word to find and show count=")
# count=0
# check=""
# for i in range(len(str)):
#     # print(i,str[i])
#     k=i
#     for j in range(len(chkstr)):
#         try:
#             check+=str[k]
#             k+=1
#         except:
#             None
#     if check==chkstr:
#         count+=1
#     check=""
# if count!=0:
#     print(f"{chkstr} found in {str} and count={count}")
# else:
#     print(f"{chkstr} not found in {str}")

