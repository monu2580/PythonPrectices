class McDonaldsMeal:
    def __init__(self,name,price,types, description):
        self.name = name
        self.price = price
        self.types = types
        self.description = description

    def showMeal(self):

        print("Types of Meal {} , "
              "Nmae of Meal {} ,"
              "price of meal {} , "
              "About Meal {} , ".format(self.types, self.name, self.price, self.description))
#****************************************
        #Breakfast
#****************************************
class breakFast(McDonaldsMeal):
    pass

b1=breakFast("Friut and maple Oatmeal",180,"breakFast","________________")
b1=breakFast("Egg McMuttin",160,"breakFast","________________")
b1=breakFast("HotCake",120,"breakFast","________________")

b1.showMeal()

#****************************************
        #HappyMeal
#****************************************
class happyMeal(McDonaldsMeal):
    pass
h1=happyMeal("humBurgar",200,"happyMeal","________________")
h1=happyMeal("chickenMcmugets",200,"happyMeal","________________")
h1=happyMeal("appleSlices",200,"happyMeal","________________")
h1=happyMeal("organicJuiceDrink",200,"happyMeal","________________")


h1.showMeal()

#****************************************
        #Burgar
#****************************************
class burgars(McDonaldsMeal):
    pass
bgr1 = burgars("bigBUrger",160,"Burger","________________")
bgr1 = burgars("Cheese BUrger",160,"Burger","________________")
bgr1 = burgars("Double Cheese BUrger",160,"Burger","________________")
bgr1 = burgars("Triple Cheese BUrgerr",160,"Burger","________________")

bgr1.showMeal()
#****************************************
        #Drink
#****************************************
class drinks(McDonaldsMeal):
    pass
d1 = drinks("coca_cola",190,"drinks","________________")
d2 = drinks("Sprite",190,"drinks","")
d3 = drinks("chocolate shake",190,"drinks","________________")
d4 = drinks("Orange juice",190,"drinks","________________")
d5 = drinks("tea",190,"drinks","________________")
d6 = drinks("coffee",190,"drinks","________________")

d1.showMeal()

list1  = []
list1.append(d1)
list1.append(d2)
for i in range(list1.__len__()):
    for j in range(len(list1[ij)):
        print(list1[j])