#toolIndexedPaletteFileConversion.py
#(C) 2018 Robin Pruss

import math
import re


class birdClass():
    pass


def setupRegex(bird):
    bird.cdfInput = re.compile(r'(.{34})(.{11})(.{11})(.{9})', flags=re.I)


def main():
    bird = birdClass()
    setupRegex(bird)
    print('done')


if __name__ == "__main__":
    main()