def citire_numar(mesaj: str) -> int:
    while True:
        try:
            return int(input(mesaj))
        except ValueError:
            print("Introduceti un numar intreg!")

def citire_lungime() -> int:
    while True:
        n = citire_numar("Cate numere vreti sa aiba lista dvs.?: ")
        if n > 0:
            return n
        print("Introduceti un numar > 0!")

def citire_lista() -> list:
    numere = []
    n = citire_lungime()
    for i in range(n):
        x = citire_numar(f"Introduceti numarul {i+1} din lista: ")
        numere.append(x)
    return numere

###################################################################################

# sir test: [8, 4, 3, 5, 9 , 10 , 5, 4, 5]
# rezultat: [4, 3, 5, 9, 10]

def cmmdc(x: int, y: int) -> int:
    x = abs(x)
    y = abs(y)
    while y != 0:
        x, y = y, x % y
    return x

def relativ_prime(sir: list) -> list:
    secventa_max = [sir[0]]
    secventa_cur = [sir[0]]
    for i in range(1, len(sir)):
        if cmmdc(sir[i-1], sir[i]) == 1:
            secventa_cur.append(sir[i])
        else:
            secventa_cur = [sir[i]]
        if len(secventa_cur) > len(secventa_max):
            secventa_max = secventa_cur.copy()
    return secventa_max
    
###################################################################################

# sir test: [2, 2, 3, 3, 3, 9, 2, 2]
# rezultat: [3, 3, 3]

def egale(sir: list) -> list:
    secventa_max = [sir[0]]
    secventa_cur = [sir[0]]
    for i in range(1, len(sir)):
        if sir[i-1] == sir[i]:
            secventa_cur.append(sir[i])
        else:
            secventa_cur = [sir[i]]
        if len(secventa_cur) > len(secventa_max):
            secventa_max = secventa_cur.copy()
    return secventa_max

###################################################################################
def meniu():
   print("----- MENIU PRINCIPAL -----")
   print("1. Citirea unei liste")
   print("2. Secventa maxima de numere relativ prime.")
   print("3. Secventa maxima de numere egale.")
   print("4. Iesire din program")

def run():
    lista = []
    while True:
        meniu()
        optiune = input("Alegeti o optiune: ")
        if optiune == '1':
            lista = citire_lista()
        elif optiune == '2':
            if not lista:
                print("Lista e goala, cititi-o la optiunea 1!")
            else:
                secv1 = relativ_prime(lista)
                print(f"Secventa de lungime maxima este {secv1}")
        elif optiune == '3':
            if not lista:
                print("Lista e goala, cititi-o la optiunea 1!")
            else:
                secv2 = egale(lista)
                print(f"Secventa de lungime maxima este {secv2}")
        elif optiune == '4':
            return
        else:
            print("Introduceti o optiune valida! (1, 2, 3, 4)")

run()