def book_seat(booked_seats, seat_number, total_seats):
    if seat_number in booked_seats:
        return f"Seat {seat_number} is already booked!"
    elif seat_number > total_seats or seat_number < 1:
        return f"Invalid seat number. Please choose a seat between 1 and {total_seats}."
    else:
        booked_seats.append(seat_number)
        return f"Seat {seat_number} has been successfully booked."

def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        return f"Seat {seat_number} has been successfully canceled."
    else:
        return f"Seat {seat_number} was not booked."

def get_available_seats(total_seats, booked_seats):
    available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return available_seats

total_seats = int(input("Enter the total number of seats: "))
booked_seats = list(map(int, input(f"Enter the initially booked seats (separated by space): ").split()))

while True:
    print("\nOptions:")
    print("1. Book a seat")
    print("2. Cancel a seat")
    print("3. View available seats")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        book_seat_number = int(input("Enter the seat number to book: "))
        print(book_seat(booked_seats, book_seat_number, total_seats))
    
    elif choice == '2':
        cancel_seat_number = int(input("Enter the seat number to cancel: "))
        print(cancel_seat(booked_seats, cancel_seat_number))
    
    elif choice == '3':
        available_seats = get_available_seats(total_seats, booked_seats)
        print(f"Available seats: {available_seats}")
    
    elif choice == '4':
        print("Exiting the system.")
        break
    
    else:
        print("Invalid choice. Please choose a valid option.")
