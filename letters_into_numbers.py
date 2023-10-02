from functools import reduce

def ofDNA(letters: str):
    def transform_one_letter(letter):
        if letter == 'A':
            return [0]
        if letter == 'C':
            return [1]
        if letter == 'T':
            return [2]
        if letter == 'G':
            return [3]
        raise ValueError('As letras inseridas têm de ser A ou C ou T ou G')

    return reduce(lambda x, y: x + y, list(map(lambda letter: transform_one_letter(letter), letters)), [])