class Order:
    def __init__(self,pName,pId,pPrice,orderDeliveryAddress):
        self.pName=pName
        self.pId=pId
        self.pPrice=pPrice
        self.orderDeliveryAddress=orderDeliveryAddress

    def showOrder(self):
        print("you have orderd a {} its product id is {} and price is {}      {}".format(self.pName, self.pId,self.pPrice,self.orderDeliveryAddress))


class orderDeliveryAddress:
    def __init__(self,h_no, streetName, personName, phone, pin):
        self.h_no=h_no
        self.streetName=streetName
        self.perrsonName=personName
        self.phone=phone
        self.pin=pin

    def showDelvrAddress(self):
        print("this order should be delever at this Address"
              "Customer Name = {}"
              "House no. = {}"
              "Street Name = {}"
              "mobile no. = {}"
              "pin code is = {}")
da1=orderDeliveryAddress(4368 , "Dugri","Deepesh" , 9803475225 , 153246 )
o1=Order("pen","BGD758G8",200,orderDeliveryAddress)
o1.showOrder()


