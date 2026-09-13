import logging
import random
import time


class Logger(logging.Logger):
    def __init__(self, name, level, output_file, mode="a"):
        super().__init__(name, level)

        formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")
        file_handler = logging.FileHandler(output_file, mode)
        stream_handler = logging.StreamHandler()

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        self.addHandler(file_handler)
        self.addHandler(stream_handler)


class BatteryTemperatureScan:
    def __init__(self, logger, interval=60, unit="C"):
        self._logger = logger
        self._interval = interval
        self._unit = unit

    def scan(self):
        while True:
            temperature = self._get_battery_temperature()
            self._log_temperature(temperature)

            time.sleep(self._interval)

    def _log_temperature(self, temperature):
        message = f"{temperature} {self._unit}"

        if temperature <= 30:
            self._logger.debug(message)
        elif temperature >= 30 and temperature <= 35:
            self._logger.warning(message)
        else:
            self._logger.critical(message)

    def _get_battery_temperature(self):
        temperature = random.randrange(20, 40)
        return temperature


logger = Logger(
    __name__, level=logging.DEBUG, output_file="./logging_/battery_temperature.log"
)
battery_scan = BatteryTemperatureScan(logger=logger)
battery_scan.scan()
