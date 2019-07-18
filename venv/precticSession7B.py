class products:
    def __init__(self, pid, name, price,delvAddress):
        self.pid = pid
        self.name = name
        self.price = price
        self.delvAddress = delvAddress

    def __str__(self):
        data = "You have orderd {} Which id is {} . you have to pay {} rupees only , Brand is  {} , model is  {} ".format(self.name,self.pid,self.price,self.brand,self.model )
        return data

    def showProductDetails(self):
        print("-------------------------------------------------------------------------------------")
        print("You have orderd {} Which id is {} . you have to pay {} rupees only".format(self.name,self.pid,self.price))
        dAddr.showAddress()

class mobile(products):
    def __init__(self,pid, name, price,delvAddress,brand, model):
        super().__init__(pid, name, price,delvAddress)
        self.brand= brand
        self.model=model





class fashion(products):
    pass

class grocery(products):
    pass

class delvAddress:
    def __init__(self,hNo,street,pinCode,phone):
        self.hNo = hNo
        self.street = street
        self.pinCode = pinCode
        self.phone = phone

    def showAddress(self):
        print("Product delivery Address is : House no :- {}, Street Name :- {} , Pincode :- {}, mobile no. :- {}".format(self.hNo,self.street,self.pinCode,self.phone))

dAddr = delvAddress(1256,"Dugri",141013,9542316780)

f1 = fashion(101,"shirt",1200,dAddr)
g1 = grocery(201,"Rice",5620,dAddr)
m1 = mobile(202,"mobile",5620,dAddr,"Nokia",3310)
g1.showProductDetails()
f1.showProductDetails()
print(m1)
# c1 = mcDonaldsMeal("Burger",190,"veg")
# c1.showMealDetails()

