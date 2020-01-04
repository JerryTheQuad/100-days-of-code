def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

def percent(word, text):
    return 100 * text.count(word) / len(text)

def vocab_size(text):
    return print(len(set(text)))

def lexical_diversity(text):
    word_count = len(text)
    vocab_size = len(set(text))
    diversity_score = vocab_size / word_count
    return diversity_score
