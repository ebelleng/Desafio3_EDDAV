from kd_tree import KD_Tree

kdt = KD_Tree(2)

nodes_to_insert = [(30,40), (5,25), (10,12), (70,70), (50,30), (35,45)]
#nodes_to_insert = [(1,1), (-2,1), (3,-1), (1,4), (-5,1), (-1,6)]

for i in range(len(nodes_to_insert)):
  kdt.insert(nodes_to_insert[i], i)

# Print the resultant tree (level by level)
#kdt.showTree()

node_to_search = (70, 70)
print(kdt.search(node_to_search))

point = (35, 45)
knn = kdt.k_nearest_neighbors(point, 4)

for i in range(len(knn)):
  print(knn[i].point, knn[i].id)