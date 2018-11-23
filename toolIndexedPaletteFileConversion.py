#toolIndexedPaletteFileConversion.py
#(C) 2018 Robin Pruss

import io
import re


class birdClass():
    pass


def setupRegex(bird):
    bird.cdfInput = re.compile(r'''
        (?P<rawDesc>.{34})      #1 description string
        (?P<rawR>.{11})         #2 R value 0.0-1.0
        (?P<rawG>.{11})         #3 G value 0.0-1.0
        (?P<rawB>.{9})          #4 B value 0.0-1.0
        ''', re.I | re.X)
    bird.gplInput = re.compile(r'''
        (?P<rawR>\d+)\s+        #1 R value 0-255
        (?P<rawG>\d+)\s+        #2 G value 0-255
        (?P<rawB>\d+)\s+        #3 B value 0-255
        (?P<rawDesc>.*)         #4 description string
        ''', re.I | re.X)


def chooseFiles(bird):
    bird.fromFileName = r'C:\TEMP\ugcolor.cdf'
    bird.toFileName = r'C:\TEMP\ugcolor_01.gpl'
    pass


def prepareFiles(bird):
    bird.fromFile = io.open(bird.fromFileName, "r", encoding="utf-8")
    bird.toFile = io.open(bird.toFileName, "w", encoding="utf-8")
    pass


def convertColor1to255(color1):
    color255 = round(color1*255.0)
    return(color255)


def convertColor255to1(color255):
    color1 = round(float(color255)/255.0,7)
    return(color1)


def main():
    bird = birdClass()
    setupRegex(bird)
    chooseFiles(bird)
    prepareFiles(bird)
    bird.fromFile.close()
    bird.toFile.close()
    print('done')


if __name__ == "__main__":
    main()