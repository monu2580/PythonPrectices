def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))

names = ["John","Jennie","Jack"]
ages = [10,20,30]
fun(age=20,name="John",address="Redwood Shores")
fun(allnames = names, allages = ages)
