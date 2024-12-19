# Hotel-Booking-System-with-Credit-Card-Validation
This project implements a hotel booking system using Python. It includes functionalities for checking room availability, validating credit card details, and generating a booking ticket. The system integrates data from CSV files for hotels, credit card information, and security credentials.
1. Hotel Management

    Class: Hotels
        Represents a hotel object with attributes like id and name.
        Provides methods:
            book(): Updates the hotel status to "not available" after a booking.
            available(): Checks the availability of the hotel.

2. Reservation System

    Class: Reservation
        Represents a customer reservation.
        Includes generate_ticket() method to create a ticket with customer and hotel details.

3. Credit Card Validation

    Class: CreditCard
        Represents a credit card object.
        Validates credit card details like number, expiration date, holder name, and CVC against data in cards.csv.

4. Secure Credit Card Verification

    Class: SecureCreditCard (inherits from CreditCard)
        Adds a security layer with password-based authentication from card_security.csv.

How It Works

  Hotel Selection:
      Users input a hotel ID to check availability.
      If the hotel is available, the booking process begins.

  Credit Card Validation:
      Users provide credit card details, which are verified against stored records in cards.csv.

  Secure Authentication:
      A password-based authentication step validates the user via card_security.csv.

  Booking Confirmation:
      If validation and authentication succeed, the hotel is booked, and a ticket is generated with the customer's name and hotel details.

Data Files

  otels.csv: Contains hotel information such as ID, name, and availability status.
  cards.csv: Stores valid credit card details (number, expiration, holder, and CVC).
  card_security.csv: Contains card numbers and associated passwords for secure authentication.

Example Usage

  Run the Script:

    python hotel_booking.py

Follow Prompts:

  Input the hotel ID to check availability.
  Provide credit card details and password for validation.
  If successful, the system confirms the booking and displays the ticket
