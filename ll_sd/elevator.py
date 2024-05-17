# Simple design

from enum import Enum
from heapq import heappush, heappop

class Direction(Enum):
    up = 'UP'
    down = 'DOWN'
    idle = 'IDLE'

class RequestType(Enum):
    external = 'EXTERNAL'
    internal = 'INTERNAL'

class Request:
    def __init__(self, origin, target, typeR, direction):
        self.target = target
        self.typeRequest = typeR
        self.origin = origin
        self.direction = direction

class Button:
    def __init__(self, floor):
        self.floor = floor

class Elevator:
    def __init__(self, currentFloor):
        self.direction = Direction.idle
        self.currentFloor = currentFloor
        self.upStops = [] # Priority queue for up requests
        self.downStops = [] # Priority queue for down requests

    def sendUpRequest(self, upRequest):
        """Method to handle incoming up requests"""
        if upRequest.typeRequest == RequestType.external:
            # If it's an external request, add it to the priority queue with origin as the key
            heappush(self.upStops, (upRequest.origin, upRequest.origin))

        # Add the target floor to the priority queue
        heappush(self.upStops, (upRequest.target, upRequest.origin))

    def sendDownRequest(self, downRequest):
        """Method to handle incoming down requests"""
        if downRequest.typeRequest == RequestType.external:
            # If it's an external request, add it to the priority queue with origin as the key
            heappush(self.downStops, (-downRequest.origin, downRequest.origin))

        # Add the target floor to the priority queue
        heappush(self.downStops, (-downRequest.target, downRequest.origin))

    def run(self):
        """Method to run the elevator"""
        while self.upStops or self.downStops:
            self.processRequests()

    def processRequests(self):
        """Method to process requests based on elevator direction"""
        if self.direction in [Direction.up, Direction.idle]:
            self.processUpRequests()
            self.processDownRequests()
        else:
            self.processDownRequests()
            self.processUpRequests()

    def processUpRequests(self):
        """Method to process up requests"""
        while self.upStops:
            target, origin = heappop(self.upStops)

            self.currentFloor = target

            if target == origin:
                print("Stopping at floor {} to pick up people".format(target))
            else:
                print("Stopping at floor {} to let people out".format(target))

        if self.downStops:
            self.direction = Direction.down
        else:
            self.direction = Direction.idle

    def processDownRequests(self):
        """Method to process down requests"""
        while self.downStops:
            target, origin = heappop(self.downStops)

            self.currentFloor = target

            if abs(target) == origin:
                print("Stopping at floor {} to pick up people".format(abs(target)))
            else:
                print("Stopping at floor {} to let people out".format(abs(target)))

        if self.upStops:
            self.direction = Direction.up
        else:
            self.direction = Direction.idle


# Creating an elevator instance with initial floor 0
elevator = Elevator(0)

# Creating internal up requests
upRequest1 = Request(elevator.currentFloor, 5, RequestType.internal, Direction.up)
upRequest2 = Request(elevator.currentFloor, 3, RequestType.internal, Direction.up)

# Creating internal down requests
downRequest1 = Request(elevator.currentFloor, 1, RequestType.internal, Direction.down)
downRequest2 = Request(elevator.currentFloor, 2, RequestType.internal, Direction.down)

# Creating external up and down requests
upRequest3 = Request(4, 8, RequestType.external, Direction.up)
downRequest3 = Request(6, 3, RequestType.external, Direction.down)

# Sending requests to the elevator
elevator.sendUpRequest(upRequest1)
elevator.sendUpRequest(upRequest2)

elevator.sendDownRequest(downRequest1)
elevator.sendDownRequest(downRequest2)

elevator.sendUpRequest(upRequest3)
elevator.sendDownRequest(downRequest3)

# Running the elevator
elevator.run()

### Objects ###
# Elevator
# Buttons
# External Buttons
# Internal Buttons
# Requests
# Elevator events
# Door
# Elevator Door
# Floor Door
# Displays
# Floor Number Screen
# Floors

### Data Sturcutres ###
# upRequests priority queue
# downRequests priority queue
# Pending requests Dictionary

### Object Relationships ###
# Elevator has a Elevator Door, Internal Buttons, Floor Number screen
# Floors have floor door, floor number screen, external buttons
# Elevator Door is a door
# Internal buttons are buttons
# Floor number screens are displays

### Design Patterns ###
# Pub/Sub: Elevator is the subject and publisher, all buttons and displays sub
# elevator to figure out what to display and when to light up
# Req/Rep: Buttons send elevator request which then generates a response

### Future work ###
# Multithreading, multi elevators
# Elevator controller/strategy that can be swapped out

from enum import Enum
from abc import ABC, abstractmethod
from turtle import up

NUMBER_OF_FLOORS = 10

class DoorType(Enum):
  floor = "FLOOR"
  elevator = "ELEVATOR"

class DoorStatus(Enum):
  open = "OPEN"
  closed = "CLOSED"


class Door():

  def __init__(self,typeD, location = None, status = DoorStatus.closed):
    self.location = location
    self.typeD = typeD
    self.location = location
    self.status = status


  def open(self):
    self.status = DoorStatus.open

  def close(self):
    self.status = DoorStatus.closed


class ElevatorDoor(Door):
  def __init__(self):
    super().__init__(DoorType.elevator)


class FloorDoor(Door):
  def __init__(self,location):
    super().__init__(DoorType.floor,location)


