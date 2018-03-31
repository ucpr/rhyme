import sys
import random
from rhyme import rhyme


if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = rhyme(sys.argv[1])
        if len(res) == 0:
            print("韻が踏めなかったYo...実力不足だったYo...")
        else:
            print(sys.argv[1] + " と " + random.choice(res) + " で韻が踏めるかもしれないYo")
    else:
        print("Yo Yo Yo チェケラ!")
