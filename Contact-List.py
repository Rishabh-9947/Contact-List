# Contact List Application

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact(name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added successfully.")

# Function to display all contacts
def display_contacts():
    if contacts:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Your contact list is empty.")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print(f"Contact '{name}' not found.")

# Function to edit an existing contact
def edit_contact(name, phone, email):
    if name in contacts:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Main function to run the contact list application
def main():
    while True:
        print("\n--- Contact List Menu ---")
        print("1: Add a new contact")
        print("2: Display all contacts")
        print("3: Search for a contact")
        print("4: Edit a contact")
        print("5: Delete a contact")
        print("6: Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            search_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to edit: ")
            phone = input("Enter new contact phone: ")
            email = input("Enter new contact email: ")
            edit_contact(name, phone, email)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            print("Exiting the Contact List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

