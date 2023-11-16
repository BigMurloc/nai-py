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
    print("Pearson")
    print_correlations(pearson_correlations)
    print("Euclidean")
    print_correlations(euclidean_correlations)
