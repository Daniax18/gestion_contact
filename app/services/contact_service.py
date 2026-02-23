from models.contact import Contact

class ContactService:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phoneNumber):
        contact = Contact(name, email, phoneNumber)
        self.contacts.append(contact)

    def get_all_contacts(self):
        return self.contacts