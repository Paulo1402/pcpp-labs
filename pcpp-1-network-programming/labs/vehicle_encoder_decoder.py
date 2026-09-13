import json
from dataclasses import dataclass


@dataclass
class Vehicle:
    registration_number: str
    year_of_production: int
    passenger: bool
    mass: float


class VehicleDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        return Vehicle(**dct)


class VehicleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Vehicle):
            return obj.__dict__

        return super().default(obj)


if __name__ == "__main__":
    print("What can I do for you?")
    print("1 - produce a JSON string describing a vehicle")
    print("2 - decode a JSON string into vehicle data")
    print()

    choice = input("Your choice: ")
    print()

    if choice == "1":
        registration_number = input("Registration number: ")
        year_of_production = input("Year of production: ")

        try:
            year_of_production = int(year_of_production)
        except ValueError:
            raise ValueError("Year of production must be an integer number")

        passenger = input("Passenger [y/n]: ").lower()

        if passenger == "y":
            passenger = True
        elif passenger == "n":
            passenger = False
        else:
            raise ValueError('Passenger only accepts "y" or "n"')

        mass = input("Vehicle mass: ")

        try:
            mass = float(mass)
        except ValueError:
            raise ValueError("Vehicle mass must be a number")

        vehicle = Vehicle(registration_number, year_of_production, passenger, mass)

        print()
        print("Resulting JSON string is:")
        print(json.dumps(vehicle, cls=VehicleEncoder))

    elif choice == "2":
        json_string = input("Enter vehicle JSON string: ")
        vehicle = json.loads(json_string, cls=VehicleDecoder)

        print(vehicle)
    else:
        print("Invalid option, try again")
        exit(1)

    print()
    print("Done")
