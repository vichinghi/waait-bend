from fuzzywuzzy import fuzz, process

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


def get_match(string, keywords, score_cutoff=70):
    results = process.extractBests(
        string, keywords, score_cutoff=score_cutoff, limit=5)
    if results:
        return True
    return False