class ButtonType(Enum):
  internal = "INTERNAL"
  external = "EXTERNAL"

class ButtonStatus(Enum):
  pressed = "PRESSED"
  unpressed = "UNPRESSED"


class Button(ABC):
  def __init__(self,typeB, status = ButtonStatus.unpressed):
    self.typeB = typeB
    self.status = status

  def press(self):
    self.status = ButtonStatus.pressed
    self.sendRequest()

  @abstractmethod
  def sendRequest(self):
    pass

  def unpress(self):
    # Pub published fulfilled requeset
    self.status = ButtonStatus.unpressed


class ElevatorGoToFloorButton(Button):
  def __init__(self, goToFloor):
    super().__init__(ButtonType.internal)
    self.goToFloor = goToFloor

  def sendRequest(self):
    if self.goToFloor > elevator.location:
      request = Request(RequestType.internal, RequestDirection.up, elevator.location,self.goToFloor)
      elevator.request(request)
    else:
      request = Request(RequestType.internal, RequestDirection.down, elevator.location,self.goToFloor)
      elevator.request(request)


class FloorButtonType(Enum):
  up = "UP"
  down = "DOWN"

class FloorButton(Button):
  def __init__(self,typeFB,location):
    super().__init__(ButtonType.external)
    self.location = location
    self.typeFB = typeFB

  def sendRequest(self):
    print('Sending Floor Button Request',self.location,self.typeFB)
    if self.typeFB == FloorButtonType.up:
      request = Request(RequestType.external, RequestDirection.up,self.location, self.location)
      elevator.request(request)

    else:
      request = Request(RequestType.external, RequestDirection.down,self.location, self.location)
      elevator.request(request)

floor = FloorButton(FloorButtonType.up,0)

class RequestType(Enum):
    internal = "INTERNAL"
    external = "EXTERNAL"

class RequestDirection(Enum):
    up = 1
    down = 0

class Request:
    def __init__(self,typeR, direction, origin, target):
        self.typeR = typeR
        self.direction = direction
        self.origin = origin
        self.target = target

class ElevatorStatus(Enum):
  down = 0
  up = 1
  idle = 2

class Elevator:
  def __init__(self,location = 0):
    self.location = 0
    self.status = ElevatorStatus.idle
    self.door = ElevatorDoor()
    self.goTobuttons = [ElevatorGoToFloorButton(i) for i in range(NUMBER_OF_FLOORS)]
    # self.display
    # self.open button
    # selt.close
    # phone, emergency
    # weight limit
    self.upRequests = []
    self.downRequests = []


  def run(self):
    while self.upRequests or self.downRequests:
      self.processRequests()

  def processRequests(self):
    if self.upRequests:
      self.processUpRequests()
      self.processDownRequests()

    else:
      self.processDownRequests()

  def processUpRequests(self):
    "Process uprequests by closest floor first"
    while self.upRequests:
      # Set status to moving up
      # Pop closest up request off the stack
      # Close Door
      # Move to request floor
      # Open door
      # Wait a few seconds
      # Remove any up or down requests that happen to coincide with the current floor or add pending requests that coincide with origin
      # Publish event for fulfilled request, unpressing buttons and changing displays
      # close door
      self.status = ElevatorStatus.up
      current_request = self.upRequests.pop(0)
      self.door.close()
      self.location = current_request.target
      self.door.open()
      if current_request.target == current_request.origin:
        print('Picking up people for Up Request, on floor:', self.location)

      else:
        print('Letting people off for Up Request, on floor:',self.location)
      self.door.close()

    self.status = ElevatorStatus.idle

  def processDownRequests(self):
    "Process downRequests by closest floor first"
    while self.downRequests:
      # Set status to moving up
      # Pop closest up request off the stack
      # Close Door
      # Move to request floor
      # Open door
      # Wait a few seconds
      # Remove any up or down requests that happen to coincide with the current floor or add pending requests that coincide with origin
      # close door
      self.status = ElevatorStatus.down
      current_request = self.downRequests.pop(0)
      self.door.close()
      self.location = current_request.target
      # Open Floor Door
      self.door.open()
      if current_request.target == current_request.origin:
        print('Picking up people for Down Request, on floor:', self.location)

      else:
        print('Letting people off for Down Request, on floor:',self.location)
      self.door.close()
    self.status = ElevatorStatus.idle


  def request(self,request):

    if request.direction == RequestDirection.up:
      self.upRequests.append(request)
      self.upRequests.sort(key = lambda x: x.target)

    else:
      self.downRequests.append(request)
      self.downRequests.sort(key = lambda x: -x.target)


class Floor:
  def __init__(self,location):
    self.location = location
    self.upButton = FloorButton(FloorButtonType.up,location)
    self.downButton = FloorButton(FloorButtonType.down,location)
    self.door = FloorDoor(location)

  def pressFloorButton(self,direction):
    if direction == FloorButtonType.up:
      self.upButton.press()
    else:
      self.downButton.press()


elevator = Elevator()

Floors = [Floor(i) for i in range(NUMBER_OF_FLOORS)]


Floors[4].pressFloorButton(FloorButtonType.up)
elevator.location = 4
elevator.goTobuttons[2].press()
elevator.run()

print()
print("RUN 2")

elevator.goTobuttons[9].press()
elevator.goTobuttons[5].press()
elevator.goTobuttons[7].press()
elevator.goTobuttons[0].press()
elevator.goTobuttons[1].press()

elevator.run()
