a = "Michal" # 1 Úkol - Proměnná, která vyjadřuje jméno.
b = "Polach" # 2 Úkol - Proměnná, která vyjadřuje příjmení.
print(a + " " + b) #3 Úkol + mezera mezi jmény

vek = int(input("Uveďte věk: ")) #4 Úkol - Uživatel napíše věk, který se mu vypíše zpátky do konzole
print("Váš věk:", vek)

print("Délka proměnné 'a':", len(a))  #5 Úkol - print vypíše text a upřesní o jakou proměnnou délku se jedná, len(a)
print("Délka proměnné 'b':", len(b))  #5 Úkol - print vypíše text a upřesní o jakou proměnnou délku se jedná, len(b)

c = 6 #6 Úkol - vytvořená proměnna s hodnotou 6

d = 0 #7 Úkol proměnna s hodnotou 0(Začátek)

for i in range(5): # Nastauje maximální počet kol od 0-4
    d += 3 # Každé kolo přičítá o 3 navíc
    print(d) #8 Úkol - Vyhodí nám zpátky výsledek.

while True:
    try:
        vek2 = int(input("Uveďte věk: "))# input, který je limitován jen na číslice pomocí int.
        print("Děkuji") # Vypisuje děkuji po správné hodnotě.
        break # Pokud byl věk správný, tak ukončí while.
    if vek2 = False
    
    except ValueError:
    print(Zadej jen celočíselnou hodnotu.)

