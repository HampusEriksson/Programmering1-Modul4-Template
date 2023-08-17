# Restaurangrouletten
# Namn
# Klass
# Påbörjat datum

# Du och dina vänner ska gå på restaurang. För att göra besöket lite festligare
# och mer spännande så kommer en av er att lottas ut för att betala hela notan.
# I denna uppgift ska du göra två olika lösningar.
# Du gör ena i funktionen check_with_choice och den andra i check_without_choice.
from random import choice, randint


def check_with_choice(names, cost):
    # I denna funktion ska du returnera en string
    # med namnet på den person som ska betala.
    # Hen väljs ut från listan names med choice-funktionen.
    person = ""
    return f"{person} ska betala {cost} kr för middagen."


def check_without_choice(names, cost):
    # I denna funktion ska du returnera en string
    # med namnet på den person som ska betala.
    # Hen väljs ut från listan names utan choice-funktionen.
    # Kom på ett annat sätt att slumpa fram en person ur listan.
    # Tips, du får använd randint, frågan är bara mellan vilka tal.
    person = ""
    return f"{person} ska betala {cost} kr för middagen."


def main():
    print("Mata in alla som åt middag, separera med kommatecken och mellanslag.")
    names_string = input()
    names = names_string.split(", ")
    cost = int(input("Notan kostade: "))

    print(check_with_choice(names), cost)
    print(check_without_choice(names), cost)


main()