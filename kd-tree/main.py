import math
from helpers import points, pivot

def distance(point1, point2):
  '''
  Find distance between two points in 2d space.
  '''

  # destructure points from new_points
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


print(closest_point(points, pivot))
