#!/usr/bin/env/python3

import os
from typing import List
import marisa_trie
from pykakasi import kakasi

kakasi_py = kakasi()
kakasi_py.setMode('H', 'a')
kakasi_py.setMode('K', 'a')
kakasi_py.setMode('J', 'a')
conv = kakasi_py.getConverter()


def _converting_to_roman(word: str) -> str:
    """ 与えられた単語をローマ字に変換して返す """
    return conv.do(word)


def _fetch_vowel(word: str) -> str:
    """ 母音のみの文字列にして返す """
    vowel_str = ""
    for i in _converting_to_roman(word):
        if i in "aiueo":
            vowel_str += i
    return vowel_str


def _find_rhyme_words(word: str) -> List:
    """ 韻を踏んでいそうな単語を探索してリストで返す """
    files = os.listdir("./dictionary/")
    vowel_word = _fetch_vowel(word)
    vowel_length = len(vowel_word)
    rhyme_words = list()

    for i in files:
        with open("./dictionary/" + i, "r") as f:
            trie = marisa_trie.Trie(list(f))
            res = trie.keys(vowel_word)

            for j in res:
                tmp = j.split()
                if len(tmp[0]) == vowel_length:  # 母音が全一致の場合のみ
                    rhyme_words.append(tmp[1])
    return rhyme_words


def rhyme(word) -> List:
    """ 韻を踏んでいそうな単語をリストで返す """
    return _find_rhyme_words(_converting_to_roman(word))


if __name__ == "__main__":
    import sys
    import random

    if len(sys.argv) > 1:
        res = rhyme(sys.argv[1])
        if len(res) == 0:
            print("韻が踏めなかったYo...実力不足だったYo...")
        else:
            print(sys.argv[1] + " と " + random.choice(res) + " で韻が踏めるかもしれないYo")
    else:
        print("Yo Yo Yo チェケラ!")
