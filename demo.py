# demo.py
'''
print("hello vs code")

strc="""다중111
문자열은 
이렇게 저장"""

print(len(strc))


# list of cars
my_cars = ["Ford", "Audi", "BMW"]

# sort the cars in Alphabetical Order
my_cars.sort()

# unpack cars into different variables
a, b, c = my_cars

print("Car", a)
print("Car", b)
print("Car", c)

'''
def intersect(prelist, postlist):
    result =[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("HAM", "SPAM"))
        