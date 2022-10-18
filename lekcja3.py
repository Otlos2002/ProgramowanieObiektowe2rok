import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @staticmethod
    def distance(point1, point2):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

class SodaCan:
    def __init__(self, h, r):
        self.h = h
        self.r = r
    def get_surface_area(self):
        return 2 *math.pi * self.r * self.h

    def get_volume(self):
        return math.pi * self.r**2 * self.h
class Adres:
    def __init__(self, nr_domu, ulica, miasto, kod_pocztowy, nr_mieszkania = None):
        self.nr_domu = nr_domu
        self.ulica = ulica
        self.miasto = miasto
        self.kod_pocztowy = kod_pocztowy

        if nr_mieszkania is not None:
            self.nr_mieszkania = nr_mieszkania

    def show(self):
        if hasattr(self, 'nr_mieszkania'):
            print(self.ulica + ' ' + self.nr_domu + '/' + self.nr_mieszkania)
            print(self.kod_pocztowy + ' ' + self.miasto)
        else:
            print(self.ulica + ' ' + self.nr_domu)
            print(self.kod_pocztowy + ' ' + self.miasto)
    def comes_before(self, other) -> bool:
        for i in range(len(self.kod_pocztowy)):
            if self.kod_pocztowy[i] == other.kod_pocztowy[i]:
                continue
            if self.kod_pocztowy[i] < other.kod_pocztowy[i]:
                return True
            return False

class Car:
    def __init__(self, eff : float, fuel_qty : float ):
        self.eff= eff
        self.fuel_qty = fuel_qty
        self.current_fuel = 0
    def drive(self, road : float) -> None:
        fuel_burn = road / self.eff
        if fuel_burn > self.current_fuel:
            print("Nie ma tyle paliwa")
            return None
        self.current_fuel -= road / self.eff

    def get_fuel_level(self) ->:






Point = Punkt(0,0)
NamedPoint = Punkt(1,1)
print(Punkt.distance(Point, NamedPoint))

adresik1 = Adres('2', "Gola", "Olsztyn", "10-270", '71')
adresik2 = Adres('12', "nieGola", "Trojmiasto", "10-314")
adresik1.show()
adresik2.show()
print (adresik1.comes_before(adresik2))

pucha = SodaCan(25.5, 6)

print(pucha.get_volume())
print(pucha.get_surface_area())









