'''
a = "Salam"
dict = {
    "a":"b",
    "c":"d"
}
t=(1,2,3)

print(len(t),len(dict),len(a))
'''


class Car:
    def a(self):
        pass

class Car1(Car):
    def a(self):
        return "Good"
    
class Car2(Car):
    def a(self):
        return "Not Good"

cars = [Car1(), Car2()]
for x in cars:
    print(x.a())