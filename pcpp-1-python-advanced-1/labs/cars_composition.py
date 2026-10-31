class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self._state = "OFF"

    def start(self):
        print(f"Starting {self.fuel_type} engine")
        self._state = "ON"

    def stop(self):
        print(f"Stopping {self.fuel_type} engine")
        self._state = "OFF"

    def get_state(self):
        return {"fuel_type": self.fuel_type, "state": self._state}


class Tires:
    def __init__(self, size, pressure=30):
        self.size = size
        self._pressure = pressure

    def get_pressure(self):
        return {"size": self.size, "pressure": self._pressure}

    def pump(self):
        print(f"Pumping tire size {self.size}")
        self._pressure += 2


class Vehicle:
    def __init__(self, vin: str, engine: Engine, tires: Tires):
        self.vin = vin
        self._engine = engine
        self._tires = tires

    def get_engine_state(self):
        return self._engine.get_state()

    def start_engine(self):
        return self._engine.start()

    def stop_engine(self):
        return self._engine.stop()

    def get_tires_pressure(self):
        return self._tires.get_pressure()

    def pump_tires(self):
        return self._tires.pump()


if __name__ == "__main__":
    eletric_engine = Engine(fuel_type="electric")
    city_tires = Tires(size=15)

    petroil_engine = Engine(fuel_type="petroil")
    off_road_tires = Tires(size=18)

    city_car = Vehicle("AAAA", engine=eletric_engine, tires=city_tires)
    all_terrain_car = Vehicle("BBBB", engine=petroil_engine, tires=off_road_tires)

    print("Engine state:", city_car.get_engine_state())
    city_car.start_engine()
    print("Engine state:", city_car.get_engine_state())
    city_car.stop_engine()

    print("Tires pressure:", city_car.get_tires_pressure())
    city_car.pump_tires()
    print("Tires pressure:", city_car.get_tires_pressure())

    print()

    print("Engine state:", all_terrain_car.get_engine_state())
    all_terrain_car.start_engine()
    print("Engine state:", all_terrain_car.get_engine_state())
    all_terrain_car.stop_engine()

    print("Tires pressure:", all_terrain_car.get_tires_pressure())
    all_terrain_car.pump_tires()
    print("Tires pressure:", all_terrain_car.get_tires_pressure())
