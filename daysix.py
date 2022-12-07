with open('C:/Users/anumsiddiqui/Downloads/input.txt') as f:
    string = f.read()

# print(string)
n = len(string);k=4

def distinctcharacters(k,string):
    i=0;j=0; myset = set()

    while j<n:
        

        if string[j] not in myset and j-i+1 <k:
            myset.add(string[j])
            j+=1
            # print(myset)
        elif len(myset)!=0 and string[j] in myset and j-i+1 <= k:
            while string[j] in myset and i!=j:
                # print(myset,string[i])
                myset.remove(string[i])
                i+=1
                # print(i,j)
                # print(myset,string[i])
                
            if j-i <1: j+=1
            # myset.add(string[j])
            if string[i] not in myset: myset.add(string[i])

        elif j-i+1 == k:
            print(j+1)
            break
distinctcharacters(14,string)

# print(string[1097:1101])
# print(string[2421-14:2422])
    
        