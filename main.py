def citire_numar(mesaj: str) -> int:
    """
        O functie pentru citirea unui numar. 
        Daca input-ul nu este un numar intreg, utilizatorul este rugat sa introduca un numar intreg si nimic altceva.
    """
    while True:
        try:
            return int(input(mesaj))
        except ValueError:
            print("Introduceti un numar intreg!")

def citire_lungime_lista() -> int:
    """
        Aceasta functie trateaza separat cazul in care utilizatorul introduce un numar negativ pentru lungimea listei.
    """
    while True:
        numar = citire_numar("Cate numere vreti sa aiba lista?: ")
        if numar > 0:
            return numar
        else:
            print("Introduceti un numar pozitiv!")

def citire_lista() -> list:
    """
        Aceasta functie il lasa pe utilizator sa puna numere intregi intr-o lista.
    """
    sir = []
    n = citire_lungime_lista()
    primul = citire_numar("Introduceti primul element din lista: ")
    sir.append(primul)
    for i in range(1, n):
        element = citire_numar(f"Introduceti cel de-al {i+1}-lea element din lista: ")
        sir.append(element)
    return sir

# sir test: [2, 5, 7, 9, 10, 2, 4]
# rezultat: [2, 5, 7, 9, 10]

def cmmdc(x, y):
    """
        O functie pentru cmmdc. Functioneaza si in cazul numerelor negative.
    """
    x = abs(x)
    y = abs(y)
    while y != 0:
        rest = x % y
        x = y
        y = rest
    return x


def relativ_prime(sir: list) -> list:
    """
        O functie care gaseste secventa de lungime maxima in care oricare doua elemente consec sunt prime intre ele
    """
    secv_max = []
    lg_cur = 1
    lg_max = 1
    left = 0
    right = 0
    left_max = 0
    right_max = 0
    for i in range(1, len(sir)): 
        if cmmdc(sir[i-1], sir[i]) == 1:
            right += 1
            lg_cur += 1
        else:
            left = i
            right = i
            lg_cur = 1
        if lg_cur > lg_max:
            right_max = right
            left_max = left
            lg_max = lg_cur
               
    for el in range(left_max, right_max + 1):
        secv_max.append(sir[el])
    return secv_max

# sir test = [2, 2, 3, 3, 1]
# rezultat = [2, 2]

def egale(sir: list) -> list:
    """
        O functie care determina secventa de lungime maxima in care toate elementele sunt egale.
    """
    secv_max = []
    lg_cur = 1
    lg_max = 1
    left = 0
    right = 0
    left_max = 0
    right_max = 0
    for i in range(1, len(sir)): 
        if sir[i-1] == sir[i]:
            right += 1
            lg_cur += 1
        else:
            left = i
            right = i
            lg_cur = 1
        if lg_cur > lg_max:
            right_max = right
            left_max = left
            lg_max = lg_cur
                   
    for el in range(left_max, right_max + 1):
        secv_max.append(sir[el])
    return secv_max

def meniu():
    """
        O functie care printeaza in consola meniul cu optiuni, practic
        interfata utilizatorului.
    """
    print("---------MENIU---------")
    print("1. Cititi o lista de numere intregi.")
    print("2. Gasiti secventa de lungime maxima in care oricare doua elemente consecutive sunt relativ prime intre ele.")
    print("3. Gasiti secventa de lungime maxima care are toate elementele egale. ")
    print("4. Iesire din program.")
    print()


def run():
    lista = []
    while True:
        meniu()
        optiune = input("Alegeti o optiune: ")
        if optiune == '1':
            lista = citire_lista()
        elif optiune == '2':
            if not lista:
                print("Lista este goala! Selectati prima optiune pentru a pune valori in lista dvs.")
            else:
                secventa1 = relativ_prime(lista)
                print(f"Secventa de lungime maxima in care oricare doua elemente consecutive sunt prime este: {secventa1}")
                print()
        elif optiune == '3':
            if not lista:
                print("Lista este goala! Selectati prima optiune pentru a pune valori in lista dvs.")
            else:
                secventa2 = egale(lista)
                print(f"Secventa de lungime maxima in care toate elementele sunt egale este: {secventa2}")
                print()
        elif optiune == '4':
            return
        else:
            print("Introduceti o optiune valida! (1, 2, 3, 4)")

run()