
from models import contact
from services.contact_service import ContactService

class ContactController:
    def __init__(self, contactService : ContactService):
        self.contactService = contactService

    def createContact(self):
        name = input("Enter contact name: ")
        email = input("Enter contact email: ")
        phoneNumber = input("Enter contact phone number: ")
        self.contactService.add_contact(name, email, phoneNumber)
        print("Contact added successfully!")

    def getAllContacts(self):
        contacts = self.contactService.get_all_contacts()

        if not contacts:
            print("No contacts found.")
            return

        for contact in contacts:
            print(f"Name: {contact.name}")
            print(f"Email: {contact.email}")
            print(f"Phone: {contact.phoneNumber}")
            print("-" * 20)

    def showMenu(self):
        while True:
            print("\nContact Management System")
            print("1. Add Contact")
            print("2. View All Contacts")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.createContact()
            elif choice == '2':
                self.getAllContacts()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")