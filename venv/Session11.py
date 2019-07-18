class Emp:
    def __init__(self,id,name,salary):
        self.id= id
        self.name= name
        self.salary=salary

    def showEmp(self):
        data1 = "id is {}, name is {}, salary is {}".format(self.id,self.name,self.salary)
        return data1
    def getEmp(self):
        data1 = "id is {}, name is {}, salary is {}".format(self.id,self.name,self.salary)
        return data1

e1 = Emp(506,"Deepesh",25000)
e2 = Emp(507,"Rahul",53000)
e3 = Emp(508,"jivesh",45000)
e1.showEmp()
e2.showEmp()
e3.showEmp()


file = open("AbcWrite.txt","a")
data = e1.getEmp()
file.write(data)
file.close()