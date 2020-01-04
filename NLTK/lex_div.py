def lexical_diversity(text):
    word_count = len(text)
    vocab_size = len(set(text))
    diversity_score = vocab_size / word_count
    return diversity_score
