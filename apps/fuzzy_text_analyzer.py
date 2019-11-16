from fuzzywuzzy import fuzz, process
from .keywords.models import Keyword

keys = ['seizure', 'seized', 'seiz*'
        'confiscation', 'confiscated', 'confiscat',
        "wildlife+seiz*/confiscat*",
        "ivory+seiz*/confiscat*",
        'rhino+seiz*/confiscat*',
        "pangolin*seiz/confiscat*",
        "elephant+tusk",
        "rhino+horn",
        "pangolin+scale",
        "illegal+wildlife+trade",
        "wildlife+trafficking",
        "hunting+trophies", "hunting+trophy"
        "endangered+species",
        "poaching"]


def get_match(string, score_cutoff=80):
    records = Keyword.query.all()
    keywords = [item.word for item in records]
    keywords += keys
    results = process.extractBests(
        string, keywords, score_cutoff=score_cutoff, limit=5)
    if results:
        return True
    return False
