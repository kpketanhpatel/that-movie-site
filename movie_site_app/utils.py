class Movie:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Movie_List:
    def __init__(self, head=None):
        self.head = head
    
    def insert_data(self, data):
        new_movie = Movie(data)
        new_movie.set_next(self.head)
        self.head = new_movie


my_movies = Movie_List()

print(my_movies)

my_movies.insert_data("Frozen")

print(my_movies.head.data)