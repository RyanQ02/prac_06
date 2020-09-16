"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print("Car fuel =", my_car.fuel)
    print("Car odometer =", my_car.odometer)

    print("Car: Fuel = {}, Odometer = {}\n".format(my_car.fuel, my_car.odometer))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("Limo fuel =", limo.fuel)
    limo.drive(115)
    print("Limo odometer =", limo.odometer)

    print("Limo: Fuel = {}, Odometer = {}".format(my_car.fuel, my_car.odometer))


main()
