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
#node_to_search = 123
#print(kdt.search(node_to_search))

# Mostrar 10 knn
print("Ingrese aplicación (id): ", end='')
id = int(input())
point = ds.generate_points_byId(df, id)
knn = kdt.k_nearest_neighbors(point[0][1:], 10)
i = 1
print("Top 10 aplicaciones más parecidas a las ingresadas por el usuario")
for movie in knn:
    print(f'{i}) ', end='')
    ds.print_byId(df, movie.id)
    i += 1

# Mostrar 10 knn por vector ingresado por teclado
print("Ingrese datos para los siguientes atributos")
print("Ingrese genero de la pelicula (si es más de uno separe por comas): ", end='')
lista_generos = list(map(str.strip, input().split(',')))
print("Ingrese actor(es) de la pelicula (si es más de uno separe por comas): ", end='')
lista_actores = list(map(str.strip, input().split(',')))
print("Ingrese director de peliculas: ", end='')
director = input()

point = ds.generate_points_byVector(df, director, lista_generos, lista_actores)
knn = kdt.k_nearest_neighbors(point[0][1:], 10)
i=1
print("Top 10 aplicaciones más parecidas a las ingresadas por el usuario")
for movie in knn:
    print(f'{i}) ', end='')
    ds.print_byId(df, movie.id)
    i += 1

