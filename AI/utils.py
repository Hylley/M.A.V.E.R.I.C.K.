import math, re
from collections import Counter


WORD = re.compile(r"\w+")

filter_guide = [
    ('a', 'á à â ã ä'),
    ('e', 'é è ê ë'),
    ('i', 'í ì ï î'),
    ('o', 'ó ò ö ô õ'),
    ('u', 'ú ù ü û')
]

def generate_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def filter(text):
    text = text.lower()

    for i in range(len(filter_guide)):
        for letter in filter_guide[i][1].split():
            text = text.replace(letter, filter_guide[i][0])
    
    #text = ''.join(ch for ch in text if ch.isalnum() or chr == ' ')

    return text


def similarity_cosine(text1, text2):

    text1, text2 = filter(text1), filter(text2)
    vec1, vec2 = generate_vector(text1), generate_vector(text2)

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    return float(numerator) / denominator