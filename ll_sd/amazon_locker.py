# Original approach:

# Create a Locker class to represent a locker with an ID, size, and status.
# Create a Package class to represent a package with an ID, size, and status.
# Create a LockerLocator class to manage lockers and packages.
# Initialize the LockerLocator with a list of Locker objects.
# Implement the find_locker_for_box method to find a locker that can fit a package based on its size.
# Sort the list of lockers by their maximum dimension.
# Use binary search to find the first locker with a maximum dimension that is greater than or equal to the package's maximum dimension.
# Iterate through the sorted list of lockers starting from the found index and check if each locker is vacant.
# If a locker is found, mark it as occupied and return its ID.
# If no locker is found, return None.

import bisect
class Locker:
    def __init__(self, x, y , z, **kwargs):
        self.length = x
        self.width = y
        self.height = z
        self.locker_id = kwargs.get('id', None)
        self.vacant = True

    def get_max_dimension(self):
        return max([self.length, self.width, self.height])

class Package:
    def __init__(self, x, y, z, **kwargs):
        self.length = x
        self.width = y
        self.height = z
        self.package_id = kwargs.get('id', None)


class LockerLocator:
    def __init__ (self, lockers):
        self.lockers = lockers
        self.sorted_lockers = sorted((x.get_max_dimension(), x) for x in self.lockers)

    def find_locker_for_box(self, box):
        # given a box, find a suitable unoccupied locker
        # lockers in the locator is sorted by max dimension
        # first fit the box's maximum dimension, then try to rotate the box
        # and find the first fit for the remaining two dimensions
        maxd = max([box.length, box.width, box.height])
        index = bisect.bisect_left(self.sorted_lockers, maxd)
        for i in range(index, len(self.sorted_lockers)):
            if not self.sorted_lockers[i][1].vacant:
                continue
            if self.check_fit(self.sorted_lockers[i][1], box):
                self.sorted_lockers[i][1].vacant = False
                return self.sorted_lockers[i][1].id

    def check_fit(self, locker, box):
        """
        sort the three dimensions, and check each dimension of the box fits
        into the locker
        """
        locker_dimensions = sorted([locker.length, locker.width, locker.height])
        box_dimensions = sorted([box.length, box.width, box.height])
        for i in range(3):
            if box_dimensions[i] <=locker_dimensions[i]:
                return True
        return False


# Create a list of lockers
lockers = [
    Locker(1, 10, 10, 10),
    Locker(2, 20, 20, 20),
    Locker(3, 30, 30, 30)
]

# Create a LockerLocator instance
locker_locator = LockerLocator(lockers)

# Create a package
package = Package(5, 5, 5)

# Find a locker for the package
locker_id = locker_locator.find_locker_for_box(package)

# Print the locker ID
print(locker_id)

##############


# Modified approach:
# Create a Locker class to represent a locker with an ID, size, and status.
# Create a Package class to represent a package with an ID, size, and status.
# Create a LockerLocator class to manage lockers and packages.
# Initialize the LockerLocator with a list of Locker objects.
# Implement the process_lockers method to process the list of lockers and create a dictionary mapping locker sizes to lockers.
# Implement the find_locker_for_box method to find a locker that can fit a package based on its size.
# Sort the list of lockers keys by size in descending order.
# Iterate through the sorted list of lockers keys and find the first locker that can fit the package and is vacant.
# If a locker is found, mark it as occupied and return its ID.
# If no locker is found, return None.


class Locker:
    def __init__(self, x, y , z, **kwargs):
        self.locker_id = kwargs.get('id', None)
        self.vacant = True
        self.sorted_d = tuple(sorted((x, y, z),reverse=True))

    def mark_occupied(self):
        self.vacant = False


class Package:
    def __init__(self, x, y, z, **kwargs):
        self.package_id = kwargs.get('id', None)
        self.sorted_d = tuple(sorted((x, y, z),reverse=True))


