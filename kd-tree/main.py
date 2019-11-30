import math
import pprint
from helpers import all_points, pivot

pp = pprint.PrettyPrinter(indent=2)

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


def build_kd(points, depth=0):
  '''
  Partitions all the points to regions.
  Returns a tree of regions
  '''
  k = 2   # dimensions

  n = len(points)
  if(n <= 0):
    return None

  partition = depth % k
  sorted_points = sorted(points, key=lambda point: point[partition])

  return {
    'point': sorted_points[n//2], # middle, floored
    'left': build_kd(sorted_points[:n//2], depth + 1),
    'right': build_kd(sorted_points[n//2 + 1:], depth + 1)
  }


pp.pprint(build_kd(all_points))
