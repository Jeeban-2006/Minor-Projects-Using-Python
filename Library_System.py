class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0
    def add_book(self,book_name):
        self.books.append(book_name)
        self.no_of_books +=1

    def print_books(self):
        if self.books:
            print("Books in the library")
            for i in self.books:
                print("-" , i)
        else:
            print("no books in the library")   
    @property
    def get_no_of_books(self):
        return self.no_of_books
# Create a Library object
my_library = Library()

# Add some books
# my_library.add_book("Harry Potter")
# my_library.add_book("The Hobbit")
# my_library.add_book("Python Programming")

# Print all books
my_library.print_books()

# Get and print the number of books
print("Total number of books:", my_library.get_no_of_books)



