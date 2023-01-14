import spacy 
nlp = spacy.load('en_core_web_md')

# reading movie descriptions from the movies.txt file and storing them in movies list
movies = []
with open("movies.txt", "r") as f:
    for lines in f:
        movie = f.readline()
        movies.append(movie)

# movie description that will me compared to the movies list
watched = ["Planet Hulk", "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"]

# defining most_similar function that will compare a movie description
# given as an argument to the list of movies stored in the file
def most_similar(watched):
    # a list to store values of comparison that will be used to find index of 
    # the most similar movie
    similarity = []
    # loop that goes trough all of the movies in the movies list
    for movie in movies:
        movie = movie.strip("\n")
        # splitting movie title from the description
        movie = movie.split(":")
        description = movie[1]
        watched_des = (watched[1])
        # tokenizing descriptions to be compared
        watched_des = nlp(watched_des)
        description = nlp(description)
        sim = watched_des.similarity(description)
        # appending similarity list with .similarity result
        similarity.append(sim)
        # finding index of largest(most similar) description
        i = similarity.index(max(similarity))
    # returning title of the most similar movie in the movies list
    m_similar = movies[i]
    m_similar = m_similar.split(":")
    return m_similar[0]

print(f"The most similar movie to {watched[0]} is {most_similar(watched)}.")

