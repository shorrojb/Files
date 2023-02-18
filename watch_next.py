import spacy

nlp = spacy.load('en_core_web_md')

def find_similar_movie(description):
    # Load the movies from the file
    with open('movies.txt', 'r') as f:
        movies = [line.strip() for line in f.readlines()]

    # Calculate the similarity between the description and each movie
    similarities = [(movie, nlp(description).similarity(nlp(movie))) for movie in movies]

    # Return the title of the most similar movie
    return max(similarities, key=lambda x: x[1])[0]


#To use the function, you can call it with the description of the movie you've watched:

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = find_similar_movie(description)
print("You should watch", similar_movie, "next!")
#This will print the title of the movie that is most similar to the one you've watched.