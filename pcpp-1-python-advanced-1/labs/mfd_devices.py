from abc import ABC, abstractmethod


class Scanner(ABC):
    def scan_document(self):
        print("Document has been scanned")

    @abstractmethod
    def get_scanner_status(self):
        pass


class Printer(ABC):
    def print_document(self):
        print("Document has been printed")

    @abstractmethod
    def get_printer_status(self):
        pass


class Fax(ABC):
    def send_document(self):
        print("Document has been sent")

    @abstractmethod
    def get_fax_status(self):
        pass


class MFDEntryLevel(Scanner, Printer):
    def get_printer_status(self):
        return {"resolution": "720x720", "serial_number": "PRINTER_ENTRY_LEVEL"}

    def get_scanner_status(self):
        return {"resolution": "720x720", "serial_number": "SCANNER_ENTRY_LEVEL"}


class MFDMediumLevel(MFDEntryLevel):
    def get_printer_status(self):
        return {"resolution": "1080x1080", "serial_number": "PRINTER_MEDIUM_LEVEL"}

    def get_scanner_status(self):
        return {"resolution": "1080x1080", "serial_number": "SCANNER_MEDIUM_LEVEL"}

    def show_operation_history(self):
        print("Operation history")


class MFDPremiumLevel(MFDMediumLevel, Fax):
    def get_printer_status(self):
        return {"resolution": "1440x1440", "serial_number": "PRINTER_PREMIUM_LEVEL"}

    def get_scanner_status(self):
        return {"resolution": "1440x1440", "serial_number": "SCANNER_PREMIUM_LEVEL"}

    def get_fax_status(self):
        return {"serial_number:" "FAX_PREMIUM_LEVEL"}


if __name__ == "__main__":
    mfd_entry_level = MFDEntryLevel()
    print("MDFEntryLevel")
    print(mfd_entry_level.get_scanner_status())
    print(mfd_entry_level.get_printer_status())
    mfd_entry_level.scan_document()
    mfd_entry_level.print_document()
    print()

    mfd_medium_level = MFDMediumLevel()
    print("MDFMediumLevel")
    print(mfd_medium_level.get_scanner_status())
    print(mfd_medium_level.get_printer_status())
    mfd_medium_level.scan_document()
    mfd_medium_level.print_document()
    mfd_medium_level.show_operation_history()
    print()

    mfd_premium_level = MFDPremiumLevel()
    print("MDFPremiumLevel")
    print(mfd_premium_level.get_scanner_status())
    print(mfd_premium_level.get_printer_status())
    print(mfd_premium_level.get_fax_status())
    mfd_premium_level.scan_document()
    mfd_premium_level.print_document()
    mfd_premium_level.show_operation_history()
    mfd_premium_level.send_document()
    print()
