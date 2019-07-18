print("Enter your String")
str1 = input()
#to get List input
liststr = list(map(str,str1.split()))

#liststr = ["anam","pfn","jkro","xwnd","qiokr","xofj"]

#str = input()
#newstr = str.split()



#print(liststr)
#liststr.sort()
#print(liststr)

xlist = []
for i in sorted(liststr):
    if i[0]=="x":
        xlist.append(i)
        liststr.remove(i)

#print(xlist)
#print(liststr)
print(xlist + liststr)
print("")
print("")
