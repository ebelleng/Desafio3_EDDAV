import pandas as pd

def create_df():
    df_movies = pd.read_csv("./dataset/movies.csv")
    return df_movies

def generate_points(df_movies):
    # Generar dummies para genero, director y actores
    df_genre = df_movies["Genre"].str.get_dummies(sep=',')
    df_director = df_movies["Director"].str.get_dummies(sep=',')
    df_actors = df_movies["Actors"].str.get_dummies(sep=',')

    # Guardamos en dataframe para generar un vector
    df_vector = pd.concat( [df_movies["Rank"], df_genre, df_director, df_actors, df_movies["Votes"], df_movies["Rating"] ], axis=1 )
    return df_vector.values.tolist()

def generate_points_byId(df_movies, id):
    # Generar dummies para genero, director y actores
    df_genre = df_movies["Genre"].str.get_dummies(sep=',')
    df_director = df_movies["Director"].str.get_dummies(sep=',')
    df_actors = df_movies["Actors"].str.get_dummies(sep=',')

    # Guardamos en dataframe para generar un vector
    df_vector = pd.concat( [df_movies["Rank"], df_genre, df_director, df_actors, df_movies["Votes"], df_movies["Rating"] ], axis=1 )
    return df_vector[ df_vector["Rank"] == id].values.tolist()

def search_byId( df , id ):
    movie = df[ df["Rank"] == id ]
    if len(movie) != 0: return movie.values.tolist()
    return None

def print_byId(df, id):
    movie = df[ df["Rank"] == id ]
    #print(movie["Title"].values[0] )
    print(f'{movie["Rank"].values[0]}: {movie["Title"].values[0]}')

