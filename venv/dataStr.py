class Emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def __str__(self):
        msg="id is {}  ,  Name is  {}  , Salary is {}".format(self.id,self.name,self.salary)
        return  msg

e1 = Emp(102,"john",10000)
e2 = Emp(103,"herry",20000)
e3 = Emp(104,"mac",30000)

#empList = [e1,e2,e3]
empList = []
empList.append(e1)
empList.append(e2)
empList.append(e3)

#****************************
        #Sorting
# for e in empList:
#     for s in sorted(e.name):
#         pass
#     print(e)
# ****************************
#empList.sort()
for e in empList:
    print("Enter salary of  {}".format(e. name))
    sal =input()
    e.salary=int(sal)
    for s in sorted(e.name):
        pass
    print(e)
    # for  s in range(len(e)):
    #     print(s)