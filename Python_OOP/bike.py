#Create a new class called Bike
class Bike(object):
    def __init__ (self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

#Create 3 instances of the Bike class
def displayInfo(self):
    print 'Price: $' + str(self.price)
    print 'Max Speed: ' + str(self.max_speed) + 'mph'
    print 'Total Miles: ' + str(self.miles) + 'miles'

def ride(self):
    print 'Riding'
    self.miles +=10

def reverse(self):
    print 'Reversing'
    if self.miles >= 5:
        self.miles -=5

#Running code
bike1 = Bike(99.99, 12)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(139.99, 20)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
