
#  a class to represent each contact
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


#  a class for the Contact Book
class ContactBook:
    def __init__(self):
        self.contacts = {}

    #  to add a new contact
    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact {name} already exists!")
        else:
            self.contacts[name] = Contact(name, phone, email)
            print(f"Contact {name} added successfully!")

    #  to view all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the contact book.")
        else:
            for contact in self.contacts.values():
                print(contact)

    #  to search for a contact
    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(contact)
        else:
            print(f"Contact {name} not found.")

    #  to update an existing contact
    def update_contact(self, name, phone=None, email=None):
        contact = self.contacts.get(name)
        if contact:
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")

    #  to delete a contact
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")


#   to run the contact book
def main():
    book = ContactBook()
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            book.add_contact(name, phone, email)
        
        elif choice == '2':
            book.view_contacts()

        elif choice == '3':
            name = input("Enter the name to search: ")
            book.search_contact(name)
        
        elif choice == '4':
            name = input("Enter the name to update: ")
            phone = input("Enter new phone number (or press Enter to skip): ")
            email = input("Enter new email address (or press Enter to skip): ")
            book.update_contact(name, phone if phone else None, email if email else None)
        
        elif choice == '5':
            name = input("Enter the name to delete: ")
            book.delete_contact(name)
        
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
