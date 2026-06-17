import os

USERS_FILE = "users.txt"
TICKETS_FILE = "tickets.txt"


def register_user():
    username = input("Enter username: ")

    with open(USERS_FILE, "a") as file:
        file.write(username + "\n")

    print("User registered successfully!")


def create_ticket():
    username = input("Enter username: ")
    issue = input("Describe the issue: ")

    ticket_id = 1

    if os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, "r") as file:
            lines = file.readlines()
            ticket_id = len(lines) + 1

    with open(TICKETS_FILE, "a") as file:
        file.write(f"{ticket_id},{username},{issue},Open\n")

    print(f"Ticket #{ticket_id} created successfully!")


def view_tickets():
    if not os.path.exists(TICKETS_FILE):
        print("No tickets found.")
        return

    with open(TICKETS_FILE, "r") as file:
        tickets = file.readlines()

    print("\n----- TICKETS -----")

    for ticket in tickets:
        data = ticket.strip().split(",")
        print(
            f"ID: {data[0]} | User: {data[1]} | Issue: {data[2]} | Status: {data[3]}"
        )


def update_ticket():
    ticket_id = input("Enter Ticket ID: ")

    if not os.path.exists(TICKETS_FILE):
        print("No tickets found.")
        return

    updated = []

    with open(TICKETS_FILE, "r") as file:
        tickets = file.readlines()

    for ticket in tickets:
        data = ticket.strip().split(",")

        if data[0] == ticket_id:
            print("1. In Progress")
            print("2. Resolved")

            choice = input("Select status: ")

            if choice == "1":
                data[3] = "In Progress"
            elif choice == "2":
                data[3] = "Resolved"

            updated.append(",".join(data) + "\n")
        else:
            updated.append(ticket)

    with open(TICKETS_FILE, "w") as file:
        file.writelines(updated)

    print("Ticket updated successfully!")


def menu():
    while True:
        print("\n===== IT HELP DESK MANAGEMENT SYSTEM =====")
        print("1. Register User")
        print("2. Create Ticket")
        print("3. View Tickets")
        print("4. Update Ticket Status")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            create_ticket()

        elif choice == "3":
            view_tickets()

        elif choice == "4":
            update_ticket()

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")


menu()