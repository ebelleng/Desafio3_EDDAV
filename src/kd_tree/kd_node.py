class KD_Node:
  def __init__(self, point, cutting_dimension=0):
    """ 
    point : tuple
    """
    self.left = None
    self.right = None
    self.parent = None
    self.point = point
    self.cd = cutting_dimension

  def __eq__(self, other):
    return self.point == other.point