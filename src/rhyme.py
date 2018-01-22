#!/usr/bin/env/python3

import os
import marisa_trie
from pykakasi import kakasi

kakasi_py = kakasi()
kakasi_py.setMode('H', 'a')
kakasi_py.setMode('K', 'a')
kakasi_py.setMode('J', 'a')
conv = kakasi_py.getConverter()


def _roman_str(text):
    """ 与えられた文字列をローマ字に変換して返す """
    return conv.do(text)


def _vowel_str(word):
    """ 母音のみの文字列にして返す """
    vowel_str = ""
    for i in _roman_str(word):
        if i in "aiueon-":
            vowel_str += i

    return vowel_str


def _make_rhyme_words(w):
    """ 韻を踏んでいそうな単語を探索してリストで返す """
    files = os.listdir("src/dictionary/")
    vowel_word = _vowel_str(w)
    vowel_length = len(vowel_word)
    rhyme_words = []

    for i in files:
        with open("src/dictionary/" + i, "r") as f:
            trie = marisa_trie.Trie(list(f))
            res = trie.keys(vowel_word)

            for j in res:
                tmp = j.split()
                if len(tmp[0]) == vowel_length:  # 母音が全一致の場合のみ
                    rhyme_words.append(tmp[1])

    return rhyme_words


def rhyme(text):
    """ 韻を踏んでいそうな単語をリストで返す """
    roman = _roman_str(text)
    return _make_rhyme_words(roman)


if __name__ == "__main__":
    res = rhyme("沖縄")
    print(res)
