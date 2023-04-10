#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
from pprint import pprint
import random
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters() -> list:
    return [random.choice(POUCH) for _ in range(NUM_LETTERS)]


def get_possible_dict_words(draw: list):
    all_w = _get_permutations_draw(draw)
    ret = []
    for w in all_w:
        if w.lower() in DICTIONARY:
            ret.append(w)
    return list(set(ret))


def _get_permutations_draw(draw: list):
    ret = []
    for n in range(1, NUM_LETTERS + 1):
        ret.extend("".join(p) for p in itertools.permutations(draw, n))
    return ret


def _validation(word: str, draw: list):
    if word not in get_possible_dict_words(draw):
        raise ValueError


def get_score_for_word(word: str):
    return sum([LETTER_SCORES[let] for let in word.upper()])


def main():
    d = draw_letters()
    print(f"Letters drawn: {', '.join(d)}")

    user_w = input("Form a valid word: ").upper()
    try:
        _validation(draw=d, word=user_w)
    except ValueError:
        print(f"invalid word: {user_w}")
        exit(1)
    user_w_val = get_score_for_word(user_w)
    print(f"Word chosen: {user_w} (value: {user_w_val})")

    perms = get_possible_dict_words(d)
    perm_scores = [(w, get_score_for_word(w)) for w in perms]

    optimal = max(perm_scores, key=lambda p: p[1])
    # pprint(sorted(perm_scores, key=lambda p: p[1]))
    # pprint(optimal)

    print(f"Optimal word possible: {optimal[0]} (value: {optimal[1]})")
    print(f"You scored: {user_w_val/optimal[1]*100:.1f}")


if __name__ == "__main__":
    main()
