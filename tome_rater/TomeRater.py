class User(object):
  def __init__(self, name, email):
    # str, str, {obj}
    self.name = name
    self.email = email
    self.books = {}

  def get_email(self):
    return self.email

  def change_email(self, address):
    temp_email = self.email
    self.email = address
    print('Email address updated to {} from {}.'.format(self.email, temp_email))

  def __repr__(self):
    return 'User {}, email: {}, books read: {}'.format(self.name, self.email, len(self.books))

  def __eq__(self, other_user):
    if type(self) != type(other_user):
      return False
    return self.name == other_user.name and self.email == other_user.email

  def read_book(self, book, rating=None):
    self.books[book] = rating

  def get_average_rating(self):
    rating, counter = 0, 0
    for v in self.books.values():
      if v != None:
        rating += v
        counter += 1
    return rating / counter

class Book(object):
  def __init__(self, title, isbn):
    # str, int, [int]
    self.title = title
    self.isbn = isbn
    self.ratings = []

  def get_title(self):
    return self.title

  def get_isbn(self):
    return self.isbn

  def set_isbn(self, isbn):
    temp_isbn = self.isbn
    self.isbn = isbn
    print('ISBN address updated to {} from {}.'.format(self.isbn, temp_isbn))

  def add_rating(self, rating):
    if rating > 0 and rating < 5:
      self.ratings.append(rating)
    else:
      print('Invalid Rating')

  def get_average_rating(self):
    return sum(self.ratings) / len(self.ratings)

  def __hash__(self):
    return hash((self.title, self.isbn))

  def __repr__(self):
    return self.title

  def __eq__(self, other):
    if type(self) != type(other):
      return False
    return self.title == other.title and self.isbn == other.isbn

class Fiction(Book):
  def __init__(self, title, author, isbn):
    super().__init__(title, isbn)
    self.author = author

  def __repr__(self):
    return '{} by {}'.format(self.title, self.author)

class Non_Fiction(Book):
  def __init__(self, title, subject, level, isbn):
    super().__init__(title, isbn)
    self.subject = subject
    self.level = level

  def get_subject(self):
    return self.subject

  def get_level(self):
    return self.level

  def __repr__(self):
    return '{}, {} manual on {}'.format(self.title, self.level, self.subject)

class TomeRater(object):
  def __init__(self):
    self.users = {}
    self.books = {}

  def create_book(self, title, isbn):
    return Book(title, isbn)

  def create_novel(self, title, author, isbn):
    return Fiction(title, author, isbn)

  def create_non_fiction(self, title, subject, level, isbn):
    return Non_Fiction(title, subject, level, isbn)

  def add_book_to_user(self, book, email, rating=None):
    user = self.users.get(email)
    if user == None:
      print('No user with email {}!'.format(email))
    else:
      user.read_book(book, rating)
      book.add_rating(rating)
      self.books[book] = self.books.get(book, 0) + 1

  def add_user(self, name, email, user_books=None):
    user = User(name, email)
    if user_books != None:
      for book in user_books:
        user.read_book(book)
    self.users[email] = user

  def print_catalog(self):
    for k in self.books.keys():
      print(k)

  def print_users(self):
    for v in self.users.values():
      print(v)

  def get_most_read_book(self):
    book = None
    count = -1
    for k, v in self.books.items():
      if v > count:
        count = v
        book = k
    return book

  def highest_rated_book(self):
    book = None
    rating = -1
    for k in self.books.keys():
      r = k.get_average_rating()
      if r > rating:
        rating = r
        book = k
    return book

  def most_positive_user(self):
    user = None
    rating = -1
    for v in self.users.values():
      r = v.get_average_rating()
      if r > rating:
        rating = r
        user = v
    return user

  def __repr__(self):
    user_list = [user.name for user in self.users.values()]
    book_list = [book.title for book in self.books.keys()]
    return 'Tome Rater:\nUsers: {}\nBooks: {}'.format(', '.join(user_list), ', '.join(book_list))
      
  def __eq__(self, other):
    if type(self) != type(other):
      return False
    if len(self.users) != len(other.users) or len(self.books) != len(other.books):
      return False
    for k, v in self.users.items():
      if v != other.users[k]:
        return False
    for k, v in self.books.items():
      if v != other.books[k]:
        return False
    return True

