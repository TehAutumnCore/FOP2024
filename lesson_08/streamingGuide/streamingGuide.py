"""
class Movie:
    def __init__(self,title,genre,director,year):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year

    def get_title(self):
        return self.title
    def get_genre(self):
        return self.genre
    def get_director(self):
        return self.director
    def get_year(self):
        return self.year


class StreamingService():
    def __init__(name,catalog):
        self.name = name
        self.catalog = {} #titles(keys) Movie objects(values)

    def get_name(self):
        return self.name
    
    def get_catalog(self):
        return self.get_catalog

    def add_movie(self,movie_object):
        movie_object = f"Movie title: {self.title}, Movie genre: {self.genre}. Directed by: {self.director}, in the year: {self.year}"
        self.get_catalog[self.title] += movie_object

    def delete_movie(self,movie_title):
        movie_title = self.title
        if movie_title in self.catalog:
            del self.catalog[movie_title]
    
class StreamingGuide(StreamingService):
    
    def __init__(self):
        super.__init__(title,genre,director,year)
    
    def add_streaming_service(StreamingService_Object):
        self.catalog.update(movie_object)
    
    def delete_streaming_service(name_of_streaming_service):
        del self.catalog[movie_object]
    
    def where_to_watch_movie(title):
        title = self.title
        return self.catalog[movie_object[title]]

movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)
"""
from StreamingService import StreamingService
from movie import Movie

class StreamingGuide(StreamingService):
    
    def __init__(self):
        self._streaming_services_list = []
    
    def add_streaming_service(self,StreamingService_Object):
        self._streaming_services_list.append(StreamingService_Object)
    
    def delete_streaming_service(self,streaming_service_name):
        for streaming_service in self._streaming_services_list:
            if streaming_service.get_name() == streaming_service_name:
                self._streaming_services_list.remove(streaming_service)
    
    def where_to_watch_movie(self,movie_title):
        result = []
        for streaming_service in self._streaming_services_list:
            catalog = streaming_service.get_catalog()
            if movie_title in catalog:
                if len(result) == 0:
                    result.append(f"{movie_title} ({catalog[movie_title].get_year()})")
                    result.append(streaming_service.get_name())
                else:
                    result.append(streaming_service.get_name())
        return result if result else None

movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch_movie('Little Women')