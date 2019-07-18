class Emp:
    def __init__(self,id,name,salary):
        self.id= id
        self.name= name
        self.salary=salary
    def __str__(self):
        data = "id is {}, name is {}, salary is {}".format(self.id,self.name,self.salary)
        return  data

# e1 = Emp(506,"Deepesh",25000)
# print(e1)
