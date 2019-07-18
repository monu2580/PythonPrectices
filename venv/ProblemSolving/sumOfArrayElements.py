arr = [1,2,5,6,47,5,6,2,2]
arrLen = arr.__len__()
sum = 0
for i in range(arr.__len__()):
    element = arr[i]
    sum += element
    #print(arr[i])
print(sum)
