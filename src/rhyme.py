#!/usr/bin/env/python3

import os
import shutil
import sys
import marisa_trie

from words import roman_dict as rd

HIRAGANA = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとど \
        なにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんー"
IGNORE = "っ"
PETIT = "ぁぃぅぇぉっゃゅょゎ"

def _is_hiragana(s):
    return all([ch in HIRAGANA for ch in s])

def _is_connectable(c):
    return c not in IGNORE and c in PETIT

def _split_mora(word):
    mora_list = []
    length = len(word)

    i = 0
    while i < length:
        if i + 1 < length:
            if _is_connectable(word[i + 1]):
                mora_list.append(word[i] + word[i + 1])
                i += 2
            else:
                mora_list.append(word[i])
                i += 1
        else:
            mora_list.append(word[i])
            i += 1

    return mora_list

def _vowel_str(word):
    _vowel_list = []

    for i in _split_mora(word):
        vowel = rd[i][-1]
        if i not in IGNORE and vowel in "aiueon":
            _vowel_list.append(vowel)
        elif vowel == "-":
            _vowel_list.append(_vowel_list[-1])

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
    word = ""
    with open("./../input.txt", "r", encoding="utf-8") as f:
        word = f.readline().rstrip()
        print(word)

    if not _is_hiragana(word):
        print("error : ひらがなではありません.")
        sys.exit()
    
    _make_rhyme_words(word)
    
if __name__ == "__main__":
    rhyme()
