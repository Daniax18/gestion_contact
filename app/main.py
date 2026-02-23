from views.contact_view import ContactView
from services.contact_service import ContactService

def main():
    contact_service = ContactService()
    contact_controller = ContactView(contact_service)
    contact_controller.showMenu()

main()