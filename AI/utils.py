import math, re
from json import load
from collections import Counter

WORD = re.compile(r"\w+")

with open('AI\\config.json', 'r', encoding='utf-8') as config_file:
    config = load(config_file)


def generate_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def filter(text):
    text = text.lower()
    
    for key, value in config['char_guide'].items():
        for letter in value:
            text = text.replace(letter, key)
    
    for word in config['ban_words']:
        if word in text:
            return 110
    
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)

    return text


def similarity_cosine(input, response):
    input, response = filter(input), filter(response)

    if input == 110: return 110

    vec1, vec2 = generate_vector(input), generate_vector(response)

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    return float(numerator) / denominator