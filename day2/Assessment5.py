def write_contact(dict):
    with open("contacts.txt", "a") as file:
        file.write(f"{dict['Name']} | {dict['Email']} | {dict['Phone']}")
        file.write("\n")
    print("Contact saved.")
        

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = []
            for line in file:
                contacts.append(line.strip())
            return contacts
    except FileNotFoundError:
        return []
    
def main():
    name =input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")

    contact_dict = {
        "Name": name,
        "Phone": phone,
        "Email": email
    }

    write_contact(contact_dict)

    print("Contacts List:")
    contacts = load_contacts()
    for contact in contacts:
        print(contact)
    
main()