


import random
num=int(input('pls write number 1 to 100: '))
def guess(num):
    rannum=random.randint(1, 100)
    probe=8
    while probe>0:
        pls (input('type number - remeber in range 1 - 100'))
        if num<rannum:
            print("Don't by shy... go higher!!! Get more!!! Number is bigger!!")
            probe-=1
        if num>rannum:
            print("Fly high but stay grounded... Less is more :D  Number is smaller")
            probe-=1
        else:
            print("The winner take it all!!!")
            break

           


# Zadanie na wtorek:
# gra w zgadywanie liczb
# import random
# wylosowana_liczba = random.randint(1, 100)
# tutaj daj zmienne dot. wygranej i liczby prób
# 1. brak wygranej
# 2. nieprzekroczona liczba prób
# while (DWA WARUNKI):
    # pobranie danych od użytkownika
    # musimy sprawdzić czy użytkownik zgadł
    # a jeśli nie to napisać czy trafił za nisko, czy za wysoko
    # pamiętaj o zwiększaniu liczby prób (+=)
    # pass
# komunikat o przegranej albo wygranej