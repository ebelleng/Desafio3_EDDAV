import pandas as pd

def create_df():
    df_movies = pd.read_csv("dataset/movies.csv")
    return df_movies

def generate_points(df_movies):
    df_vector = vectorizar_df(df_movies)
    return df_vector.values.tolist()

def generate_points_byId(df_movies, id):
    df_vector = vectorizar_df(df_movies)
    return df_vector[ df_vector["Rank"] == id].values.tolist()

def search_byId( df , id ):
    movie = df[ df["Rank"] == id ]
    if len(movie) != 0: return movie.values.tolist()
    return None

def print_byId(df, id):
    movie = df[ df["Rank"] == id ]
    print(f'{movie["Rank"].values[0]}: {movie["Title"].values[0]}')

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

def vectorizar_df(df_movies):
    # Generar dummies para genero, director y actores
    df_genre = df_movies["Genre"].str.get_dummies(sep=',')
    df_director = df_movies["Director"].str.get_dummies(sep=',')
    df_actors = df_movies["Actors"].str.get_dummies(sep=',')

    # Guardamos en dataframe para generar un vector
    df_vector = pd.concat( [df_movies["Rank"], df_genre, df_director, df_actors, df_movies["Rating"] ], axis=1 )
    return df_vector