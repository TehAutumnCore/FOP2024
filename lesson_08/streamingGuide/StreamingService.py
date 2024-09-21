from movie import Movie

class StreamingService():
    def __init__(self,name):
        self.name = name
        self.catalog = {} #titles(keys) : Movie objects(values)

    def get_name(self):
        return self.name
    
    def get_catalog(self):
        return self.get_catalog

    def add_movie(self,movie_object):
        self.get_catalog[movie_object.get_title()] = movie_object

    def delete_movie(self,movie_title):
        movie_title = self.title
        if movie_title in self.catalog:
            del self._catalog[movie_title]