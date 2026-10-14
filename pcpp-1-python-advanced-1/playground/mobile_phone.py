class MobilePhone:
    def __init__(self, number):
        self._number = number
        self._is_on = False

    @property
    def number(self):
        return self._number

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self):
        if self._is_on:
            print("mobile phone is already on")
            return

        print(f"mobile phone {self._number} is turned on")
        self._is_on = True

    def turn_off(self):
        if not self._is_on:
            print("mobile phone is already off")
            return

        print("mobile phone is turned off")
        self._is_on = False

    def call(self, phone: "MobilePhone"):
        if not phone.is_on:
            print(f"mobile phone {phone.number} is off, try again later")

        print(f"calling {phone.number}...")


if __name__ == "__main__":
    phone1 = MobilePhone("41 987211886")
    phone2 = MobilePhone("41 988647260")

    phone1.turn_on()
    phone2.turn_on()

    phone1.call(phone2)

    phone1.turn_off()
    phone2.turn_off()
