from kd_tree.kd_tree import KD_Tree
import dataset.dataset as ds

df = ds.create_df()

# ds.generate_points retorna una lista dnd el 1er elemento es el id
nodes_to_insert = ds.generate_points(df)
COLS = len(nodes_to_insert[0]) - 1
kdt = KD_Tree(COLS)

for i in range(len(nodes_to_insert)):
    #  .insert([points], id)
    kdt.insert(nodes_to_insert[i][1:], nodes_to_insert[i][0])

# Mostrar por id
#node_to_search = 1234
#print(kdt.search(node_to_search))

# Mostrar 10 knn
id = 124
point = ds.generate_points_byId(df, id)
knn = kdt.k_nearest_neighbors(point[0][1:], 10)
i = 1
for movie in knn:
    print(f'{i}) ', end='')
    ds.print_byId(df, movie.id)
    i += 1

# Mostrar 10 knn por vector ingresado por teclado



