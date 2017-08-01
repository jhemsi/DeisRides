"""
Welcome to DeisRides! This Program creates a list of rides student drivers are currently offering to other students.
Drivers are directed to input their contact and ride information into the available rides list called "drivers".
However, Riders will only be able to view the entire list of available rides, or filter this list by desired location.
"""

drivers = [
        {'first_name':"Bob", 'last_name':"Hicks", 'email':"bhicks@brandeis.edu", 'phone_number':"7777777777", 'start_location': "5. Main Street Marketplace", 'destination': "1. Brandeis University Admissions Bus Stop", 'date': "01/21/1995", 'time': "12:30", 'seats': 3},
        {'first_name':"Sara", 'last_name':"Smith", 'email':"ssmith@brandeis.edu", 'phone_number':"5555555555", 'start_location': "10. South Station", 'destination': "3. Boston Children Hospital", 'date': "02/22/2017", 'time': "18:24", 'seats': 2},
        {'first_name':"Phil", 'last_name':"Phillips", 'email':"pphillips@brandeis.edu", 'phone_number':"3333333333", 'start_location': "1. Brandeis University Admissions Bus Stop", 'destination': "5. Main Street Marketplace", 'date': "06/01/2001", 'time': "09:00", 'seats': 1}
        ]

place = {1:"1. Brandeis University Admissions Bus Stop",
        2:"2. Village Market South Street",
        3:"3. Boston Children Hospital",
        4:"4. Walgreens Weston Street",
        5:"5. Main Street Marketplace",
        6:"6. Hannaford Supermarket",
        7:"7. Merc Apartment Complex",
        8:"8. Cronins Apartment Complex",
        9:"9. Riverside Station",
        10:"10. South Station",
        11:"11. Logan International Airport"}

def location(x):
    """
    This function ensures that drivers can only chose locations from the above list of eleven places.
    If the user choses a number that does not correspond to said list, then he/she will be informed that this location is not offered.
    """

    if x < 12 and x >= 1:
        return (place[x])
    else:
        print("Sorry, but that location is not offered.")
        return False

def seats_in_car(s):
    """
    This function acts as an algorithm to subtract one (the driver) from the total number of seats in car.
    This will inform riders how many seats are available in the car.
    """

    return s-1

def new_carpool():
    """
    This function gathers all information from drivers needed to create new trips.
    It also arranges said information so that it is easiest to read.
    If you notice, all possible start locations and final destinations are already set in a predetermined list users can choose from.
    Our global drivers variable ensures that this information is stored in the list.
    All information requires user prompted input.
    """

    global drivers

    #user input for name, email, and phone number
    driverInfo = {'first_name':"", 'last_name':"", 'email':"", 'phone_number':"", 'start_location': "", 'destination': "", 'date': "", 'time': "", 'seats': 0}
    driverInfo['first_name'] = input("Enter your first name: ")
    driverInfo['last_name'] = input("Enter your last name: ")
    driverInfo['email'] = input("Enter your email address: ")
    driverInfo['phone_number'] = input("Enter your phone number: ")

    for x in range (1,12):
        print (place[x])

    #user input for start location, destination, date, time, and number of seats available in vehicle
    driverInfo['start_location'] = location(int(input("Please enter the number above that corresponds to your start location: ")))
    driverInfo['destination'] = location(int(input("Please enter the number above that corresponds to your final destination: ")))
    driverInfo['date'] = input("Please enter the date you will be driving using the format MM/DD/YYYY: ")
    driverInfo['time'] = input("Please enter your start time for the ride using the military clock format 00:00: ")
    driverInfo['seats'] = seats_in_car(int(input("Please enter the number of total seats in your car: "))) #program will automatically subtract one seat for the driver
    drivers.append(driverInfo)

    print (driverInfo)
    print("Above you will see your new trip. This information has automatically been added to the list of available rides. If a student is interested in this ride, then he/she contact you directly. Thank you!")
    return driverInfo

def filterLocation(destination):
    """
    This function works as a list comprehension to filter the list of all available rides by final destination.
    Riders will be able to view rides that only pertain to their needs by utilizing this function.
    """

    filteredList = [x for x in drivers if x['destination'] == destination]
    for x in filteredList:
        print(x)

def deisRide():
    """
    This is the program's main function,
    which works to differentiate between drivers and riders once the application in launched,
    and direct them to the appropriate next steps.
    """

    users = {}
    x = input("Welcome to DeisRides! Are you a driver or rider? ")
    if x == "driver":
        new_carpool()
    else:
        for x in range (1,12):
            print (place[x])

        user_input = int(input("Please enter the number above that corresponds to your final destination for a filtered list of rides "))
        destination = place[user_input]
        filterLocation(destination)


while True:
    deisRide()
