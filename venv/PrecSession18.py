# emp =[{"id":120,"name":"Deepesh"},{"id":121,"name":"Deepak"},{"id":122,"name":"Deepesh"},{"id":123,"name":"Deepak"}]
# #lmd1 = lambda dic : dic["id"]
# lmd1 = lambda dic : dic["id"] == 201
# result = map(lmd1,emp)
#
# print(list(result))
#
# filterResult = filter(lmd1,emp)
# print(list(filterResult))

def show1():
    return "A"
    return "B"
    return "C"
def show():
    yield "A"
    yield "B"
    yield "C"
    yield "D"

s1=show1()

# print(next(s1))
# print(next(s1))
# print(next(s1))

print(s1)
print(s1)
print(s1)