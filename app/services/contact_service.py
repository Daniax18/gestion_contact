from models.contact import Contact

class ContactService:
    def __init__(self):
        self.contacts = []

    def find_contact_by_phone(self, phoneNumber):
        for contact in self.contacts:
            if contact.phoneNumber == phoneNumber:
                return contact
        return None

    def add_contact(self, name, email, phoneNumber):
        if self.find_contact_by_phone(phoneNumber):
            print("Response => A contact with this phone number already exists.")
            return
        contact = Contact(name, email, phoneNumber)
        self.contacts.append(contact)
        print("Response => Contact added successfully!")

    def get_all_contacts(self):
        contacts = self.contacts
        if not contacts:
            print("Response => No contacts found.")
            return []
        return contacts
    
    def delete_contact(self, phoneNumber):
        contact = self.find_contact_by_phone(phoneNumber)
        if contact:
            self.contacts.remove(contact)
            print("Response => Contact deleted successfully.")
        else:
            print("Response => Contact not found.")

    def count_contacts(self):
        return len(self.contacts)
    
