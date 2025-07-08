ukoly = []

def pridej_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný.")
            continue
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný.")
            continue
        ukol = {"nazev": nazev, "popis": popis}
        ukoly.append(ukol)
        print(f'Úkol "{nazev}" byl přidán.')
        break

def zobraz_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['nazev']}: {ukol['popis']}")

def odstran_ukol(index):
    if 0 < index <= len(ukoly):
        odebrany = ukoly.pop(index - 1)
        print(f'Úkol "{odebrany["nazev"]}" byl odstraněn.')
    else:
        print("Neplatné číslo úkolu.")

def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridej_ukol()
        elif volba == "2":
            zobraz_ukoly()
        elif volba == "3":
            zobraz_ukoly()
            if ukoly:
                try:
                    cislo = int(input("Zadejte číslo úkolu k odstranění: "))
                    odstran_ukol(cislo)
                except ValueError:
                    print("Zadejte platné číslo.")
            else:
                print("Seznam je prázdný.")
        elif volba == "4":
            print("Program ukončen.")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
    hlavni_menu()





        