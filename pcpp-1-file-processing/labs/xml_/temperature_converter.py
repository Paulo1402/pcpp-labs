import xml.etree.ElementTree as ET


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        return 9 / 5 * temperature_in_celsius + 32


class ForecastXmlParser:
    def __init__(self):
        self._converter = TemperatureConverter()

    def parse(self, path):
        tree = ET.parse(path)
        root = tree.getroot()

        for item in root.findall("item"):
            day = item.find("day").text
            temperature_in_celsius = item.find("temperature_in_celsius").text
            temperature_in_fahrenheit = self._converter.convert_celsius_to_fahrenheit(
                float(temperature_in_celsius)
            )

            print(
                f"{day}: {temperature_in_celsius} Celsius, {temperature_in_fahrenheit} Fahrenheit"
            )


parser = ForecastXmlParser()
parser.parse("xml_/forecast.xml")
