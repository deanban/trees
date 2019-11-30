import xml.etree.ElementTree as ET

CIRCLE_TAG = '{http://www.w3.org/2000/svg}circle'
GROUP_TAG = '{http://www.w3.org/2000/svg}g'

def get_points_from_circle(circle):
  '''
  Returns points from each circle collected in get_points_from_svg()
  '''
  return (float(circle.attrib['cx']), float(circle.attrib['cy']))


def parse_svg(file):
  '''
  Parsed a svg file and returns it's tree.
  '''
  return ET.parse(file)


def get_all_points(tree):
  '''
  Returns all points from a tree
  '''
  # collect all the circles in file and return points from the circles
  return [get_points_from_circle(circle) for circle in tree.iter(CIRCLE_TAG)]


def get_point_by_id(tree, point_id):
  '''
  Collects points from svg tree where point_id is a match.
  Returns points.
  '''
  return [get_points_from_circle(circle) for circle in tree.iter(CIRCLE_TAG) if('id' in circle.attrib)
          if(circle.attrib['id'] == point_id)]


def get_group_by_id(tree, group_id):
  '''
  Collects points from a group in svg tree where group_id is a match.
  Returns points.
  '''
  return [points
          for group in tree.iter(GROUP_TAG)
          if('id' in group.attrib)
          if(group.attrib['id'] == group_id)
          for points in get_all_points(group)]


svg_tree = parse_svg('./points.svg')
[pivot] = get_point_by_id(svg_tree, 'pivot')
all_points = get_group_by_id(svg_tree, 'points')
