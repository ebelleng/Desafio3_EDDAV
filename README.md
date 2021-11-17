# Estructuras de Datos Espaciales

Para entender el objetivo de estas estructuras, debemos mencionar el origen de lo que hoy se conoce como el oro negro del siglo XXI: _los datos_.
Para entender como esta pequeña unidad de información se ha convertido en lo más cotizado en estos días, debemos conocer su historia y creciente evolución.

## El internet de las cosas

Este término aparece por primera vez en 1999, cuando un profesor del MIT usó la expresión de forma publica por primera vez, desde entonces ha tenido un crecimiento de forma exponencial. Pero, ¿a qué se refiere? Básicamente es conectar todos los objetos con los cuales interactuamos y que existen en nuestro planeta. Es decir, que tengan una dirección IP  (Protocolo  de  Internet)  para  que  puedan  generar  información  y  transferir  datos  mediante la red, sin la intervención de los seres humanos.

Una de las consecuencias de esta nueva tendencia es la generación de grandes volúmenes de datos. El 90% de los datos en servidores de todo el mundo se han creado en los últimos años y por eso aparece con tanta fuerza el termino _Big Data_.

## Big data

Cuando hablamos de Big Data nos referimos a conjuntos de datos o combinaciones de conjuntos de datos cuyo tamaño (volumen), complejidad (variabilidad) y velocidad de crecimiento (velocidad) dificultan su captura, gestión, procesamiento o análisis mediante tecnologías y herramientas convencionales, tales como bases de datos relacionales y estadísticas convencionales o paquetes de visualización, dentro del tiempo necesario para que sean útiles. 

Para agilizar las consultas, se han implementado nuevas estructuras de datos, entre ellas los arboles binarios. En particular, para este desafío utilizaremos el KD tree, un arbol diseñado como Metodo de Acceso a Puntos (PAMs) y que sentí las bases para importantes ideas que varios Métodos de Acceso Espacial (SAMs) han utilizado posteriormente.

## KD Tree

Se ha decidido implementar la estructura espacial KD Tree con el nodo raíz y la dimensión del vector que se almacenará en el nodo. Esta estructura trata de mantener la noción de un árbol binario, pero cortando el espacio usando un sólo hiperplano ortogonal y en cada nivel del árbol varia el eje de corte.

    class KD_Tree:
        def __init__(self, dimensions):
          self.root = None
          self.D = dimensions
      
#### Nodo
 
 Para la estructura del nodo se ha implementado la siguiente estructura con el fin de almacenar el vector (point) y el id del registro.
 
    class KD_Node:
      def __init__(self, id_obj, point, cutting_dimension=0):
        self.left = None
        self.right = None
        self.parent = None
        self.point = point
        self.cd = cutting_dimension
        self.id = id_obj
        
#### Métodos

Para insertar los nodos en el árbol, se implementó la siguiente función, la cual busca la posición según las coordenadas (point) del vector y lo inserta donde corresponde.
    
    def insert(self, point, id_obj=None):

Para buscar los vecinos más cercanos se utiliza esta función que recibe un vector y genera los _k_ vecinos más prometedores (que recibe como parámetro) según la distancia entre ellos. El parametro _same_vector_ se utiliza para diferenciar el vector de él mismo y que no se incluya dentro de la solución. 

    def k_nearest_neighbors(self, point, k=1, same_vector=False):

Para buscar un nodo en el árbol se utiliza esta función, la cual recorre el árbol hasta encontrar el vector ingresado por parámetro.

    def search(self, point):
    
Para obtener la distancia entre dos puntos se compara posición por posición de las coordenadas del vector mediante el método de distancia euclideana.

    def get_distance(self, point_one, point_two):
    
### Ejemplo

Se muestra el siguiente ejemplo para probar la estructura.

  
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

    point = (0, 0)
    knn = kdt.k_nearest_neighbors(point, 4)

    for i in range(len(knn)):
    print(knn[i].point, knn[i].id)
 
 Obteniendo como resultado los 4 vecinos más cercanos al punto (0,0):
 
    True
    (10, 12) 2
    (5, 25) 1 
    (30, 40) 0
    (35, 45) 5
    
## Set de datos

Una vez implementado nuestra estructura espacial, se trabajó en el formato de los vectores extrayendo información desde un [csv](/src/dataset/movies.csv).

### Elección del set de datos

Para este desafío se encontró un dataset sobre película con el siguiente formato:

    >> print(df_movies.columns)
    
    Index(['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year', 
    'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)',
    'Metascore'], dtype='object')
    
A continuación se detalla los campos que llamaron más la atención por su pontencial para vectorizar.

