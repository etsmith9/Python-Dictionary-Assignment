#question2

def new_ticket(Tic_num, Customer_name, Issue):
    service_tickets[Tic_num] = {"Customer": Customer_name, "Issue": Issue, "Status" : "open"}
    print(f"New Ticket added: {Tic_num} - {Issue} - Status: Open")

def update_status(Tic_num, new_status):
    if Tic_num in service_tickets:
        service_tickets[Tic_num]["Status"] = new_status
        print(f"Status for {Tic_num} has been updated to {new_status}.")
    else:
        print(f"Ticket number {Tic_num} does not exist.")

def display_tickets(service_tickets):
    for Tic_num, details in service_tickets.items():
        print(f" Ticket: {Tic_num} - Customer Name: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")



service_tickets = {
    "001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

while True:
    print("\n Customer Service Ticket Management System")
    print("1. Add a Ticket\n2. Update the Status of a Ticket\n3. Display Existing Tickets\n4. Exit")
    choice = input("Please enter a selection:  ")

    if choice == '1':
        Tic_num = input("Please enter a ticket number:  (ex.009)")
        Customer_name = input("Please enter your name:  ")
        Issue = input("Please enter your issue:  ")
        new_ticket(Tic_num, Customer_name, Issue)
    elif choice == '2':
        Tic_num = input("Please enter the ticket number:  (ex.009) ")
        new_status = input("Please enter the updated status: (open/closed) ")
        update_status(Tic_num, new_status)
    elif choice == '3':
        display_tickets(service_tickets)
    elif choice == '4':
        print("Exiting System")
        break
    else:
        print("/n Your selection is not valid, please try again.")