import random

# Total seats
TOTAL_SEATS = 50

# Data storage
available_seats = list(range(1, TOTAL_SEATS + 1))
bookings = {}  # booking_id: details


def generate_booking_id():
    return "BID" + str(random.randint(1000, 9999))


def check_availability():
    print("\nAvailable Seats:", len(available_seats))
    print(available_seats)


def book_ticket():
    if not available_seats:
        print("No seats available!")
        return

    name = input("Enter your name: ")
    age = input("Enter your age: ")

    seat = available_seats.pop(0)
    booking_id = generate_booking_id()

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat
    }

    print("\nTicket Booked Successfully!")
    print(f"Booking ID: {booking_id}")
    print(f"Seat Number: {seat}")


def view_ticket():
    booking_id = input("Enter Booking ID: ")

    if booking_id in bookings:
        details = bookings[booking_id]
        print("\nTicket Details:")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Seat: {details['seat']}")
    else:
        print("Invalid Booking ID!")


def cancel_ticket():
    booking_id = input("Enter Booking ID to cancel: ")

    if booking_id in bookings:
        seat = bookings[booking_id]["seat"]
        available_seats.append(seat)
        available_seats.sort()

        del bookings[booking_id]

        print("Ticket Cancelled Successfully!")
    else:
        print("Invalid Booking ID!")


def menu():
    while True:
        print("\n--- Ticket Booking System ---")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_availability()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            view_ticket()
        elif choice == '4':
            cancel_ticket()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
