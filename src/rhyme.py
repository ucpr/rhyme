#!/usr/bin/env/python3

import os
import shutil
import sys
import marisa_trie

from words import roman_dict as rd

HIRAGANA = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとど \
        なにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんー"

def _is_hiragana(s):
    return all([ch in HIRAGANA for ch in s])

def _vowel_str(word):
    _roman_list = [rd[i] for i in word]
    _vowel_list = []

    for i in _roman_list:
        for j in "aiueon":
            if j in i:
                _vowel_list.append(j)
                break

    return "".join(_vowel_list)

def _make_rhyme_words(w):
    files = os.listdir("./dictionary/")
    vowel_word = _vowel_str(w)
 
    for i in files:
        with open("./dictionary/" + i, "r", encoding="utf-8") as f:
            trie = marisa_trie.Trie(list(f))
            if not os.path.isdir("../rhyme_words"):
                os.mkdir("../rhyme_words")

            with open("../rhyme_words/" + i[0] + ".txt", "w", encoding="utf-8") as new_f:
                res = trie.keys(vowel_word)
                for r in res:
                    new_f.write(r)
                print("add ./../rhyme_words/{}".format(i[0] + ".txt"))

def rhyme():
    try:
        w = sys.argv[1]
    except IndexError:
        print("引数にひらがなの文字列を与えてください.")
        sys.exit()

    if not _is_hiragana(w):
        print("error : ひらがなではありません.")
        sys.exit()

    _make_rhyme_words(w)
    
if __name__ == "__main__":
    rhyme()
