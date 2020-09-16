from prac_06.guitar import Guitar


def main():
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "\nAdded Guitar to the shred list ;)")

    if guitars:
        guitars.sort()
        print("Guitars owned: ")
        for i, guitar in enumerate(guitars, 1):
            vintage_num = ""
            if guitar.is_vintage():
                vintage_num = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
                 {2}".format(i + 1, guitar, vintage_num))
    else:
        print("No guitars available.")


main()
