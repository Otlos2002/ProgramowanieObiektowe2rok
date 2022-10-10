
https://drive.google.com/drive/folders/1kBOBUI0E1pTlnn5ohyjrWmlKBl6na_Kv

#zad1
# A = [1+x for x in range(0,10)]
# # print(a)
# B = [2*x for x in range(0,10+1)]
# # print(B)
# C = [x**2 for x in range(0,10)]
# # print(C)
# D = [x*0 for x in range(0,10)]
# # print(D)
# E = [x % 2 for x in range(0,11)]
# # print(E)
# F = [x %5 for x in range(0,11)]
# # print(F)

#zad2
# a = []
# x=1
# while x in range(0,11):
#     a.append(x)
#     x+=1
# print(a)

# a = []
# x=1
# while x in range(0,11):
#     a.append(x*2)
#     x+=1
# print(a)

# a = []
# x=1
# while x in range(0,11):
#     a.append(x**2)
#     x+=1
# print(a)

# a = []
# x=1
# while x in range(0,11):
#     a.append(x*0)
#     x+=1
# print(a)

# a = []
# x=0
# while x in range(0,11):
#     a.append(x%2)
#     x+=1
# print(a)

# a = []
# x=1
# while x in range(0,10):
#     a.append(x%5)
#     x+=1
# print(a)

# zad3
# def ile_ujemnych(lista):
#     licznik=0
#     for x in lista:
#         if(x<0):
#             licznik+=1
#     print(licznik)
#
# list = [-1,2,3,-1,-5,-6,-5,-9]
# ile_ujemnych(list)

#zad4
# def iloczyn(lista):
#     wynik=1
#     for x in lista:
#        wynik = wynik*x
#
#     print(wynik)
#
# list = [5, 2, 3]
# iloczyn(list)
#
#zad5
# def minmax(list):
#     M = max(list)
#     m = min(list)
#     return (m,M)
#
# lista=[1,2,6,8,-3]
# print(minmax(lista))
#zad6
# def sumens(list):
#     sign = 1
#     suma = 0
#     for x in list:
#         suma += sign*x
#         sign = -sign
#     print(suma)
#
# lista=[1 ,4 ,16 ,9 ,9, 7, 4, 9, 11]
# sumens(lista)


# Napisz program, który wczytuje kolejną liczbę i dodaje ją do listy, o ile nie wystę-
# puje ona jeszcze na liscie. Gdy lista zawiera dziesięć liczb, program wyświetla jej
#
# zawartość i kończy pracę.
#zad7
def czy_jest(x, list):
    for i in list:
        if i == x:
            return True
    return False


def zadanie7():
    lista = []
    while len(lista) < 10:
        x = input("Podaj liczbe: ")
        if czy_jest(x, lista):
            print("Liczba jest juz na liscie, podaj ina.")
        else:
            lista.append(x)
            print("Dodano!")
    print("Koniec dodawania liczb, lista koncowa: ")
    for x in lista:
        print(x)


#zad8
# Napisz program, który dodaje wszystkie liczby od 2 do 10000 do początkowo pustej
# listy, po czym usuwa wielokrotności 2 (ale nie 2), wielokrotności 3 (ale nie 3), i tak
# dalej, aż do wielokrotności 100. Następnie program wypisuje liczby pozostałe na
# liście.


def zad8():
    list = [x for x in range(2,10000+1)]
    iterat = 0
    for i in list:
        for base in range(2,100+1):
            if i != base and i % base == 0:
                del list[iterat]
                continue
        iterat += 1
    for x in list:
        print(x)

# zad8()

def zad9a(list):
    temp = list[-1]
    list[-1] = list[0]
    list[0] = temp


def zad9b(list):
    ostatniaLiczba = list[-1]
    iterator = len(list) - 1
    while iterator > 0:
        list[iterator] = list[iterator - 1]
        iterator -= 1
    list[0] = ostatniaLiczba


def zad9c(list):
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            list[i] = 0


def zad9e(list):
    dlugosc = len(list)
    if dlugosc % 2 == 1:
        del list[int((dlugosc - 1) / 2)]
    else:
        print(dlugosc)
        del list[int(dlugosc / 2)]
        del list[int((dlugosc / 2)) - 1]


def wiekszy(i, j):
    if i > j:
        return i
    return j


def zad9d(list):
    for x in range(1, len(list) - 1):
        list[x] = wiekszy(list[x - 1], list[x + 1])


def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def sortDown(list, downIndex, upIndex):
    x = upIndex
    while x > downIndex:
        swap(list, x, x - 1)
        x -= 1


def zad9f(list):
    aktualnyPierwszyElement = 0
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            sortDown(list, aktualnyPierwszyElement, i)
            aktualnyPierwszyElement += 1



def zad9g(list):
    najwiekszaWartosc = float('-inf')
    najwiekszyIndex = -1
    najwiekszyIndexDrugi = -1

    for x in range(0, len(list)):
        if list[x] > najwiekszaWartosc:
            najwiekszaWartosc = list[x]
            najwiekszyIndex = x

    najwiekszaWartosc = float('-inf')

    for x in range(0, len(list)):
        if list[x] > najwiekszaWartosc and x != najwiekszyIndex:
            najwiekszaWartosc = list[x]
            najwiekszyIndexDrugi = x

    return najwiekszyIndexDrugi


def zad9h(list):
    for x in range(0, len(list) - 1):
        if list[x] >= list[x + 1]:
            return False
    return True


def zad9i(list):
    for x in range(0, len(list) - 1):
        if list[x] == list[x + 1]:
            return True
    return False



def zad9j(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1):
            if i == j:
                continue
            if list[i] == list[j]:
                return True
    return False


lista = [x ** 2 % 25 for x in range(1, 10)]
lista2 = [x ** 2 % 24 for x in range(1, 10)]
# for x in lista:
#     print(x)
# print("-------------------------------------")
# print(zad9g(lista))
# for x in lista:
#     print(x)



def Equal(lista1, lista2):
    iterator = 0
    length = len(lista1)

    if len(lista2) != length:
        return False

    while iterator < length:
        if lista1[iterator] != lista2[iterator]:
            return False
        iterator += 1

    return True

print(Equal(lista, lista2))














