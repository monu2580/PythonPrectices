def starPattern(n):
    #Right angle Trangle
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")

    #Left Angle Trangle
    k=2*n-2
    for p in range(0,n):
        for q in range(0,k):
            print(end=" ")
        k=k-2
        for q in range(0, p+1):
            print("*", end=" ")
        print("\r")

    #Piramide
    c= 2*n-2
    for d in range(0,n):
        for e in range(0,c):
            print(end=" ")
        c = c-1
        for  e in range(0,d+1):
            print("*", end=" ")
        print("\r")

    #Print No. T-B in RAT Shape
    for f in range(0,n):
        for g in range(0,f+1):
            print(f," ",end=" ") #g # for L-R
        print("\r")

    #Piramide with L-R no.
    l =2*n-2
    for o in range(0,n):
        for m in range(0,l):
            print(end=" ")
        l=l-1
        for m in range(0,o+1):
            print(m,end=" ")
        print("\r")

    #Print No. in RightAngleTrangle Without reapting no.
    num = 1
    for r in range(0,n):
        for s in range(0,r+1):
            print(num, end=" ")
            num=num+1
        print("\r")

    chIndex = 65
    for u in range(0,n):
        for v in range(0,u+1):
            ch=chr(chIndex)
            print(ch,end=" ")
            #chIndex=chIndex+1 #Print Alphabate without repeation
            if chIndex>90:
                chIndex=65
            else:
                chIndex=chIndex
        chIndex = chIndex + 1  # Print Alphabate with repeation
        print("\r")


starPattern(10)