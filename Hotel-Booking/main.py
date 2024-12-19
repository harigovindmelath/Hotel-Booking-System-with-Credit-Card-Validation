import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_security = pd.read_csv('card_security.csv',
                          sep=',',
                          skipinitialspace=True, dtype=str)


class Hotels:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotel_csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class Reservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate_ticket(self):
        content = f"""
        Thank you for booking!!
        Here is your booking details:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def security(self, given_password):
        password = df_security.loc[df_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(df)
hotel_Id = input("Enter the id of the hotel: ")
hotel = Hotels(hotel_Id)

if hotel.available():
    card_number = input("Enter your credit card number: ")
    credit_card = SecureCreditCard(number=card_number)
    exp = input("Enter your expiration date: ")
    hold = input("Enter the account holder name: ")
    cvc_in = input("Enter the cvc number: ")
    if credit_card.validate(expiration=exp, holder=hold, cvc=cvc_in):
        password1 = input("Enter your password: ")
        if credit_card.security(given_password=password1):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = Reservation(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate_ticket())
        else:
            print("Authentication failed")
    else:
        print("Invalid card details. Try again")
else:
    print("Sorry, hotel is not free")
