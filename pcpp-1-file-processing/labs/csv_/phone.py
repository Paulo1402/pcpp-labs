import csv
from dataclasses import dataclass


@dataclass
class PhoneContact:
    name: str
    phone: str


class Phone:
    def __init__(self):
        self._contacts = []

    def load_contacts_from_csv(self, file):
        with open(file, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                contact = PhoneContact(name=row["Name"], phone=row["Phone"])
                self._contacts.append(contact)

    def search_contacts(self, term):
        results = []

        for contact in self._contacts:
            match_name = term.lower() in contact.name.lower()
            match_phone = term in contact.phone

            if match_name or match_phone:
                results.append(contact)

        return results


if __name__ == "__main__":
    phone = Phone()
    phone.load_contacts_from_csv("./csv_/contacts.csv")

    term = input("Search contacts: ")
    results = phone.search_contacts(term)

    print()

    if results:
        print("Contacts found:\n")

        for contact in results:
            print(contact.name, contact.phone)
    else:
        print("No contacts found")