class LockerLocator:
    def __init__ (self, lockers):
        self.lockers = self.process_lockers(lockers)

    def process_lockers(self, lockers):
        locker_dict = {}
        for locker in lockers:
            if locker.sorted_d not in locker_dict:
                locker_dict[locker.sorted_d] = []
            locker_dict[locker.sorted_d].append(locker)
        return locker_dict

    def find_locker_for_box(self, box):
        lockers_keys = [k for k in self.lockers.keys() if k[0]>box.sorted_d[0] and k[1]>box.sorted_d[1] and k[1]>box.sorted_d[1]]
        lockers_keys.sort(key=lambda k:k[0])
        for key in lockers_keys:
            for locker in self.lockers[key]:
                if locker.vacant:
                    locker.mark_occupied()
                    return locker.locker_id
        return None


# Create a list of lockers
lockers = [
    Locker(1, 10, 10, 10),
    Locker(2, 20, 20, 20),
    Locker(3, 30, 30, 30)
]

# Create a LockerLocator instance
locker_locator = LockerLocator(lockers)

# Create a package
package = Package(5, 5, 5)

# Find a locker for the package
locker_id = locker_locator.find_locker_for_box(package)

# Print the locker ID
print(locker_id)

##############

# Modified 2:

from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    EXTRALARGE = 4

class Package:
    count = 0
    def __init__(self, package_size):
        Package.count += 1
        self.package_id = Package.count
        self.package_size = package_size

    def get_package_size(self):
        return self.package_size

class PackageFactory:
    @staticmethod
    def create(package_size):
        if not isinstance(package_size, Size):
            raise ValueError(package_size)
        return Package(package_size)

class Locker:
    count = 0
    def __init__(self, locker_size):
        Locker.count += 1
        self.locker_id = Locker.count
        self.locker_size = locker_size
        self.vacancy_status = True

    def set_vacancy_status(self, new_status):
        self.vacancy_status = new_status

    def get_vacancy_status(self):
        return self.vacancy_status

    def get_locker_size(self):
        return self.locker_size

    def get_locker_id(self):
        return self.locker_id


class LockerFactory:
    @staticmethod
    def create(locker_size):
        if not isinstance(locker_size, Size):
            raise ValueError(locker_size)
        return Locker(locker_size)


class LockerManager:
    def __init__(self, lockers = []):
        self.lockers = lockers
        self.locker_map = {}

    def get_lockers(self):
        return self.lockers


    def add_lockers(self, new_lockers):
        if any(not isinstance(l, Locker) for l in new_lockers):
            raise ValueError(new_lockers)
        self.lockers.extend(new_lockers)

    @staticmethod
    def match_sizes(locker, package):
        locker_size = locker.get_locker_size().value
        package_size = package.get_package_size().value
        return locker_size >= package_size

    def occupy_locker(self, package):
        if not isinstance(package, Package):
            raise ValueError(package)
        for locker in self.get_lockers():
            if locker.get_vacancy_status():
                match = LockerManager.match_sizes(locker, package)
                if not match: continue
                locker_id = locker.get_locker_id()
                self.locker_map[locker_id] = package
                locker.set_vacancy_status(False)
                return (locker_id, True)
        return (-1, False)

    def extract_package_from_locker(self, locker_id):
        for locker in self.get_lockers():
            if locker_id in self.locker_map and locker_id == locker.get_locker_id():
                locker.set_vacancy_status(True)
                stored_package = self.locker_map[locker_id]
                return stored_package
        return None

small_locker = LockerFactory.create(Size.SMALL)
medium_locker = LockerFactory.create(Size.MEDIUM)
large_locker = LockerFactory.create(Size.LARGE)


lm = LockerManager()
lm.add_lockers([small_locker, medium_locker, large_locker])

p1 = PackageFactory.create(Size.LARGE)
p2 = PackageFactory.create(Size.LARGE)
p3 = PackageFactory.create(Size.LARGE)
p4 = PackageFactory.create(Size.LARGE)

print(lm.extract_package_from_locker(large_locker.get_locker_id()))
#None

packages = [p1, p2, p3, p4]
for i,p in enumerate(packages):
    print(i, lm.occupy_locker(p))
    """
    (0, (3, True))
    (1, (-1, False))
    (2, (-1, False))
    (3, (-1, False))
    """

print(lm.extract_package_from_locker(large_locker.get_locker_id()))
#<__main__.Package instance at 0x7f067d3e1280>
