class Scanner:
    def scan(self):
        print("scan() method from Scanner class")


class Printer:
    def print(self):
        print("print() method from Printer class")


class Fax:
    def print(self):
        print("print() method from Fax class")

    def send(self):
        print("send() method from Fax class")


class MDF_SPF(Scanner, Printer, Fax):
    pass


class MDF_SFP(Scanner, Fax, Printer):
    pass


if __name__ == "__main__":
    mdf_spf = MDF_SPF()
    mdf_spf.scan()
    mdf_spf.print()
    mdf_spf.send()
    
    print()
    
    mdf_sfp = MDF_SFP()
    mdf_sfp.scan()
    mdf_sfp.print()
    mdf_sfp.send()
    
