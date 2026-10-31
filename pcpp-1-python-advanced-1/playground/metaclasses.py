import datetime


class LoggingMeta(type):
    CLASSES = []

    def __new__(mcs, name, bases, namespace):
        namespace.update(
            {
                "instantiation_time": datetime.datetime.now(),
                "get_instantiation_time": lambda self: self.instantiation_time,
            }
        )
        obj = super().__new__(mcs, name, bases, namespace)

        mcs.CLASSES.append(name)

        return obj


class User(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name


class Car(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    user = User("Paulo")
    car = Car("BMW")

    print(user.get_instantiation_time())
    print(car.get_instantiation_time())
    print(LoggingMeta.CLASSES)
