with open("C:/Users/Deepesh/Dropbox/Python/proj/venv/employees.xml","r") as file:

    #sk = file.seek(89)
    #data = file.readlines()
    data = file.readlines()
    # print(len(data))
    # eid = ""
    # for l in data:
    #     eid += l
    # print(eid)

    for i in data:
        wd = i.split()
        print(wd)
