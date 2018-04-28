# map-segmentation
## Purpose:
The goal is to parse the lines csv file to map line ids to map section ids. Map sections are roughly rectangular and are based on just adding 0.01 incriments to latitude and longitude. Relevant sections are provided in the csv file as well

**lines csv file format:**
"line_id","start_latitude","start_longitude","end_latitude","end_longitude"

**sections csv file format:**
"section_id","max_latitude","min_latitude","min_longitude","max_longitude"

## The plan:
The plan is to create a GeoLine class with the following contents
- ray_intersection_point - to find the point where those line would intersect if they did not end at the start and end points
- includes_point - checks if the point belongs to this line
- intersects - to check if lines actually intersect
- find_sections - actual map segmentation
