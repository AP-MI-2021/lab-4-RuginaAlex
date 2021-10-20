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

    maximul=none
    minimul=None
    for y in l:

        if y%10 ==k:
            minimul=y
        if maximul is None or minimul<maximul:
            maximul=minimul
    return maximul


def test_numar_minim ():
    assert numar_minim ([28,38,0] ,8) == 28
    assert numar_minim ([1, 2, 3],0) is None


def super_prim(l):
    '''
    Determinam numerele superprime
    :param l: lista de numere intregi
    :return: Returnam lista numerele superprime
    '''
    rezultat=[]
    nr=0
    for x in l:
        while x>0 and ok==1:
            d=0
            for i in range(2,len(l//2),1):
                if x%i == 0:
                    d=1
            if d>0 :
                ok=0
            x=x//10
        if ok == 1:
            rezultat.append (x)
            nr=nr+1



def test_super_prim():
    assert super_prim ([239 , 0]) == 239
    assert super_prim ([22,24]) == []












def main():
    test_numereNegativeNenule()
    l=[]

    while True:
        print("1.Citire lista")
        print("2.Afișarea tuturor numerelor negative nenule din listă")
        print("3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură")
        print("4.Afișarea tuturor numerelor din listă care sunt superprime.")
        print("a. Afisare lista")
        print("x. Iesire")





        optiune = input ("Dati optiunea: ")


        if optiune == "1":
            l=citire_lista()


        elif optiune == "2":
            print(numereNegativeNenule(l))


        elif optiune == "3":
            k=int(input("Dati un nr: "))
            maximul= numar_minim(l,k)
            if maximul is None:
                print ("Nu exista")
            else:
                print (maximul)


        elif optiune == "a":
            print(l)


        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")



main()


