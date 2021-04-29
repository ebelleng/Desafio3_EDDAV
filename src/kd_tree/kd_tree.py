from kd_node import KD_Node

class KD_Tree:
  def __init__(self, dimensions):
    self.root = None
    self.D = dimensions

  def insert(self, point):
    if self.root == None:
      self.root = KD_Node(point, 0)
    else:
      parent_aux = self.root
      aux = self.root

      while aux != None:
        parent_aux = aux
        
        if aux.point[aux.cd] > point[aux.cd]:
          aux = aux.left
        else:
          aux = aux.right

      new_node = KD_Node(point, (parent_aux.cd + 1) % self.D)
      new_node.parent = parent_aux

      if parent_aux.point[parent_aux.cd] > point.[parent_aux.cd]:
        parent_aux.left = new_node
      else:
        parent_aux.right = new_node