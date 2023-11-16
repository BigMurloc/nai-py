import numpy as np

import data_initializer
from scipy.stats import pearsonr

candidates = data_initializer.initialize_data_from_json()


def find_candidate(name):
    for candidate in candidates:
        if candidate.name == name:
            return candidate
    return None


def find_common_movies(candidate, other_candidate):
    """Do set intersection to find common movies"""
    return set(candidate.recommendations.keys()) & set(other_candidate.recommendations.keys())


def create_common_scoring(candidate, other_candidate, commonMovies):
    """Extracts scoring for common movies and returns it accordingly to the index"""
    candidate_recommendations = []
    other_candidate_recommendations = []

    for movie in commonMovies:
        candidate_recommendations.append(candidate.recommendations[movie])
        other_candidate_recommendations.append(other_candidate.recommendations[movie])

    return np.array(candidate_recommendations, dtype=float), np.array(other_candidate_recommendations, dtype=float)


chosen_candidate = find_candidate("Dominik Pasymowski")

correlations = {}
for other_candidate in candidates:
    if other_candidate != chosen_candidate:
        common_movies = find_common_movies(chosen_candidate, other_candidate)
        chosen_candidate_scoring, other_candidate_scoring = create_common_scoring(
            chosen_candidate,
            other_candidate,
            common_movies
        )
        if len(common_movies) > 2:
            correlation, _ = pearsonr(chosen_candidate_scoring, other_candidate_scoring)
            correlations.update({other_candidate.name: correlation})

print(correlations)
max_correlation = max(correlations, key=correlations.get)
min_correlation = min(correlations, key=correlations.get)
print(max_correlation)
print(min_correlation)