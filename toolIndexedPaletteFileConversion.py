#toolIndexedPaletteFileConversion.py
#(C) 2018 Robin Pruss

import io
import os
import re


class birdClass():
    fromFile = None
    toFile = None


def setupRegex(bird):
    bird.cdfExt = re.compile(r''' 
        (?P<eFN>.*)             #any number of characters
        \.                      #escape for "."
        cdf                     #extension for cdf
        $                       #at end of line
        ''', re.I | re.X)
    bird.cdfInput = re.compile(r'''
        (?P<rawDesc>.{34})      #description string
        (?P<rawR>.{11})         #R value 0.0-1.0
        (?P<rawG>.{11})         #G value 0.0-1.0
        (?P<rawB>.{9})          #B value 0.0-1.0
        ''', re.I | re.X)
    bird.gplInput = re.compile(r'''
        (?P<rawR>\d+)\s+        #R value 0-255
        (?P<rawG>\d+)\s+        #G value 0-255
        (?P<rawB>\d+)\s+        #B value 0-255
        (?P<rawDesc>.*)         #description string
        ''', re.I | re.X)


def chooseFiles(bird):
    
    foundFiles = []
    while foundFiles == []:
        tempPathName = input('Enter a folder path with .cdf files >> ')
        with os.scandir(tempPathName) as thisPath:
            for thisFile in thisPath:
                result = bird.cdfExt.search(thisFile.name)
                if result:
                    foundFiles.append(result.group('eFN'))
    if len(foundFiles) == 1:
        x = 0
    else:
        foundFiles.sort
        for y, z in enumerate(foundFiles):
            print(str(y), ' ', z)
        x = int(input('Which of these files? >> '))
    bird.fromFileName = os.path.join(tempPathName, 
                                     foundFiles[x] + '.cdf')
    bird.toFileName = os.path.join(tempPathName, 
                                   foundFiles[x] + '.gpl')


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
    print('''Welcome to toolIndexedPaletteFileConversion.py
        Copyright 2018, Robin Pruss
        Licensed under the BSD 3-Clause License
        This program currently converts from .cdf to .gpl.\n''')
    try:
        bird = birdClass()
        setupRegex(bird)
        chooseFiles(bird)
        prepareFiles(bird)
        bird.fromFile.close()
        bird.toFile.close()
        print('done')
    except:
        print('ERROR')


if __name__ == "__main__":
    main()