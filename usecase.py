import sys
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Flight:

    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")
    return wrapper


@announce
def hello():
    print("Hello, world!")

movies = [
    {"title": "Green Book", "year": 2018},
    {"title": "The Shape of Water", "year": 2017},
    {"title": "Moonlight", "year": 2016},
    {"title": "Spotlight", "year": 2015},
    {"title": "Birdman", "year": 2014},
    {"title": "12 Years a Slave", "year": 2013}
]

movies.sort(key=lambda movie: movie["year"])

for movie in movies:
    print("{title} was released in {year}".format(**movie))

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
    sys.exit(1)

print(f"x / y = {result}")


hello()

flight = Flight(capacity=3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight.")
    else:
        print(f"No available seats for {person}.")

p = Point(3, 5)
print(p.x)
print(p.y)
