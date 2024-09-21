class Point:
    def __init__(self,x_coord,y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def distance_to(self,point_object):
        distance = ((self._x_coord - point_object.get_x_coord()) **2) + ((self._y_coord - point_object.get_y_coord())**2) **.5
        return distance

class LineSegment:

    def __init__(self,endpoint_1,endpoint_2):
        self._endpoint_1_object = endpoint_1_object
        self._endpoint_2_object = endpoint_2_object

    def get_endpoint_1(self):
        return self._endpoint_1_object

    def get_endpoint_2(self):
        return self._endpoint_2_object

    def length(self):
        return self._endpoint_1_object.distance_to(self._endpoint_2_object)

    def slope(self):
        return ((self._endpoint_2_object.get_y_coord() - self._endpoint_1_object.get_y_coord()) / (self._endpoint_2_object.get_x_coord() - self._endpoint_1_object.get_x_coord()))

    def is_parallel_to(line_segment_object):
        #y2 - y1 / x2 - x1
        line_segment_1 = self.slope()
        line_segment_2 = line_segment_object.slope()
        print(line_segment_1,line_segment_2)       

point_1 = Point(7,4)
point_2 = Point(-6,18)
line_segment_1 = LineSegment(point_1,point_2)
point_3 = Point(-2,2)
point_4 = Point(24, 12)
line_segment_2 = LineSegment(point_3,point_4)
print(line_segment_1.slope())
print(line_segment_2.slope())