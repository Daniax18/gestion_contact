
from models import contact
from services.contact_service import ContactService

class ContactView:
    def __init__(self, contactService : ContactService):
        self.contactService = contactService

    def createContact(self):
        name = input("Enter contact name: ")
        email = input("Enter contact email: ")
        phoneNumber = input("Enter contact phone number: ")
        self.contactService.add_contact(name, email, phoneNumber)

    def getAllContacts(self):
        contacts = self.contactService.get_all_contacts()
       
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
            print("3. Delete Contact")
            print("4. Count Contacts")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.createContact()
            elif choice == '2':
                self.getAllContacts()
            elif choice == '3':
                phoneNumber = input("Enter phone number of contact to delete: ")
                self.contactService.delete_contact(phoneNumber)
            elif choice == '4':
                count = self.contactService.count_contacts()
                print(f"Response => Total contacts: {count}")
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")