import pygame
pygame.init()
from tetparser import tetParser

class configData():
    configObj = tetParser()
    configObj.compile()
    data = configObj.data_map
    colorsArr = configObj.colors
    pointsArr = configObj.points

    print("Printing from config file")
    print(colorsArr)
    print(data)

    black = data['screenColor']
    white = data['scoreColor']
    colors = tuple(colorsArr)


    # Sizes
    blockSize = int(data['blockSize'])
    border = 1
    rows = int(data['rows'])
    cols = int(data['cols'])
    screenHeight = rows*blockSize
    screenWidth = cols*blockSize + 200
    screenSize = (screenWidth, screenHeight)
    fontSize = int(data['fontSize'])
    orderThickness = 2

    # Speed
    tickInterval = int(data['tickInterval'])
    delay = int(data['delay'])
    repeat = int(data['repeat']) 
    speed = float(data['speed'])

    pygame.key.set_repeat(delay, repeat)


    # Miscellaneous
    emptyColor = black
    boundaryColor = data['boundaryColor']
    borderColor = data['colorBorder']
    borderThickness = int(data['thicknessBorder'])
    emptyCell = (emptyColor, 0)
    boundaryCell = (boundaryColor, 0)
    points = pointsArr
    score = int(data['score'])

    singlePlayer = data['SINGLE_PLAYER']