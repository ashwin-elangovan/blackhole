# Online cloud reading application

# Similar to amazon kindle (for short stories)

# We need help designing actual application (code that implements this)

# A few things looking for:

# Users have a library of books that they can add to or remove from

# Users can set a book from their library as active

# The reading application remembers where a user left off in a given book

# The reading application only displays a page of text at a time in the active book.


Simple requirements:
- All books in library
- Remember active book
- Remember last pages in all books
- Display a page in active book

- Classes:
  - representing a BOOK
    - id: int ? (can we have title as unique id?)
    - title: str
    - page/content in the book: array of str (per page)
    - last page user looked at: int
  - representing a library
    - collection of books: dict {id: book()}
    - active book: correspond to id int (thought of boolean but dont want to overcomplicate)


class Book:
  def __init__(self, id, title, content):
    self.id = id
    self.title = title
    self.content = content
    self.last_page = 0

    # Calculating font size
    # self.font_size = 12
    # now content will be a single string
    # introduce a new method to calculate chars per page calculate(self.font_size)
    # def display_page(self):
    #   start_idx = self.chars_per_page * self.last_page
    #   end_idx = start_idx + self.chars_per_page
    #   return self.content[start_idx:end_idx]

    # Multiple users share books
    # The above customizations will be of per user basis


  def display_page(self):
    return self.content[self.last_page]

  def turn_page(self):
    self.last_page += 1
    return self.display_page()

class Library:
  def __init__(self):
    self.collection = dict()
    self.active_book = None
    self.id_counter = 0

  def add_book(self, title, content):
    new_book = Book(self.id_counter, title, content)
    self.collection[id_counter] = new_book
    self.id_counter += 1

  def remove_book(self, id):
    del self.collection[id]

  def set_active_book(self, id):
    self.active_book = id

  def display_page(self):
    if self.active_book:
      return self.collection[self.active_book].display_page()
    return None

  def turn_page(self):
    if self.active_book:
      return self.collection[self.active_book].turn_page()
    return None







