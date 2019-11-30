import math
import xml.etree.ElementTree as ET

CIRCLE_TAG = '{http://www.w3.org/2000/svg}circle'

def get_points_from_circle(circle):
  '''
  Returns points from each circle collected in get_points_from_svg()
  '''
  return (float(circle.attrib['cx']), float(circle.attrib['cy']))

def get_points_from_svg(file):
  '''
  DEPRECATED
  Parses all the points from svg file.
  '''
  tree = ET.parse(file)
  # collect all the circles in file and return points from the circles
  return [get_points_from_circle(circle) for circle in tree.iter(CIRCLE_TAG)]

def parse_svg(file):
  '''
  Parsed a svg file and returns it's tree.
  '''
  return ET.parse(file)

def get_point_by_id(tree, point_id):
  '''
  Collects points from svg tree where point_id is a match.
  Returns points.
  '''
  return [get_points_from_circle(circle) for circle in tree.iter(CIRCLE_TAG)if('id' in circle.attrib)
  if(circle.attrib['id'] == point_id)]

def distance(point1, point2):
  '''
  Find distance between two points in 2d space.
  '''
  x1, y1 = point1
  x2, y2 = point2

  dx = x1 - x2
  dy = y1 - y2

  return math.sqrt(dx * dx + dy * dy)

def closest_point(all_points, new_point):
  '''
  Find closest neighbor to new_point in the set of
  all_points.
  '''
  best_known_point = None
  best_known_distance = None

  for curr_point in all_points:
    curr_distance = distance(new_point, curr_point)

    if(best_known_distance is None or curr_distance < best_known_distance):
      best_known_point = curr_point
      best_known_distance = curr_distance

  return best_known_point



import pdb; pdb.set_trace()
