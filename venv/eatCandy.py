import sys
candy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
m = 5
ateCandy = []
index = 0
while True:
    if candy[index] in ateCandy:
        break
    else:
        ateCandy.append(candy[index])
    index = (index + m)%candy.__len__()

print(ateCandy)
