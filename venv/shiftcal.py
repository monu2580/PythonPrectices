#val = input()
#intval = list(map(int,val.split()))
val = [1,2,3,4,5,6]

#shiftinput = input()
#key = int(shiftinput)
key = 8
newval = []

for i in range(val.__len__()):
    i =(i+key)%val.__len__()
    newval.append(val[i])

print(val)
print(key , "Left Shift  ",newval)

newval2 = []

for i in range(val.__len__()):
    i =(i-key)%val.__len__()
    newval2.append(val[i])

print(key , "Right shift  " , newval2)
