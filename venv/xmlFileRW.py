with open("C:/Users/Deepesh/Dropbox/Python/proj/venv/employees.xml","r") as file:

    #data = file.readline()
    #file.seek(89)
    #file.seek(108) #+19
    #file.seek(133) #+25

    #file.seek(183)  @+50
    #file.seek(202)
   # file.seek(227)

    #file.seek(56)
    #file.seek(161)

    #file.seek(164)
    file.seek(258)


    data = file.readlines(74)
    #print(len(data))
    for l in data:
        print(l)
