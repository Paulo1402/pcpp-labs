import configparser
import xml.parsers


class ConfigParser:
    def __init__(self, config_file):
        self._config_file = config_file

    def parse_environments(self, dev_out_file, prod_out_file):
        parser = configparser.ConfigParser()
        successful = parser.read(self._config_file)

        if not successful:
            raise RuntimeError("Can't parse config file, check the file path")

        dev_config_dict = {}
        prod_config_dict = {}

        for section in parser.sections():
            options = dict(parser.items(section))
            env = options.pop("env")

            if env == "prod":
                prod_config_dict[section] = {**options}
            else:
                dev_config_dict[section] = {**options}

        dev_config = configparser.ConfigParser()
        dev_config.read_dict(dev_config_dict)

        with open(dev_out_file, "w") as dev_file:
            dev_config.write(dev_file)

        prod_config = configparser.ConfigParser()
        prod_config.read_dict(prod_config_dict)

        with open(prod_out_file, "w") as prod_file:
            prod_config.write(prod_file)


parser = ConfigParser("./configparser_/mess.ini")
parser.parse_environments(
    dev_out_file="./configparser_/dev_config.ini",
    prod_out_file="./configparser_/prod_config.ini",
)
