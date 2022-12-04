from collections import Counter
file = open('C:/Users/anumsiddiqui/Downloads/input.txt')
total = 0
n = len(file.readlines())
file.close()
file = open('C:/Users/anumsiddiqui/Downloads/input.txt')
s = Counter()
while n:
    
    for i in range(3):
        fileline = file.readline().replace("\n","")
        fileline = set(fileline)
        s += Counter(fileline)
    for k,v in s.items():
        if v == 3:
            
            if k.islower():
                    val = ord(k)-96
            else:
                val = ord(k)-64+26
            # print(k)
            total+=val
            break
    n = n-3
    s = Counter()

print(total)

#PART 1#
# s = "LHLRlCCvCLVgHPfCHtVjBGrBDNzWFBsBGBfscGsD"
# print(len(s))
# total = 0
# while fileline:

#     n = len(fileline)
#     f = fileline[0:n//2]
#     s = fileline[n//2:]
#     f = set(f)
#     for i in s:
#         if i in f: 
#             if i.islower():
#                 val = ord(i)-96
#             else:
#                 val = ord(i)-64+26
#             print(i, val)
#             total+=val
#             break
#     fileline = file.readline().replace("\n","")

# print(total)
