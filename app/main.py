from services.contact_service import ContactService
from controllers.contact_controller import ContactController

def main():
    contact_service = ContactService()
    contact_controller = ContactController(contact_service)
    contact_controller.showMenu()

if __name__ == "__main__":
    main()