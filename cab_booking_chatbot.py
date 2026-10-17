# Task 02 - Cab Booking Chatbot (Menu, Fare & OTP Rules) - Python
import random

# Predefined cab types and rates (Rs. per km)
CAB_NAMES = {"1": "Auto", "2": "Sedan", "3": "SUV"}
CAB_RATES = {"1": 12, "2": 18, "3": 25}

# Predefined routes: (source, destination, fixed distance in km)
ROUTES = {
    "1": ("Pune Station", "Shivajinagar", 5),
    "2": ("Swargate", "Kothrud", 8),
    "3": ("Hinjawadi", "Wakad", 10),
}

print("=== Welcome to the Cab Booking Chatbot ===")

while True:
    # Step 1: Main menu
    print("\n----- MAIN MENU -----")
    print("1. Book Ride")
    print("2. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "2":
        # Step 7: Exit
        print("Thank you for using the Cab Booking Chatbot. Goodbye!")
        break

    elif choice == "1":
        # Step 2: Choose cab type
        print("\nChoose your cab type:")
        print("1. Auto  (Rs.12/km)")
        print("2. Sedan (Rs.18/km)")
        print("3. SUV   (Rs.25/km)")
        cab_choice = input("Enter cab choice: ").strip()

        if cab_choice not in CAB_RATES:
            print("Invalid cab choice! Returning to main menu.")
            continue

        # Step 3: Choose route
        print("\nAvailable routes:")
        print("1. Pune Station -> Shivajinagar (5 km)")
        print("2. Swargate -> Kothrud (8 km)")
        print("3. Hinjawadi -> Wakad (10 km)")
        route_choice = input("Enter route number: ").strip()

        if route_choice not in ROUTES:
            print("Invalid route choice! Returning to main menu.")
            continue

        cab_name = CAB_NAMES[cab_choice]
        rate = CAB_RATES[cab_choice]
        source, destination, distance = ROUTES[route_choice]

        # Step 4: Calculate fare = rate per km x distance
        fare = rate * distance

        print("\n----- BOOKING SUMMARY -----")
        print("Cab Type    :", cab_name)
        print("Source      :", source)
        print("Destination :", destination)
        print("Distance    :", distance, "km")
        print("Rate        : Rs.", rate, "per km")
        print("Total Fare  : Rs.", fare, "(", distance, "x", rate, ")")

        # Step 5: Cancellation is allowed only BEFORE the OTP is shared
        print("\nCancellation is possible only before the OTP is shared.")
        while True:
            print("1. Confirm & Share OTP")
            print("2. Cancel Ride")
            confirm = input("Enter your choice: ").strip()

            if confirm == "1":
                # Step 6: Generate a 4-digit OTP and lock the ride
                otp = random.randint(1000, 9999)
                print("\nYour OTP is:", otp, "(shared with you)")
                print("NOTE: The OTP has been shared, so this ride can NO LONGER be cancelled.")
                print("Booking confirmed! Your", cab_name, "is on the way.")
                break

            elif confirm == "2":
                print("\nRide cancelled. No OTP was shared. Returning to main menu.")
                break

            else:
                print("Invalid choice! Please enter 1 or 2.")

    else:
        print("Invalid choice! Please enter 1 or 2.")
