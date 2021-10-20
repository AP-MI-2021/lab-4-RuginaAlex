def citire_lista():
    l=[]
    givenString = input ("Dati lista,cu elementele separate prin virgula: ")
    numberAsString = givenString.split (",")
    for x in numberAsString:
        l.append(int(x))
    return l


def numereNegativeNenule (l):
    '''
    Determina toate numerele negative nenule din listă
    :param l: lista de numere intregi
    :return: Returneaza elementele din lista negative nenule
    '''
    rezultat = []
    for x in l:
        if x!=0 and x<0:
         rezultat.append(x)
    return rezultat

def test_numereNegativeNenule ():
    assert numereNegativeNenule ([-1, -56, 0]) == [-1,-56]
    assert numereNegativeNenule ([1, 2, 3]) == []


def main():
    l=[]
    while True:
        print("1.Citire lista")
        print("2.Afișarea tuturor numerelor negative nenule din listă")
        print("a. Afisare lista")
        print("x. Iesire")





        optiune = input ("Dati optiunea: ")


        if optiune == "1":
            l=citire_lista()
        elif optiune == "2":
            print(numereNegativeNenule(l))
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")



main()


