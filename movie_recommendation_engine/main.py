
from engine import find_recommended_movies_for_candidate, find_not_recommended_movies_for_candidate

candidate_name = input("Enter your name: ")

pearson_recommended_movies, euclidean_recommended_movies = find_recommended_movies_for_candidate(candidate_name)
pearson_not_recommended_movies, euclidean_not_recommended_movies = find_not_recommended_movies_for_candidate(candidate_name)

print("Pearson based:")
print("Recommended:")
print(pearson_recommended_movies)
print("Not recommended:")
print(pearson_not_recommended_movies)
print("Euclidean based:")
print("Recommended:")
print(euclidean_recommended_movies)
print("Not recommended:")
print(euclidean_not_recommended_movies)
