import random

class Apartament:
    def __init__(self, addres, area, price):
        self.status = 'Available'
        self.CanWrite = True
        self.addres = addres
        self.area = area
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value >= 1000 and self.status == 'Available':
             self._price = value
        else:
            raise ValueError
    @property
    def area(self):
        return self._area
    @area.setter
    def area(self, meters):
        if meters > 0:
            self._area = meters
        else:
            raise ValueError
    @property 
    def addres(self):
        return self._addres
    @addres.setter
    def addres(self, name):
        name = name.replace(' ', '')
        if len(name) >= 10 and self.CanWrite != False:
            self._addres = name
            self.CanWrite = False
        else:
            raise ValueError
    @property
    def PerMeterPrice(self):
        PerMeter = round(self.price / self.area, 2)
        print(f'{PerMeter} $')
        return PerMeter
    
    def BuyAraptament(self, plrMoney):
        if plrMoney >= self.price and self.status == 'Available':
            self.status = 'Sold'
            plrMoney -= self.price
            People = ['Беднеку!', 'Джентельмену в шляпе!', 'Беднеку в шляпе!', 'привлекательной леди!(оставьте свой номер)', 'нищей!', 'мне', 'банану в колготках', 'Слону с калькулятором']
            RandomPeople = random.choice(People)
            print(f'Квартира {self.addres} была продана {RandomPeople} за {self.price}$! У вас осталось {plrMoney}$')
            return self.status
        else:
            raise ValueError
P = Apartament('TheBestHouse', 60, 1001)
P.PerMeterPrice
P.BuyAraptament(3233)