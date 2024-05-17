from datetime import date, timedelta

class Book:
    def __init__(self, title, author, publication_date, unique_id):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.unique_id = unique_id

    def get_details(self):
        return {
            "title": self.title,
            "author": self.author,
            "publication_date": self.publication_date,
            "unique_id": self.unique_id
        }
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Date: {self.publication_date}, Unique ID: {self.unique_id}"

class BookItem:
    def __init__(self, book, barcode, rack_number):
        self.book = book
        self.barcode = barcode
        self.rack_number = rack_number
        self.is_available = True
        self.due_date = None
        self.reserved_by = None

    def check_out(self, member):
        if self.is_available:
            self.is_available = False
            self.due_date = date.today() + timedelta(days=10)
            member.checked_out_books.append(self)
            return True
        else:
            return False

    def reserve(self, member):
        if self.is_available:
            self.reserved_by = member
            member.reserved_books.append(self)
            return True
        else:
            return False

    def return_book(self):
        self.is_available = True
        self.due_date = None
        self.reserved_by = None

    def __repr__(self):
        return self.book.title

# class BookReservation:
#     def __init__(self, book_item, member, reservation_date):
#         self.book_item = book_item
#         self.member = member
#         self.reservation_date = reservation_date

#     def fetch_reservation(self):
#         return {
#             "book_item": self.book_item,
#             "member": self.member,
#             "reservation_date": self.reservation_date
#         }

class Catalog:
    def __init__(self):
        self.books = []
        self.book_items = []

    def search_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def search_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def search_by_pub_date(self, pub_date):
        return [book for book in self.books if book.publication_date == pub_date]

    def __repr__(self):
        return f"{self.books}$$$$${self.book_items}"

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.checked_out_books = []
        self.reserved_books = []
        self.total_fines = 0

    def __repr__(self):
        return f"{self.name}"

    def check_out_book(self, book_item):
        if len(self.checked_out_books) < 5:
            if book_item.check_out(self):
                return True
            else:
                return False
        else:
            return False

    def reserve_book(self, book_item):
        if book_item.reserve(self):
            return True
        else:
            return False

    def return_book(self, book_item):
        book_item.return_book()
        self.checked_out_books.remove(book_item)

    def renew_book(self, book_item):
        if book_item in self.checked_out_books:
            book_item.due_date += timedelta(days=10)
            return True
        else:
            return False

    def pay_fine(self, amount):
        self.total_fines -= amount

class FinePolicy:
    def __init__(self, max_allowed_days=10, fine_per_day=0.5):
        self.max_allowed_days = max_allowed_days
        self.fine_per_day = fine_per_day

    def calculate_fine(self, days_delayed):
        return days_delayed * self.fine_per_day

class LibrarySystem:
    def __init__(self):
        self.catalog = Catalog()
        self.members = []
        self.fine_policy = FinePolicy()
        self.max_books_allowed = 5

    def add_book(self, book):
        self.catalog.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def search_books(self, query, search_type):
        if search_type == "title":
            return self.catalog.search_by_title(query)
        elif search_type == "author":
            return self.catalog.search_by_author(query)
        elif search_type == "subject":
            return self.catalog.search_by_subject(query)
        elif search_type == "pub_date":
            return self.catalog.search_by_pub_date(query)
        else:
            return []

    def check_out_book(self, member, book_item):
        if member:
            return member.check_out_book(book_item)
        else:
            return False

    def reserve_book(self, member_id, book_item):
        member = next((member for member in self.members if member.member_id == member_id), None)
        if member:
            return member.reserve_book(book_item)
        else:
            return False

    def return_book(self, member, book_item):
        if member:
            member.return_book(book_item)
            return True
        else:
            return False

    def renew_book(self, member, book_item):
        if member:
            return member.renew_book(book_item)
        else:
            return False

    def pay_fine(self, member, amount):
        if member:
            member.pay_fine(amount)
            return True
        else:
            return False

library_system = LibrarySystem()

book1 = Book("Harry Potter", "JK Rowling", "Fiction", "B001")
library_system.add_book(book1)
book_item = BookItem(book1, "barcode123", "rack123")
# print(book1)

book2 = Book("Game of Thrones", "JK Rowling", "Fiction", "B001")
library_system.add_book(book2)
book_item2 = BookItem(book2, "barcode234", "rack234")

member1 = LibraryMember("John Doe", "M001")
library_system.add_member(member1)
print(member1)

search_results = library_system.search_books("Harry Potter", "title")
print(search_results)

library_system.check_out_book(member1, book_item)
print(member1.checked_out_books)

library_system.return_book(member1, book_item)
print(member1.checked_out_books)

