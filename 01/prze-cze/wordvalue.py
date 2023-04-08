from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, "r") as dict_inp:
        ret = dict_inp.read().strip().split("\n")
    return ret


def calc_word_value(word: str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    ret = sum((LETTER_SCORES.get(let.upper(), 0) for let in word))
    return ret


def max_word_value(word_list: list = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list is None:
        word_list = load_words()
    rel = ((w, calc_word_value(w)) for w in word_list)
    return sorted(rel, key=lambda a: a[1], reverse=True)[0][0]


if __name__ == "__main__":
    pass  # run unittests to validate
