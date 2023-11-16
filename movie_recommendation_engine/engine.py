import data_initializer

from correlation import create_pearson_and_euclidean_correlations

candidates = data_initializer.initialize_data_from_json()


def find_candidate(name):
    for candidate in candidates:
        if candidate.name == name:
            return candidate
    return None


def print_correlations(correlations):
    max_correlation = max(correlations, key=correlations.get)
    min_correlation = min(correlations, key=correlations.get)
    print(max_correlation)
    print(min_correlation)


def find_recommended_movies_for_candidate(name):
    chosen_candidate = find_candidate(name)
    pearson_correlations, euclidean_correlations = create_pearson_and_euclidean_correlations(chosen_candidate,
                                                                                             candidates)
    pearson_based_recommendations = create_recommended_movies(chosen_candidate, pearson_correlations)
    euclidean_based_recommendations = create_recommended_movies(chosen_candidate, euclidean_correlations)

    return pearson_based_recommendations, euclidean_based_recommendations


def find_not_recommended_movies_for_candidate(name):
    chosen_candidate = find_candidate(name)
    pearson_correlations, euclidean_correlations = create_pearson_and_euclidean_correlations(chosen_candidate,
                                                                                             candidates)
    pearson_based_recommendations = create_not_recommended_movies(chosen_candidate, pearson_correlations)
    euclidean_based_recommendations = create_not_recommended_movies(chosen_candidate, euclidean_correlations)

    return pearson_based_recommendations, euclidean_based_recommendations


def create_recommended_movies(chosen_candidate, correlations):
    movies = []
    seen_by_chosen_candidates = chosen_candidate.recommendations.keys()
    candidate = find_candidate(max(correlations, key=correlations.get))
    for key in candidate.recommendations:
        if not seen_by_chosen_candidates.__contains__(key) and float(candidate.recommendations[key]) > 7 and len(
                movies) < 5:
            movies.append(key)
    return movies


def create_not_recommended_movies(chosen_candidate, correlations):
    movies = []
    seen_by_chosen_candidates = chosen_candidate.recommendations.keys()
    candidate = find_candidate(min(correlations, key=correlations.get))
    for key in candidate.recommendations:
        if (
                not seen_by_chosen_candidates.__contains__(key)
                and float(candidate.recommendations[key]) > 7
                and len(movies) < 5):
            movies.append(key)
    return movies
