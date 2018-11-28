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
    bird.baseName = foundFiles[x]
    bird.fromFileName = os.path.join(tempPathName, 
                                     bird.baseName + '.cdf')
    bird.toFileName = os.path.join(tempPathName, 
                                   bird.baseName + '.gpl')


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


def readDataFromCDF(bird):
    bird.fromLineList = bird.fromFile.readlines()
    bird.fromFile.close()
    bird.toLineList = []
    for tempLine in bird.fromLineList:
        tempIn = bird.cdfInput.search(tempLine)
        if tempIn:
            newDesc = tempIn.group('rawDesc').rstrip()
            newR = convertColor1to255(float(tempIn.group('rawR')))
            newG = convertColor1to255(float(tempIn.group('rawG')))
            newB = convertColor1to255(float(tempIn.group('rawB')))
            newOut = str(newR).ljust(4) + \
                    str(newG).ljust(4) + \
                    str(newB).ljust(4) + \
                    newDesc + '\n'
            bird.toLineList.append(newOut)
    bird.totalColors = len(bird.toLineList)
    print('readDataFromCDF ok')


def writeDataToGPL(bird):
    line1 = 'GIMP Palette\n'
    line2 = '#Palette Name: '  + \
            bird.baseName.upper() + \
            '\n'
    line3 = '#Description: Converted from ' + \
            bird.baseName +  '.cdf ' + \
            'using toolIndexedPaletteFileConversion.py\n'
    line4 = '#Colors: '+  str(bird.totalColors) + '\n'
    bird.toLineList.insert(0, line1)
    bird.toLineList.insert(1, line2)
    bird.toLineList.insert(2, line3)
    bird.toLineList.insert(3, line4)
    bird.toFile.writelines(bird.toLineList)
    bird.toFile.close()
    

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
        readDataFromCDF(bird)
        writeDataToGPL(bird)
        
        
        print('done')
    except:
        print('ERROR')


if __name__ == "__main__":
    main()