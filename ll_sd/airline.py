class Airline:
    def __init__(self, name=None):
        self._name = name
        self._booked = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def book(self, passenger, plane, cls=None):
        while cls not in ['first class', 'coach']:

            cls = input("Please pick a seat: First class or Coach ").lower()

            if cls not in ['first class', 'coach']:
                print("Please select either from 'first class' or 'coach'")
                pass
        if cls == 'first class':
            first_class = ([(number, seat) for number, seat in enumerate(plane.capacity)][0:10])
            choice = None
            while choice not in range(10):
                try:
                    choice = int(input(f"Please select a number between 0 and 9 for your seats: "))
                except ValueError:
                    print("Please select a valid number between 0 and 9")
                if choice in self._booked:
                    print(f"That seat is taken please choose another seat\n"
                          f"These seats are booked: {self._booked}")
                    choice = None
            for seat in first_class:
                if seat[0] == choice:
                    plane.capacity[seat[1]] = passenger
                    passenger._balance = passenger._balance - seat[1].price
                    self._booked.append(seat[0])
                    passenger._assignment = seat[1].tier + f" seat {seat[0]}"
        else:
            coach = ([(number, seat) for number, seat in enumerate(plane.capacity)][10:50])
            choice = None
            while choice not in range(10, 50):
                try:
                    choice = int(input(f"Please select a number between 10 and 50 for your seats: "))
                except ValueError:
                    print("Please select a valid number between 10 and 50")
                if choice in self._booked:
                    print(f"That seat is taken please choose another seat\n"
                          f"These seats are booked: {self._booked}")
                    choice = None
            for seat in coach:
                if seat[0] == choice:
                    plane.capacity[seat[1]] = passenger
                    passenger._balance = passenger._balance - seat[1].price
                    self._booked.append(seat[0])
                    passenger._assignment = seat[1].tier + f" seat {seat[0]}"

    def refund(self, passenger, plane):
        for i, (seat, person) in enumerate(plane.capacity.items()):
            if person == passenger:
                plane.capacity[seat] = None
                passenger._balance = passenger._balance + seat.price
                passenger._assignment = None
                self._booked.remove(i)


class Passenger:
    def __init__(self, balance=1000, assignment=None):
        self._balance = balance
        self._assignment = assignment

    def get_balance(self):
        return self._balance

    def get_assignment(self):
        return self._assignment


class Seat:
    def __init__(self):
        pass


class FirstClass(Seat):
    def __init__(self):
        super().__init__()
        self.tier = 'First Class'
        self.price = 500

class Coach(Seat):
    def __init__(self):
        super().__init__()
        self.tier = 'Coach'
        self.price = 100


class Plane:
    def __init__(self):
        self.capacity = {}
        temp_capacity = []  # Create a temporary list to append seats into ( this will be the seats in the airplane)
        for i in range(10):  # first 10 seats are first class
            temp_capacity.append(FirstClass())
        for i in range(10, 50):  # last 40 seats are coach class
            temp_capacity.append(Coach())
        for seat in temp_capacity:
            self.capacity[seat] = None  # Each seat has no value(person) assigned

    def view_plane(self):
        for i, k in self.capacity.items():
            print(f"{i} : {k}")

    def get_available_seats(self):
        count = 0
        for value in self.capacity.values():
            if value is None:
                count += 1
        return count

plane = Plane()
p = Passenger()
p2 = Passenger()
p3 = Passenger()
airline = Airline()

# plane.view_plane()
airline.book(p, plane)
airline.book(p2, plane)
# print(airline._booked)
print(f"passenger 1 balance: {p.get_balance()}\n"
      f"passenger 1 assignment: {p.get_assignment()}\n"
      f"passenger 2 balance: {p2.get_balance()}\n"
      f"passenger 2 assignment: {p2.get_assignment()}\n"
      f"Number of seats available: {plane.get_available_seats()}\n"
      f"Number of seats booked: {len(airline._booked)}")
# plane.view_plane()
airline.book(p3, plane)
# plane.view_plane()
print("--------------")
# print(airline._booked)
print(f"passenger 1 balance: {p.get_balance()}\n"
      f"passenger 1 assignment: {p.get_assignment()}\n"
      f"passenger 2 balance: {p2.get_balance()}\n"
      f"passenger 2 assignment: {p2.get_assignment()}\n"
      f"passenger 3 balance: {p3.get_balance()}\n"
      f"passenger 3 assignment: {p3.get_assignment()}\n"
      f"Number of seats available: {plane.get_available_seats()}\n"
      f"Number of seats booked: {len(airline._booked)}")
print("----------------")
airline.refund(p2, plane)
# print(airline._booked)
print(f"passenger 1 balance: {p.get_balance()}\n"
      f"passenger 1 assignment: {p.get_assignment()}\n"
      f"passenger 2 balance: {p2.get_balance()}\n"
      f"passenger 2 assignment: {p2.get_assignment()}\n"
      f"passenger 3 balance: {p3.get_balance()}\n"
      f"passenger 3 assignment: {p3.get_assignment()}\n"
      f"Number of seats available: {plane.get_available_seats()}\n"
      f"Number of seats booked: {len(airline._booked)}")
