#!/usr/bin/env/python3

import os
import shutil
import sys
import marisa_trie
from docopt import docopt

from words import roman_dict as rd
from doc import __doc__

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
    vowel_list = []

    for i in _split_mora(word):
        vowel = rd[i][-1]
        if i not in IGNORE and vowel in "aiueon":
            vowel_list.append(vowel)
        elif vowel == "-":
            vowel_list.append(vowel_list[-1])

    return "".join(vowel_list)

def _make_rhyme_words(w, state=0):
    files = os.listdir("./dictionary/")
    vowel_word = _vowel_str(w)
    vowel_length = len(vowel_word)
 
    for i in files:
        with open("./dictionary/" + i, "r", encoding="utf-8") as f:
            trie = marisa_trie.Trie(list(f))
            if not os.path.isdir("../rhyme_words"):
                os.mkdir("../rhyme_words")

            with open("../rhyme_words/" + i[0] + ".txt", "w", encoding="utf-8") as new_f:
                res = trie.keys(vowel_word)
                for r in res:
                    tmp = r.split()
                    if vowel_length < len(tmp[0]):
                        continue
                    new_f.write(tmp[1] + "\n")
                if not state:
                    print("add ./../rhyme_words/{}".format(i[0] + ".txt"))

def _input_word(args):
    word = args["<hiragana_word>"]
    if not word:
        print("Error : 文字列が空文字列です.")
        sys.exit()
    if not _is_hiragana(word):
        print("Error : ひらがなではありません.")
        sys.exit()
    return word

def rhyme():
    args = docopt(__doc__)
    
    if args["--show"]:
        word = _input_word(args)
        _make_rhyme_words(word, 1)
        files = os.listdir("../rhyme_words")
        for f in files:
            with open("../rhyme_words/" + f, "r", encoding="utf-8") as txt:
                for row in txt:
                    print(row.rstrip())
    elif args["--write"]:
        word = _input_word(args)
        _make_rhyme_words(word)
    elif args["--help"]:
        print(__doc__)
    else:
        word = args["<hiragana_word>"]
        if not word:
            print(__doc__)
        else:
            if not _is_hiragana(word):
                print("Error : ひらがなではありません.")
                sys.exit()
            _make_rhyme_words(word)

if __name__ == "__main__":
    rhyme()
