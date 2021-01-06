class Flight():
    def __init__(self, _capacity):
        self.capacity= _capacity
        self.passenger=[]
    def add_passenger(self,name):
        if not self.open_seats():
            return false
        self.passengers.append(name)
        return true
    def open_seats(self):
        return self.capacity - len(self.passengers)

    flight = Flight(3)

    people = ["harry","don","raon and jd","raon husband"]
    for peoples in people:
        success = Flight.add_passenger(peoples)
    if success :
        print(f"we added {peoples} to flight sccessfully.")
    else:
        print(f"sorry {peoples} flight is full")
