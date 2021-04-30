from kd_tree import KD_Tree

kdt = KD_Tree(2)

nodes_to_insert = [(30,40), (5,25), (10,12), (70,70), (50,30), (35,45)]

for i in range(len(nodes_to_insert)):
  kdt.insert(nodes_to_insert[i])

# Print the resultant tree (level by level)
kdt.showTree()

node_to_search = (70, 70)

print(kdt.search(node_to_search))