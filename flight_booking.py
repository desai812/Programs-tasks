# Task 04 - Flight Booking Console Application (OOP) - Python
from abc import ABC, abstractmethod


def money(amount):
    """Format an amount like 7,200 (no decimals if it is a whole number)."""
    if amount == int(amount):
        return f"Rs.{int(amount):,}"
    return f"Rs.{amount:,.2f}"


# ---------------------------------------------------------------
# ABSTRACTION + INHERITANCE + POLYMORPHISM: Passenger classes
# ---------------------------------------------------------------
class Passenger(ABC):
    """Base class (abstract). Every passenger type must define its own discount."""

    def __init__(self, name, age):
        self.__name = name          # private fields (encapsulation)
        self.__age = age

    # Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @abstractmethod
    def get_discount_percent(self):
        """Common discount contract - each subclass overrides this."""
        pass

    @abstractmethod
    def get_type(self):
        pass

    def calculate_discount(self, subtotal):
        # Same method call works for every passenger type (polymorphism)
        return subtotal * self.get_discount_percent() / 100


class RegularPassenger(Passenger):
    def get_discount_percent(self):
        return 0

    def get_type(self):
        return "Regular"


class StudentPassenger(Passenger):
    def get_discount_percent(self):
        return 10

    def get_type(self):
        return "Student"


# ---------------------------------------------------------------
# CLASS: Flight (encapsulates its own seat count)
# ---------------------------------------------------------------
class Flight:
    def __init__(self, code, airline, source, destination, seats, base_fare):
        self.__code = code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__available_seats = seats
        self.__base_fare = base_fare

    def get_code(self):
        return self.__code

    def get_airline(self):
        return self.__airline

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_available_seats(self):
        return self.__available_seats

    def get_base_fare(self):
        return self.__base_fare

    def has_seats(self, tickets):
        return tickets <= self.__available_seats

    def reserve_seats(self, tickets):
        """Only way to change the seat count - used after a booking is confirmed."""
        if self.has_seats(tickets):
            self.__available_seats -= tickets
            return True
        return False


# ---------------------------------------------------------------
# CLASS: Booking (one confirmed booking)
# ---------------------------------------------------------------
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets, subtotal, discount, final_amount):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets
        self.subtotal = subtotal
        self.discount = discount
        self.final_amount = final_amount


# ---------------------------------------------------------------
# CLASS: FlightBookingSystem (controls the whole application)
# ---------------------------------------------------------------
class FlightBookingSystem:
    def __init__(self):
        # Data is kept in program memory only
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB201", "Sky Jet", "Mumbai", "Bengaluru", 30, 5000),
            Flight("PH301", "Indigo Wings", "Pune", "Hyderabad", 15, 3500),
        ]
        self.bookings = []
        self.next_booking_number = 1001

    # --- display all flights ---
    def display_flights(self):
        print("\n----- AVAILABLE FLIGHTS -----")
        print(f"{'Code':<7}{'Airline':<15}{'Source':<10}{'Destination':<13}{'Seats':<7}{'Base Fare'}")
        for flight in self.flights:
            print(f"{flight.get_code():<7}{flight.get_airline():<15}{flight.get_source():<10}"
                  f"{flight.get_destination():<13}{flight.get_available_seats():<7}"
                  f"{money(flight.get_base_fare())}")

    # --- find a flight by its code ---
    def find_flight(self, code):
        for flight in self.flights:
            if flight.get_code() == code:
                return flight
        return None

    # --- validate every booking detail before anything changes ---
    def validate_booking_details(self, code, name, age_text, type_text, tickets_text):
        """Returns (error_message, flight, passenger, tickets). error is None if all OK."""
        flight = self.find_flight(code)
        if flight is None:
            return "Flight code does not exist.", None, None, 0

        if name.strip() == "":
            return "Passenger name cannot be blank.", None, None, 0

        try:
            age = int(age_text)
        except ValueError:
            return "Age must be a number.", None, None, 0
        if age <= 0:
            return "Age must be greater than 0.", None, None, 0

        passenger_type = type_text.strip().lower()
        if passenger_type == "regular":
            passenger = RegularPassenger(name.strip(), age)
        elif passenger_type == "student":
            passenger = StudentPassenger(name.strip(), age)
        else:
            return "Passenger type must be Regular or Student.", None, None, 0

        try:
            tickets = int(tickets_text)
        except ValueError:
            return "Number of tickets must be a number.", None, None, 0
        if tickets <= 0:
            return "Number of tickets must be greater than 0.", None, None, 0

        if not flight.has_seats(tickets):
            return "Not enough seats available.", None, None, 0

        return None, flight, passenger, tickets

    # --- calculate subtotal, discount and final amount ---
    def calculate_fare(self, flight, passenger, tickets):
        subtotal = flight.get_base_fare() * tickets
        discount = passenger.calculate_discount(subtotal)   # polymorphic call
        final_amount = subtotal - discount
        return subtotal, discount, final_amount

    # --- confirm: reduce seats, create booking, store in memory ---
    def confirm_booking(self, flight, passenger, tickets):
        subtotal, discount, final_amount = self.calculate_fare(flight, passenger, tickets)
        flight.reserve_seats(tickets)
        booking_id = "BK" + str(self.next_booking_number)
        self.next_booking_number += 1
        booking = Booking(booking_id, flight, passenger, tickets, subtotal, discount, final_amount)
        self.bookings.append(booking)
        return booking

    # --- show a booking summary ---
    def display_summary(self, booking):
        flight = booking.flight
        passenger = booking.passenger
        print("Booking ID:", booking.booking_id)
        print(f"Flight: {flight.get_code()} | {flight.get_source()} to {flight.get_destination()}")
        print("Passenger:", passenger.get_name())
        print("Age:", passenger.get_age())
        print("Passenger type:", passenger.get_type())
        print("Tickets:", booking.tickets)
        print("Base fare per ticket:", money(flight.get_base_fare()))
        print("Subtotal:", money(booking.subtotal))
        print(f"{passenger.get_type()} discount ({passenger.get_discount_percent()}%):",
              money(booking.discount))
        print("Final amount:", money(booking.final_amount))

    # --- menu option 2: book a flight ---
    def book_flight(self):
        code = input("Enter flight code: ").strip().upper()
        name = input("Enter passenger name: ")
        age_text = input("Enter age: ").strip()
        type_text = input("Passenger type (Regular/Student): ")
        tickets_text = input("Enter number of tickets: ").strip()

        error, flight, passenger, tickets = self.validate_booking_details(
            code, name, age_text, type_text, tickets_text)

        if error is not None:
            print("Booking failed:", error)
            print("No booking was created. Available seats remain unchanged.")
            return

        booking = self.confirm_booking(flight, passenger, tickets)
        print("\nBooking confirmed!")
        self.display_summary(booking)

    # --- menu option 3: view the most recent booking ---
    def view_booking(self):
        if len(self.bookings) == 0:
            print("No booking found. Please book a flight first (option 2).")
        else:
            print("\n----- MOST RECENT BOOKING -----")
            self.display_summary(self.bookings[-1])

    # --- main menu loop ---
    def run(self):
        print("Welcome to Kiran Air Booking")
        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()
