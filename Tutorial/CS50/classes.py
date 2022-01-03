# Most important key technique that python supports is OOP.
# __init__(self): constructor.
# self: this

class Flight:
    # This init method construct an object when it is created.
    # It is basically a magic method.
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if not self.open_seats():
            return False;
        self.passengers.append(name)
        return True;


flight = Flight(3)
print(type(flight))
persons = ["Jhon", "Tiku", "Kawla", "Misus", "Okaol"]
for i in persons:
    success = flight.add_passenger(i)
    if success:
        print(f'Added {i}.')
    else:
        print(f'No seat available for {i}.')