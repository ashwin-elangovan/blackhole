# Give the design of an automated valet parking system with the following specifications:
# There are 3 parking areas (each of different sizes) for 3 different vehicle sizes - small, medium and large.
# Small one can accommodate only small vehicles, medium can accommodate small and medium vehicles and similarly for the large one.
# Design a system which issues a parking ticket to a vehicle entering the lot with the optimal parking space allotted to it. For eg., if a medium vehicle arrives and both medium and large parking areas have vacant spaces, the vehicle should be allotted the medium slot.
# Also design a syntax for the token ID which is generated when each vehicle enters the lot. The ID should be uniquely able to determine the details of the slot where the vehicle is parked for smooth parking and un-parking.
# Provide the class design of the same.


#########

# Amazon solution:

class Vehicle:
    def __init__(self, size):
        self.size = size

class ParkingSlot:
    def __init__(self, slot_number, area_type):
        self.slot_number = slot_number
        self.area_type = area_type
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True

    def vacate(self):
        self.is_occupied = False

    def get_ticket(self):
        return f"{self.area_type}-{self.slot_number}"

class ParkingArea:
    def __init__(self, area_type, total_slots):
        self.area_type = area_type
        self.available_slots = {}
        for idx in range(1, total_slots + 1):
          self.available_slots[idx] = ParkingSlot(slot_number=idx, area_type=area_type)
        self.occupied_slots = {}

    def fetch_available_slot(self):
        if len(self.available_slots) > 0:
            curr_id = next(iter(self.available_slots))
            slot = self.available_slots[curr_id]
            slot.occupy()
            del self.available_slots[curr_id]
            self.occupied_slots[curr_id] = slot
            return slot
        return None

    def vacate_slot(self, id):
        if id not in self.occupied_slots:
            return None
        slot = self.occupied_slots[id]
        self.available_slots[id] = slot
        slot.vacate()
        del self.occupied_slots[id]
        return True

class AutomatedValetParkingSystem:
    def __init__(self):
        self.small_area = ParkingArea(area_type='S', total_slots=1)
        self.medium_area = ParkingArea(area_type='M', total_slots=2)
        self.large_area = ParkingArea(area_type='L', total_slots=3)

    def park_vehicle(self, vehicle):
        vehicle_size = vehicle.size.lower()
        if vehicle_size not in {'small', 'medium', 'large'}:
            return "Invalid vehicle size."

        areas = []
        if vehicle_size == 'small':
          areas = [self.small_area, self.medium_area, self.large_area]
        elif vehicle_size == 'medium':
          areas = [self.medium_area, self.large_area]
        else:
            areas = [self.large_area]

        for area in areas:
          slot = area.fetch_available_slot()
          if slot:
            return slot.get_ticket()

        return "No available slots."

    def un_park_vehicle(self, token_id):
        try:
            area_type, slot_number = token_id.split('-')
        except:
           return "Invalid token ID."

        if area_type == 'S':
            area = self.small_area
        elif area_type == 'M':
            area = self.medium_area
        else:
            area = self.large_area

        slot = area.vacate_slot(int(slot_number))
        if slot:
            return f"Vehicle successfully un-parked. Token ID: {token_id}"
        return "Error in un-parking"

# Example usage:
valet_system = AutomatedValetParkingSystem()
small_car = Vehicle(size='small')
token_id = valet_system.park_vehicle(small_car)
print(f"Small car parked. Token ID: {token_id}")
small_car2 = Vehicle(size='small')
token_id_2 = valet_system.park_vehicle(small_car2)
print(f"Small car2 parked. Token ID: {token_id_2}")
small_car3 = Vehicle(size='small')
token_id = valet_system.park_vehicle(small_car3)
print(f"Small car2 parked. Token ID: {token_id}")
small_car4 = Vehicle(size='small')
token_id = valet_system.park_vehicle(small_car4)
print(f"Small car2 parked. Token ID: {token_id}")
print(valet_system.un_park_vehicle(token_id_2))
small_car5 = Vehicle(size='small')
token_id_5 = valet_system.park_vehicle(small_car5)
print(f"Small car2 parked. Token ID: {token_id_5}")

#############

class ParkingArea:
    def __init__(self, size):
        self.size = size
        self.available_slots = size
        self.occupied_slots = set()

    def has_space(self):
        return self.available_slots > 0

    def park_vehicle(self, vehicle):
        if not self.has_space():
            return False
        self.available_slots -= 1
        self.occupied_slots.add(vehicle)
        return True

    def vacate_slot(self, vehicle):
        if vehicle in self.occupied_slots:
            self.available_slots += 1
            self.occupied_slots.remove(vehicle)
            return True
        return False

class Vehicle:
    def __init__(self, size):
        self.size = size

class ParkingTicket:
    def __init__(self, vehicle, parking_area):
        self.vehicle = vehicle
        self.parking_area = parking_area
        self.token_id = self.generate_token_id()

    def generate_token_id(self):
        # Example syntax: <vehicle_size>_<parking_area_size>_<unique_number>
        return f"{self.vehicle.size}_{self.parking_area.size}_{self.token_id}"

