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



def numar_minim (l,k):
    '''
    Determinam cel mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura
    :param l: Lista de numere intregi
    :param k: Numarul citit de la tastatura
    :return: Returnam cel mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura
    '''

    c=0
    minimul=None
    for y in l:
        c=y%10
        if c==k and (minimul is None or y>minimul):
            minimul=y
    return minimul


def test_numar_minim ():
    assert numar_minim ([1, 6, 34, 68, 40, 48, 20] , 8) == 48
    assert numar_minim ([1, 2, 3],0) == []









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


        elif optiune == "3":
            k=int(input("Dati un nr: "))
            minimul= numar_minim(l,k)
            if max is None:
                print ("Nu exista")
            else:
                print (minimul)


        elif optiune == "a":
            print(l)


        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")



main()


