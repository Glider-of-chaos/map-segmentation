import csv
import math

class GeoLine:

    def __init__(self, coords_one, coords_two):
        if coords_one[0] < coords_two[0]:
            self.start = coords_one
            self.end = coords_two
        elif coords_one[0] > coords_two[0]:
            self.start = coords_two
            self.end = coords_one
        else:
            if coords_one[1] < coords_two[1]:
                self.start = coords_one
                self.end = coords_two
            else:
                self.start = coords_two
                self.end = coords_one
                
    def __str__(self):
        return (self.start, self.end).__str__()
                
    def ray_intersection(self, line):
        line1_lat_start = self.start[0]
        line1_lon_start = self.start[1]
        line1_lat_end = self.end[0]
        line1_lon_end = self.end[1]

        line2_lat_start = line.start[0]
        line2_lon_start = line.start[1]
        line2_lat_end = line.end[0]
        line2_lon_end = line.end[1]
        
        line1_lon_const = False
        line2_lon_const = False
        
        slope1 = self.slope()
        if math.isnan(slope1):
            line1_lon_const = True
            
        slope2 = line.slope()
        if math.isnan(slope2):
            line2_lon_const = True
            
        if (line1_lon_const and line2_lon_const) or (slope1 == slope2):
            if line1_lat_start == line2_lat_start:
                return self
            else:
                return math.nan
        
        elif line1_lon_const:
            lon = line1_lon_start
            lat = line.lat(lon)
            
        elif line2_lon_const:
            lon = line2_lon_start
            lat = self.lat(lon)
            
        else:
            lon = (line2_lat_start -line1_lat_start - line2_lon_start*slope2 + line1_lon_start*slope1)/(slope1-slope2)
            lat= line1_lat_start + (lon - line1_lon_start) * slope1
        
        return (lat, lon)
        
    def slope(self):
        line1_lat_start = self.start[0]
        line1_lon_start = self.start[1]
        
        line1_lat_end = self.end[0]
        line1_lon_end = self.end[1]

        try:
            slope = (line1_lat_end - line1_lat_start)/(line1_lon_end - line1_lon_start)
        except ZeroDivisionError:
            slope = math.nan

        return slope
        
    def includes_point(self, point):
        
        point_lat = point[0]
        point_lon = point[1]
        
        line1_lat_start = self.start[0]
        line1_lon_start = self.start[1]

        line1_lat_end = self.end[0]
        line1_lon_end = self.end[1]
        
        if  point_lat >= self.start[0] and point_lat <= self.end[0] and point_lon >= self.start[1] and point_lon <= self.end[1]:
            if point_lat == line1_lat_start + point_lon * (line1_lon_end - line1_lon_start)/(line1_lat_end - line1_lat_start):
                return True
        return False
        
    def lat(self,lon):
        line1_lat_start = self.start[0]
        lat = self.start[0] + (lon - self.start[1])*self.slope()
        return lat
        
    def intersects(self, line):
        line1_lat_min = round(min(self.start[0], self.end[0]), 12)
        line1_lat_max = round(max(self.start[0], self.end[0]), 12)
        line1_lon_min = round(min(self.start[1], self.end[1]), 12)
        line1_lon_max = round(max(self.start[1], self.end[1]), 12)
        
        line2_lat_min = round(min(line.start[0], line.end[0]), 12)
        line2_lat_max = round(max(line.start[0], line.end[0]), 12)
        line2_lon_min = round(min(line.start[1], line.end[1]), 12)
        line2_lon_max = round(max(line.start[1], line.end[1]), 12)

        ray_intersection_point = self.ray_intersection(line)

        if isinstance(ray_intersection_point, float):
            if math.isnan(ray_intersection_point):
                return false
            else:
                raise ValueError('float that is non a nan was returned from the ray_intersection')
        elif ray_intersection_point == self:
            if line1_lat_min == line_lat_max:
                return (line2_lon_min <= line1_lon_max and line2_lon_max >= line1_lon_min)
            else:
                return (line2_lat_min <= line1_lat_max and line2_lat_max >= line1_lat_min)
        elif isinstance(ray_intersection_point, tuple):
            lat = round(ray_intersection_point[0], 12)
            lon = round(ray_intersection_point[1], 12)
            return (line2_lat_min <= lat and line2_lat_max >= lat and
                line1_lat_min <= lat and line1_lat_max >= lat
                and
                line2_lon_min <= lon and line2_lon_max >= lon and
                line1_lon_min <= lon and line1_lon_max >= lon)
        else:
            raise ValueError('unexpected value returned from ray_intersection')
            
    def find_sections(self):
        lat_start = self.start[0]
        lon_start = self.start[1]
        lat_end = self.end[0]
        lon_end = self.end[1]
        
        rounded_lat_start = math.floor(self.start[0]*100)/100
        rounded_lon_start = math.floor(self.start[1]*100)/100
        rounded_lat_end = math.floor(self.end[0]*100)/100
        rounded_lon_end = math.floor(self.end[1]*100)/100
        
        sections = [(round(rounded_lat_start, 2), round(rounded_lon_start, 2))]
        
        if rounded_lat_start == rounded_lat_end and rounded_lon_start == rounded_lon_end:
            return sections
            
        if rounded_lat_start != rounded_lat_end:
            crossed_lats = round((rounded_lat_end - rounded_lat_start)*100)
            crossed_lons = round((rounded_lon_end - rounded_lon_start)*100)
            for i in range(0, crossed_lats + 1):
                for j in range(0, crossed_lons + 1):
                    section_node = (round(rounded_lat_start + 0.01*i, 2), round(rounded_lon_start + 0.01*j, 2))
                    if (section_node) not in sections:
                        crossing_lat = GeoLine((rounded_lat_start + 0.01*i, rounded_lon_start + 0.01*j),
                                                (rounded_lat_start + 0.01*(i+1), rounded_lon_start + 0.01*j))
                        crossing_lon = GeoLine((rounded_lat_start + 0.01*i, rounded_lon_start + 0.01*j),
                                                (rounded_lat_start + 0.01*i, rounded_lon_start + 0.01*(j + 1)))
                        
                        lat_crossed = self.intersects(crossing_lat)
                        lon_crossed = self.intersects(crossing_lon)
                        
                        if lat_crossed or lon_crossed:
                            sections.append(section_node)
                            
        return sections


            
#    lat= line1_lat_start + (lon - line1_lon_start) * slope1
#    lat= line2_lat_start + (lon - line2_lon_start) * slope2
        
#        lon = (line2_lat_start - line1_lat_start) / \
#            ( (line1_lon_end - line1_lon_start)/(line1_lat_end - line1_lat_start) -\
#            (line2_lon_end - line2_lon_start)/(line2_lat_end - line2_lat_start) )

#        line1_lat_start + lon*slope1 - line1_lon_start*slope1 = line2_lat_start + lon*slope2 - line2_lon_start*slope2
#        lon(slope1-slope2) = line2_lat_start -line1_lat_start - line2_lon_start*slope2 + line1_lon_start*slope1
        
if __name__ == '__main__':        
    sections_dict = {}
    with open("E:\Downloads\Programming\map\sections.csv", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            key = '-'.join((row[2], row[3]))
            sections_dict[key] = row[0]
        
    with open("E:\Downloads\Programming\map\dp_view_01.csv", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        #for row in csvreader:
