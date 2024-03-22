import sys
from database import SessionLocal
from db.models import Lawyer, Case, Client
from helpers import validate_email, validate_phone_number


def main():
    print("Welcome to Lawyers Dome CLI!")
    print("1. Manage Lawyers")
    print("2. Manage Cases")
    print("3. Manage Clients")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_lawyers()
        elif choice == "2":
            manage_cases()
        elif choice == "3":
            manage_clients()
        elif choice == "4":
            print("Exiting Lawyers Dome CLI. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid option.")


def manage_lawyers():
    print("Lawyers Management Menu")
    print("1. Create Lawyer")
    print("2. View Lawyers")
    print("3. Back to Main Menu")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            create_lawyer()
        elif choice == "2":
            view_lawyers()
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please enter a valid option.")


def create_lawyer():
    print("Creating a Lawyer")
    name = input("Enter lawyer's name: ")
    email = input("Enter lawyer's email: ")
    phone = input("Enter lawyer's phone number: ")

    # Validate email and phone number
    if not email or not validate_email(email):
        print("Invalid email format. Please enter a valid email.")
        return
    if not phone or not validate_phone_number(phone):
        print("Invalid phone number format. Please enter a valid phone number.")
        return

    # Create a session and use it to add the new lawyer to the database
    session = SessionLocal()
    lawyer = Lawyer(name=name, email=email, phone=phone)
    session.add(lawyer)
    session.commit()
    print("Lawyer created successfully.")
    session.close()


def view_lawyers():
    print("Viewing Lawyers")
    # Create a session and use it to query all lawyers from the database
    session = SessionLocal()
    lawyers = session.query(Lawyer).all()

    if lawyers:
        print("List of Lawyers:")
        for lawyer in lawyers:
            print(f"Name: {lawyer.name}, Email: {lawyer.email}, Phone: {lawyer.phone}")
    else:
        print("No lawyers found.")

    input("Press Enter to continue...")
    session.close()


def manage_cases():
    print("Cases Management Menu")
    print("1. Create Case")
    print("2. View Cases")
    print("3. Back to Main Menu")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            create_case()
        elif choice == "2":
            view_cases()
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please enter a valid option.")


def create_case():
    print("Creating a Case")
    title = input("Enter case title: ")
    description = input("Enter case description: ")

    # Create a session and use it to add the new case to the database
    session = SessionLocal()
    case = Case(title=title, description=description)
    session.add(case)
    session.commit()
    print("Case created successfully.")
    session.close()


def view_cases():
    print("Viewing Cases")
    # Create a session and use it to query all cases from the database
    session = SessionLocal()
    cases = session.query(Case).all()

    if cases:
        print("List of Cases:")
        for case in cases:
            print(f"Title: {case.title}, Description: {case.description}")
    else:
        print("No cases found.")

    input("Press Enter to continue...")
    session.close()


def manage_clients():
    print("Clients Management Menu")
    print("1. Create Client")
    print("2. View Clients")
    print("3. Back to Main Menu")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            create_client()
        elif choice == "2":
            view_clients()
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please enter a valid option.")


def create_client():
    print("Creating a Client")
    name = input("Enter client name: ")
    email = input("Enter client email: ")
    phone = input("Enter client phone number: ")

    # Validate email and phone number
    if not email or not validate_email(email):
        print("Invalid email format. Please enter a valid email.")
        return
    if not phone or not validate_phone_number(phone):
        print("Invalid phone number format. Please enter a valid phone number.")
        return

    # Create a session and use it to add the new client to the database
    session = SessionLocal()
    client = Client(name=name, email=email, phone_number=phone)
    session.add(client)
    session.commit()
    print("Client created successfully.")
    session.close()


def view_clients():
    print("Viewing Clients")
    # Create a session and use it to query all clients from the database
    session = SessionLocal()
    clients = session.query(Client).all()

    if clients:
        print("List of Clients:")
        for client in clients:
            print(f"Name: {client.name}, Email: {client.email}, Phone: {client.phone_number}")
    else:
        print("No clients found.")

    input("Press Enter to continue...")
    session.close()


if __name__ == "__main__":
    main()