class AutomatedValetParkingSystem:
    def __init__(self):
        self.small_parking_area = ParkingArea("small")
        self.medium_parking_area = ParkingArea("medium")
        self.large_parking_area = ParkingArea("large")

    def issue_ticket(self, vehicle):
        if vehicle.size == "small":
            if self.small_parking_area.has_space():
                self.small_parking_area.park_vehicle(vehicle)
                return ParkingTicket(vehicle, self.small_parking_area)
        elif vehicle.size == "medium":
            if self.medium_parking_area.has_space():
                self.medium_parking_area.park_vehicle(vehicle)
                return ParkingTicket(vehicle, self.medium_parking_area)
            elif self.large_parking_area.has_space():
                self.large_parking_area.park_vehicle(vehicle)
                return ParkingTicket(vehicle, self.large_parking_area)
        elif vehicle.size == "large":
            if self.large_parking_area.has_space():
                self.large_parking_area.park_vehicle(vehicle)
                return ParkingTicket(vehicle, self.large_parking_area)
        return None

    def release_ticket(self, ticket):
        if ticket.vehicle.size == "small":
            return self.small_parking_area.vacate_slot(ticket.vehicle)
        elif ticket.vehicle.size == "medium":
            return self.medium_parking_area.vacate_slot(ticket.vehicle)
        elif ticket.vehicle.size == "large":
            return self.large_parking_area.vacate_slot(ticket.vehicle)

# Example usage
automated_valet_parking_system = AutomatedValetParkingSystem()

# Vehicle arrives
vehicle1 = Vehicle("medium")
ticket1 = automated_valet_parking_system.issue_ticket(vehicle1)
print(ticket1.token_id)  # This will print the token ID for the issued parking ticket

# Vehicle leaves
automated_valet_parking_system.release_ticket(ticket1)


from enum import Enum

# Vehicle type class for what all type of vehicles can come for parking
class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    BUS = 3

# Vehicle class for license plate, company name and their type
class Vehicle:
    def __init__(self, licensePlate, companyName, type_of_vehicle):
        self.licensePlate = licensePlate
        self.companyName = companyName
        self.type_of_vehicle = type_of_vehicle

    def getType(self):
        return self.type_of_vehicle

    '''overwrite __eq__ methods to correctly check if two vehicle objects are same. Otherwise, they will be
    checked at hashcode level not at content level.'''

    def __eq__(self, other):
        if other is None:
            return False
        if self.licensePlate != other.licensePlate:
            return False
        if self.companyName != other.companyName:
            return False
        if self.type_of_vehicle != other.type_of_vehicle:
            return False
        return True


# Car class inherited from Vehicle class for license plate, company name and their type
class Car(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.CAR)


# Bike class inherited from Vehicle class for license plate, company name and their type
class Bike(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.BIKE)


# Bus class inherited from Vehicle class for license plate, company name and their type
class Bus(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.BUS)


class Slots:
    def __init__(self, lane, spotNumber, type_of_vehicle):
        # self.level = level
        self.lane = lane
        self.spotNumber = spotNumber
        self.vehicle = None
        self.type_of_vehicle = type_of_vehicle

    def isAvailable(self):
        return self.vehicle == None

    def park(self, vehicle):
        if vehicle.type_of_vehicle == self.type_of_vehicle:
            self.vehicle = vehicle
            return True
        else:
            return False

    def removeVehicle(self):
        self.vehicle = None
        return self.vehicle

    def getVehicle(self):
        return self.vehicle


'''Level class - Each level is an independent entity with a floor number, its lanes and the slots within it.
The number of lanes are designed based on the number of slots. 10 slots make one lane'''

class Levels:
    def __init__(self, floorNumber, no_of_slots):
        self.floorNumber = floorNumber
        self.spots_per_lane = 10
        self.lanes = no_of_slots / self.spots_per_lane
        self.parkingSlots = set()
        self.availableSpots = []

        # Check available spots in a lane
        for lane in range(int(self.lanes)):
            for i in range(self.spots_per_lane):
                import random
                # We will randomly assign a type to each slot.
                self.availableSpots.append(Slots(lane, i, random.choice(list(VehicleType))))
                # self.availableSpots.append(Slots(lane, i, type_of_vehicle))

    # Park vehicle is spot is available
    def park(self, vehicle):
        for slot in self.availableSpots:
            if slot.park(vehicle):
                return True
        return False

    # Remove vehicle from a spot
    def remove(self, vehicle):
        for spot in self.availableSpots:
            if spot.getVehicle() == vehicle:
                spot.removeVehicle()
                return True
        return False

    # Company name for the vehicle parked at the available spots
    def companyParked(self, companyName):
        all_vehicles = []
        for spot in self.availableSpots:
            vehicle = spot.getVehicle()
            if (vehicle is not None) and (vehicle.companyName == companyName):
                all_vehicles.append(vehicle)
                #print(all_vehicles)
        return all_vehicles


# A parking lot is made up of 'n' number of levels/floors and 'm' number of slots per floor.
class ParkingLot:
    def __init__(self, no_of_floor, no_of_slot):
        self.levels = []
        for i in range(no_of_floor):
            self.levels.append(Levels(i, no_of_slot))

    # This operation inserts a vehicle accordingly, also takes care of what company vehicle it is.
    def parkVehicle(self, vehicle):
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False

    # This operation exits a vehicle 'C' in a level 'm'.
    def leaveOperation(self, vehicle):
        for level in self.levels:
            if level.remove(vehicle):
                return True

    # This operation allows the user to view the list of vehicles parked for a particular company.
    def companyParked(self, companyName):
        all_vehicles = []
        for level in self.levels:
            all_vehicles.extend(level.companyParked(companyName))
        return all_vehicles

