class KD_Node:
  def __init__(self, id_obj, point, cutting_dimension=0):
    """ 
    point : tuple
    """
    self.left = None
    self.right = None
    self.parent = None
    self.point = point
    self.cd = cutting_dimension
    self.id = id_obj