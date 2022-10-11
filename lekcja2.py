def mult(a):
    ilo = 1
    for i in a:
        ilo *= i
    return ilo

# print(mult([3, 5, 7]))
# print(mult(range(3, 8, 2)))

#zad2
# Napisz funkcj˛e mult_ints, która przyjmuje jeden argument tylko pozycyjny. Załó˙z,
# ˙ze ten argument jest niepustym obiektem iterowalnym typu krotka, lista, zbiór lub zakres.
# Jako wynik zwraca iloczyn tych argumentów, które sa˛ typu całkowitego. Wfunkcji main
# przetestuj działanie funkcji mult_ints.
# Przykładowo, wywołanie
# mult_ints(3, 3.14, 5, "abc", 7) powinno zwróci´c liczb˛e 105.

def mult_ints(b):
    ilo = 1
    for i in b:
        if type(i) == int:
            ilo *= i
    return ilo

# print(mult_ints([3, 3.14, 5, "abc", 7]))

#zad3
def multiply(*args):
    ilo = 1
    for i in args:
        ilo *= i
    return ilo

print(multiply(3, 5, 7))

#zad4
def mult_ints(*args):
    ilo = 1
    for i in args:
        if type(i) == int:
            ilo *= i
    return ilo

print(mult_ints(3, 5, 7))

#zad5
def make_car(firma, model, **kwargs):
    slownik = kwargs
    slownik['firma'] = firma
    slownik['model'] = model
    return slownik

# print(make_car("Kia", 'Picanto', kolor='czerwony', nrseryjny=900))


#zad 3.1
# Program to add two matrices using nested loop

X = [[x for x in range(1,10+1)],
    [x**2 for x in range(1,10+1)],
    [x**3 for x in range(1,10+1)]]

for i in X:
    print(i)

#zad 3.2
Y = [[1],
    [1,2],
    [1,2,3],
    [1,2,3,4],
    [1,2,3,4,5],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9,10]]

suma=0
for i in Y:
    for x in i:
        suma+=x
print(suma)













