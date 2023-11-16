import data_initializer

candidates = data_initializer.initialize_data_from_json()


def find_candidate(name):
    for candidate in candidates:
        if candidate.name == name:
            return candidate
    return None


def find_common_movies(candidate, otherCandidate):
    """Do set intersection to find common movies"""
    return set(candidate.recommendations.keys()) & set(otherCandidate.recommendations.keys())


chosen_candidate = find_candidate("Dominik Pasymowski")
