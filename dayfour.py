file = open('C:/Users/anumsiddiqui/Downloads/input.txt')
fileline = file.readline().replace("\n","").split(',')
total = 0

while fileline:

    f = fileline[0].split('-')
    s = fileline[1].split('-')
    f[0] = int(f[0])
    f[1] = int(f[1])
    s[0] = int(s[0])
    s[1] = int(s[1])

    if abs(int(f[0])-int(f[1])) >= abs(int(s[0])-int(s[1])):
        if f[0]<=s[0]<=f[1] or f[0]<=s[1]<=f[1]: total+=1
    else:
        if s[0]<=f[0]<=s[1] or s[0]<=f[1]<=s[1]: total+=1

    fileline = file.readline().replace("\n","").split(',')
    if fileline[0] == '': break
    # print(fileline)

print(total)
