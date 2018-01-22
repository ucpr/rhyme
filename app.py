import sys
sys.path.append("src/")

from rhyme import rhyme


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(rhyme(sys.argv[1]))
    else:
        print("Yo Yo Yo チェケラ!")
