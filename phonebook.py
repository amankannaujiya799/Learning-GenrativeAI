phone_book = [] //
def display_menu():
    print("\n===== My Little Phone Book =====")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    print("\n--- Add New Contact ---")

    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contact = {
        "name": name,
        "phone": phone
    }

    phone_book.append(contact)

    print("Contact added successfully!")


def view_contacts():

    print("\n--- Your Contacts ---")

    if not phone_book:
        print("📭 Your phone book is empty!")
    else:
        for contact in phone_book:
            print("Name:", contact["name"], "| Phone:", contact["phone"])

def search_contact():

    print("\n--- Search Contact ---")

    search_name = input("Enter name to search: ")

    found = False

    for contact in phone_book:
        if contact["name"].lower() == search_name.lower():
            print("Contact Found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            found = True
            break

    if not found:
        print("Contact not found.")

def delete_contact():

    print("\n--- Delete Contact ---")

    delete_name = input("Enter name to delete: ")

    found = False

    for contact in phone_book:
        if contact["name"].lower() == delete_name.lower():
            phone_book.remove(contact)
            print("Contact deleted successfully!")
            found = True
            break

    if not found:
        print("❌ Contact not found.")


while True:

    display_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact()

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        search_contact()

    elif choice == '4':
        delete_contact()

    elif choice == '5':
        print("Thanks for using Phone Book.")
        break

    else:
        print(" Invalid choice. Please enter number between 1 and 5.")








        if(){

        }else{

        }

elif