file = open('C:/Users/anumsiddiqui/Downloads/basicinput.txt')
fileline = file.readline().split()
# print(fileline[1])
score = 0
total = 0
A =1; B=2;C=3

while fileline:

    if fileline[1]=='X': 
        score+=0
        if fileline[0] == 'A':
            score+=C
        elif fileline[0] == 'B':
            score+=A
        elif fileline[0] == 'C':
            score+=B

    elif fileline[1]=='Y':
        score+=3
        if fileline[0]=='A': score+=A
        elif fileline[0]=='B': score+=B
        elif fileline[0]=='C': score+=C

    elif fileline[1]=='Z':
        score+=6
        if fileline[0] == 'A':
            score+=B
        elif fileline[0] == 'B':
            score+=C
        elif fileline[0] == 'C':
            score+=A

    total+=score
    score=0
    fileline=file.readline().split()
print(total)