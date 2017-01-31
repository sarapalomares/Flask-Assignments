#create a class called Car
class Car(object):
    def __init__ (self, price, speed, fuel, mileage):
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.mileage) + 'mpg'
        print 'Tax: ' + str(self.tax)

#create six different instances of Car
car1 = Car(2000,85,'Half',20)
car2 = Car(3000,70,'Full',15)
car3 = Car(4000,75,'Almost empty',25)
car4 = Car(5000,90,'Empty',20)
car5 = Car(6000,80,'3/4',20)
car6 = Car(20000,95,'Full',35)
