import math
import bisect
from .kd_node import KD_Node

class KD_Tree:
  def __init__(self, dimensions):
    self.root = None
    self.D = dimensions


  def insert(self, point, id_obj=None):
    if len(point) != self.D:
      raise ValueError(f'Dimension of the tree ({self.D}) does not coincide with the point ({len(point)})')

    if self.root == None:
      self.root = KD_Node(id_obj, point, 0)
    else:
      parent_aux = self.root
      aux = self.root

      while aux != None:
        parent_aux = aux
        
        if aux.point[aux.cd] > point[aux.cd]:
          aux = aux.left
        else:
          aux = aux.right

      new_node = KD_Node(id_obj, point, (parent_aux.cd + 1) % self.D)
      new_node.parent = parent_aux

      if parent_aux.point[parent_aux.cd] > point[parent_aux.cd]:
        parent_aux.left = new_node
        #print(f'{point} <- ({parent_aux.point})\n')               # For debug
      else:
        parent_aux.right = new_node
        #print(f'            ({parent_aux.point}) -> {point}\n')     # For debug


  def k_nearest_neighbors(self, point, k=1, same_vector=False):
    if len(point) != self.D:
      raise ValueError(f'Dimension of the tree ({self.D}) does not coincide with the point ({len(point)})')

    stack = [self.root]
    nearst_neighs = []
    nearst_dists = []

    while len(stack) != 0:
      node = stack.pop()
      distance = self.get_distance(node.point, point)

      if len(nearst_dists) < k or distance < nearst_dists[-1]:
        if point != node.point or same_vector == True:
          # Se obtiene el indice para ingresarlo ordenado en las listas
          index = bisect.bisect(nearst_dists, distance)
          nearst_dists.insert(index, distance)
          nearst_neighs.insert(index, node)

      # Si se supero el limite de vecinos se elimina el ultimo
      if len(nearst_dists) > k:
        nearst_dists.pop()
        nearst_neighs.pop()

      distance_branch = abs(node.point[node.cd] - point[node.cd])

      if node.point[node.cd] > point[node.cd]:
        if node.left != None:
          stack.append(node.left)

        if distance_branch < nearst_dists[-1] and node.right != None:
          stack.append(node.right)
      else:
        if node.right != None:
          stack.append(node.right)

        if distance_branch < nearst_dists[-1] and node.left != None:
          stack.append(node.left)

    return nearst_neighs
      

  def search(self, point):
    if len(point) != self.D:
      raise ValueError(f'Dimension of the tree ({self.D}) does not coincide with the point ({len(point)})')

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


  def get_distance(self, point_one, point_two):
    if len(point_one) != len(point_two):
      raise ValueError(f'Dimension dont match')

    distance = 0.0
    for i in range(len(point_one)):
      distance = distance + (point_two[i] - point_one[i]) ** 2

    return math.sqrt(distance)

  def showTree(self):
    queue = [self.root]

    while len(queue) != 0 and queue[0] != None:
      current_node = queue.pop(0)

      print(current_node.point)

      if current_node.left != None:
        queue.append(current_node.left)
      
      if current_node.right != None:
        queue.append(current_node.right)