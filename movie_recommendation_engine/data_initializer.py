import json
from dataclasses import dataclass
from typing import List


@dataclass
class Recommendation:
    """Class for keeping track of movie and its score"""
    movie: str
    score: float

    @staticmethod
    def from_json_data(recommendation):
        return Recommendation(recommendation['movie'], recommendation['score'])


@dataclass
class Candidate:
    """Class for keeping track of a candidate with his movie recommendations"""
    name: str
    recommendations: List[Recommendation]

    @staticmethod
    def from_json_data(candidate):
        name = candidate['name']
        recommendations = []
        for recommendation in candidate['recommendations']:
            recommendations.append(Recommendation.from_json_data(recommendation))
        return Candidate(name, recommendations)


def initialize_data_from_json():
    """Open and load json data from data.json"""
    f = open('data.json')
    data = json.load(f)

    """Initialize array of candidates objects by mapping each json record to python object"""
    candidates = []
    for jsonCandidate in data['people']:
        candidate = Candidate.from_json_data(jsonCandidate)
        candidates.append(candidate)

    """Close file after being done with objects initialization"""
    f.close()

    return candidates