| Campo          | Descripción                                                           |
|----------------|-----------------------------------------------------------------------|
| **'Rank'**     | Corresponde al id de cada película                                    |
| **'Title'**    | Corresponde al nombre o titulo de la película                         |
| **'Genre'**    | Es una lista de los generos que categorizan al video separado por ',' |
| **'Director'** | Corresponde al director del film                                      |
| **'Actors'**   | Es una lista de los actores que conforman el reparto                  |
| **'Votes'**    | Corresponde a los votos para calcular el rating                       |
| **'Rating'**   | Corresponde al promedio del puntaje dado por el publico               |

### ETL: Extraer, Transformar y Cargar

De los atributos seleccionados anteriormente se tomaron las siguientes decisiones:

* El 'Rank' se utilizará como identificador de la película, se insertará en la estructura nodo. 
* El 'Title' se descartó ya que no se considera útil a la hora de generar una distancia espacial.
* El 'Genre' se puede incluir en el vector ya que los géneros son finitos y agrupables entre ellos.
* El 'Director' se consideró para incluir en el vector ya que existe una preferencia por películas dirigidas por la misma persona.
* El 'Actors' se trabajará de igual manera que 'Genre' ya que existen preferencias por películas de cierto actor
* El 'Votes' se descartará para la generación del vector ya que no tiene sentido una distancia espacial entre estos elementos.
* El 'Rating' se agregó al vector ya que una película bien evaluada, generará en los usuarios buscar película así. También se puede ver que si una película tiene bajo rating, significa que está más cerca en distancia que una de alto rating, por lo tanto puede considerarse perfectamente como un atributo a incluir.

La transformación de las listas de elementos como géneros y actores se realizó en el siguiente [archivo](/src/dataset/ETL.ipynb). Se utilizó un jypiter notebook para mostrar de forma gráfica la transformación del dataframe y el formato de salida. 

### Funciones para trabajar vector

En el [archivo](/src/dataset/dataset.py) encontramos la implementación de las funciones principales para generar y operar los vectores.

* En la siguiente función se importa el archivo csv a un dataframe

        def create_df():
            df_movies = pd.read_csv("./dataset/movies.csv")
            return df_movies
            
* La siguiente función recibe el dataframe con el formato inicial (el importado desde el csv) y genera el vector con los pasos explicados en la sección del ETL.

        def vectorizar_df(df_movies):
            # Generar dummies para genero, director y actores
            df_genre = df_movies["Genre"].str.get_dummies(sep=',')
            df_director = df_movies["Director"].str.get_dummies(sep=',')
            df_actors = df_movies["Actors"].str.get_dummies(sep=',')

            # Guardamos en dataframe para generar un vector
            df_vector = pd.concat( [df_movies["Rank"], df_genre, df_director, df_actors, df_movies["Rating"] ], axis=1 )
            return df_vector
            
* Esta función es la encargada de recibir un dataframe, lo convierte en vector y lo retorna en formato de lista donde el primer elemento es el id de la película. 

        def generate_points(df_movies):
            df_vector = vectorizar_df(df_movies)
            return df_vector.values.tolist()
            
* En esta función se busca una película en el dataframe y se vectoriza, retornando una lista de los datos

        def generate_points_byId(df_movies, id):
            df_vector = vectorizar_df(df_movies)
            return df_vector[ df_vector["Rank"] == id].values.tolist()
            
* En la siguiente función se ingresa por parametros el director, una lista de actores, otra de generos y el rating de una película. Se inicializa un vector de ceros y se agrupan todos lo ingresado por parámetro en una lista llamada datos, y para cada elemento de esta lista se comprueba si existe una columna en el dataframe del vector, si existe entonces se cambia el valor de su posición en el vector a 1. Una vez comprobado todos los datos, se asigna el rating (corresponde a la ultima opsición del vector y se retorna este.

        def generate_points_byVector(df_vector, director, actors, genres, rating):
            datos = [director] + actors + genres

            vector = [0 for i in range(df_vector.shape[1] - 1)]
            list_columns = df_vector.columns.to_list()

            for dato in datos:
                index = list_columns.index(dato)

                if -1 == index:
                    raise ValueError(f'{dato} no encontrado')

                vector[index - 1] = 1

            vector[-1] = rating

            return vector
           
            
## Conclusión

A raíz del creciente volumen de datos que se ha desarrollado en los ultimos años, se ha expuesto la necesidad de buscar otras estructuras para el manejo de datos. Entre ellas, encontramos el KD Tree, un árbol de complejidad O (k * lg (n)), donde _k_ corresponde a la cantidad de vecinos más cercanos (knn) y _n_ la altura. Este tipo de árboles no funcionan demasiado bien en altas dimensiones (donde hay que visitar multiples ramas de los árboles), para nuestras pruebas (1000 registros de peliculas y un vector de ~3000 columnas) obtuvimos buenos tiempos de respuesta.

Finalmente se entiende que estos problemas tienen buenas soluciones si el dato está en un espacio vectorial de baja dimensión. La complejidad de la mayoría de las técnicas existentes crecen exponencialmente con la dimensión, aunque superan a los tiempos de las bases de datos tradicionales. 
