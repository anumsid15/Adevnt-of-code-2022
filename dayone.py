import heapq
file = open('C:/Users/anumsiddiqui/Downloads/input.txt')
fileline = file.readline()
print(fileline)
heap = []
heapq.heapify(heap)
tempSum = 0; maxSumm = 0
while fileline:
    
    if fileline != "\n":
        tempSum += int(fileline)
    
    fileline = file.readline()
    # print(fileline)
    
    if fileline == "\n":
        maxSumm = max(maxSumm,tempSum)
        # print(tempSum)
        
        if len(heap) < 3:
            heapq.heappush(heap,tempSum)
        else:
            heapq.heappushpop(heap,tempSum)
        tempSum = 0
        
        
print(maxSumm)        
print(heap)
print(sum(heap))