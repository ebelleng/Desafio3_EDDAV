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

      if parent_aux.point[parent_aux.cd] > point[parent_aux.cd]:
        parent_aux.left = new_node
        #print(f'{point} <- ({parent_aux.point})\n')               # For debug
      else:
        parent_aux.right = new_node
        #print(f'            ({parent_aux.point}) -> {point}\n')     # For debug


  def search(self, point):
    return KD_Tree.searchNode(self.root, point)


  @classmethod
  def searchNode(cls, node, point):
    if node == None:
      return False
    elif node.point == point:
      return True
    elif node.point[node.cd] > point[node.cd]:
      return cls.searchNode(node.left, point)
    else:
      return cls.searchNode(node.right, point)


  def showTree(self):
    queue = [self.root]

    while len(queue) != 0 and queue[0] != None:
      current_node = queue.pop(0)

      print(current_node.point)

      if current_node.left != None:
        queue.append(current_node.left)
      
      if current_node.right != None:
        queue.append(current_node.right)