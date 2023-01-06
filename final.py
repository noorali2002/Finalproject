class Bus:
    def __init__(self, number_of_chairs, destination):
        self.number_of_chairs = number_of_chairs
        self.destination = destination
        self.reserved_chairs = []

    def reserve_chair(self, chair_number):
        if chair_number in self.reserved_chairs:
            print("Sorry, chair number {} is already reserved!".format(chair_number))
        elif chair_number > self.number_of_chairs:
            print("Invalid chair number")
        else:
            self.reserved_chairs.append(chair_number)
            print("Successfully reserved chair number {}".format(chair_number))

# Create the buses
bus1 = Bus(40, "New York")
bus2 = Bus(30, "Chicago")
bus3 = Bus(50, "Los Angeles")
bus4 = Bus(45, "Houston")
bus5 = Bus(35, "Miami")

# List of all the buses
buses = [bus1, bus2, bus3, bus4, bus5]

# Loop until the user exits
while True:
    # Display options
    print("Enter 1 to see the available buses")
    print("Enter 2 to see the number of available chairs in a specific bus")
    print("Enter 3 to reserve a chair in a specific bus")
    print("Enter 4 to exit")
    user_input = input("What do you want to do? ")

    # See the available buses
    if user_input == "1":
        for i, bus in enumerate(buses):
            print("{}. {}".format(i + 1, bus.destination))

    # See the number of available chairs in a specific bus
    elif user_input == "2":
        for i, bus in enumerate(buses):
            print("{}. {}".format(i + 1, bus.destination))
        bus_number = int(input("Enter the number of the bus: "))
        if bus_number > len(buses):
            print("Invalid bus number")
        else:
            bus = buses[bus_number - 1]
            available_chairs = bus.number_of_chairs - len(bus.reserved_chairs)
            print("Number of available chairs: {}".format(available_chairs))

    # Reserve a chair in a specific bus
    elif user_input == "3":
        for i, bus in enumerate(buses):
            print("{}. {}".format(i + 1, bus.destination))
        bus_number = int(input("Enter the number of the bus: "))
        if bus_number > len(buses):
            print("Invalid bus number")
        else:
            bus = buses[bus_number - 1]
            chair_number = int(input("Enter the number of the chair you want to reserve: "))
            bus.reserve_chair(chair_number)

    # Exit the program
    elif user_input == "4":
        print("Thank you for using the bus reservation system!")
        break
    else:
        print("Invalid input")