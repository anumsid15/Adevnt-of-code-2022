# file = open('C:/Users/anumsiddiqui/Downloads/input.txt')
# import re 
# fileline = file.readline().replace("\n","")
# c= len(fileline)
# i = 0
# cnt = 0
# mystack = [[]]*9
# print(c)
# col = 1
# while fileline:

#     if fileline[0] == 'm': break
#     col +=1
#     while i<c:
#         print(fileline[i:i+4],cnt)
#         mystack.append([fileline[i:i+4].replace(" ","")])
#         print(mystack)
#         i+=4
#         cnt+=1
#         print(i,c)
#     i = 0
#     print("new filline")
#     fileline = file.readline().replace("\n","")
# print(col-2)
# del(mystack[-9:])
# print(mystack)



# # myregex  = re.compile(r'\[\w\]')
# # objsearch = myregex.search(fileline)
# # print(objsearch.group())


