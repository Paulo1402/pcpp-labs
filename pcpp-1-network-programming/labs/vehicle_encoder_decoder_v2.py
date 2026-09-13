from jsonparser.json_parser import JsonParserMixin


class ValidationError(Exception):
    pass


class Vehicle(JsonParserMixin):
    def __init__(
        self,
        registration_number: str,
        year_of_production: int | str,
        passenger: bool | str,
        mass: float | str,
    ):
        year_of_production_clean, passenger_clean, mass_clean = self._clear_data(
            year_of_production, passenger, mass
        )

        self._data = {
            "registration_number": registration_number,
            "year_of_production": year_of_production_clean,
            "passenger": passenger_clean,
            "mass": mass_clean,
        }

    def _clear_data(self, year_of_production, passenger, mass):
        # Year of production
        try:
            year_of_production = int(year_of_production)
        except ValueError:
            raise ValidationError("Year of production must be an integer number")

        # Passenger
        if isinstance(passenger, str):
            if passenger == "y":
                passenger = True
            elif passenger == "n":
                passenger = False
            else:
                raise ValidationError('Passenger only accepts "y" or "n"')

        # Mass
        try:
            mass = float(mass)
        except ValueError:
            raise ValidationError("Vehicle mass must be a number")

        return year_of_production, passenger, mass

    def __str__(self):
        return f"{self.__class__.__name__}({self.__dict__})"


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
        passenger = input("Passenger [y/n]: ")
        mass = input("Vehicle mass: ")

        vehicle = Vehicle(registration_number, year_of_production, passenger, mass)
        json_string = vehicle.encode()

        print()
        print("Resulting JSON string is:")
        print(json_string)
    elif choice == "2":
        json_string = input("Enter vehicle JSON string: ")
        vehicle = Vehicle.decode(json_string)

        print(vehicle)
    else:
        print("Invalid option, try again")
        exit(1)

    print()
    print("Done")
