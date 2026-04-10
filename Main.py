class Apartament:
    def __init__(self, addres, area, price):
        self.CanWrite = True
        self.addres = addres
        self.area = area
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value >= 1000:
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
P = Apartament('TheBestHouse', 60, 1001)
P.PerMeterPrice