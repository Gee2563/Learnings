# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# * Use the material, Python Docs and Google as much as you want

# == EXERCISES ==

# Purpose: Use Python libraries to request the provided URL, convert the
#          response data to JSON, and return the data.
# Example:
#   Call:    load_data_from_url("https://example.org/my.json")
#   Returns: A JSON object
import json
import os
from urllib.request import urlopen
def load_data_from_url(url):
    url = urlopen(f'{url}')
    response = url.read().decode('UTF-8')
    return json.loads(response)

# Purpose: Use Python libraries to open the specified file, convert the
#          data to JSON, and return the data.
# Example:
#   Call:    load_data_from_file("my_test_data.json")
#   Returns: A JSON object
def load_data_from_file(filename):
    with open(f'/Users/georgesmith/Projects/python_foundations/python_foundations/extension_challenges/02_json/program/lib/{filename}') as myFile:
        return json.load(myFile)

# Purpose: Load the sample JSON from file, and returns a list of films 
#           directed by the named person.
# Example:
#   Call:    get_films_by_director("my_test_data.json", "Olivia Wilde")
#   Returns: ["Booksmart, "Don't Worry Darling"]
def get_films_by_director(filename, director):
    data = load_data_from_file(filename)
    return [film['name'] for film in data if film['director'] == director]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           starring the named person.
# Example:
#   Call:    get_films_by_actor("my_test_data.json", "Dwayne Johnson")
#   Returns: ["Jumanji", "Jungle Cruise"]
def get_films_by_actor(filename, desired_actor):
    data = load_data_from_file(filename)
    return [film['name'] for film in data if desired_actor in  film['stars']]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           with a rating which is AT LEAST the value specified.
# Example:
#   Call:    get_films_with_minimum_rating("test.json", 9.3)
#   Returns: ["The Shawshank Redemption"]
def get_films_with_minimum_rating(filename, rating):
    data = load_data_from_file(filename)
    return [film['name'] for film in data if film['imdb_rating'] >= rating]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           which were released during the specified years.
# Example:
#   Call:    get_films_within_year_range("my_test_data.json", 1994, 1996)
#   Returns: ["The Lion King", "Independence Day"]
def get_films_within_year_range(filename, start_year, end_year):
    data = load_data_from_file(filename)
    return [film['name'] for film in data if start_year <= film['year'] <=end_year]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           in order of the year that they were released.
# Example:
#   Call:    order_films_chronologically("test.json")
#   Returns: ["12 Angry Men", "The Godfather", "The Godfather: Part II", ... ]
def order_films_chronologically(filename):
    data = load_data_from_file(filename)
    filtered =  [(film['year'],film['name']) for film in data]
    return [film[1] for film in sorted(filtered)]


# Purpose: Load the sample JSON from file, and returns a list of films 
#           starting with the most recent.
# Example:
#   Call:    order_films_most_recent_first("test.json")
#   Returns: ["The Dark Knight", "The Shawshank Redemption", "The Godfather: Part II", ... ]
def order_films_most_recent_first(filename):
    a =  order_films_chronologically(filename)
    return a[::-1]
# Purpose: Load the sample JSON from file, and returns a deduplicated list 
#           of all the actors whose name begins with that letter,
#           in alphabetical order.
# Example:
#   Call:    all_actors_starting_with_letter("test.json", "a")
#   Returns: ["Aaron Eckhart, "Al Pacino"]
def all_actors_starting_with_letter(filename, letter):
    data = load_data_from_file(filename)
    stars_in_film = [film['stars'] for film in data]
    result  = []
    for actors in stars_in_film:
        for actor in actors:
            if actor[0].lower() == letter and actor not in result:
                result.append(actor)
                print(result)
    return sorted(result)
