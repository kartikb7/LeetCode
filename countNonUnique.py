
numbers = [1,2,3,1,2,3,4,5,7,5]
testDict = {}

for n in numbers:
    if n in testDict:
        testDict[n]+=1
    else:
        testDict[n]=1
count = 0

for v in testDict.keys():
    if testDict[v]>1:
        count+=1

return count