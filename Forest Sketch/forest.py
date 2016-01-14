__author__ = 'SAHIL JASROTIA, LOKESH AGRAWAL'
#CSCI-603: Assignment 2

import turtle as t
import random
import math

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
maxheight = 0
maxtrees = 0

def init():
    """
    This function initializes the Position of turtle and sets the window
    co-ordinates
    :pre: pos (0,0), heading (east), up
    :post: pos (-300,-100), heading (east), up
    :return: None
    """
    t.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    t.up()
    t.setpos(-300,-100)
    t.setheading(0)
    t.title('ForestHome')

def makePolygon(sides,length):
    '''
    This function draws polygon with n sides and length l
    :param sides: number of sides of a polygon
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :param length: length of each side of a polygon
    :return:none
    '''
    t.down()
    if(sides == 0):
       t.circle(length)
    else:
        perAngel = ((sides-2)*180)/sides
        t.forward(length/2)
        for i in range(sides):
            t.left(180-perAngel)
            t.forward(length)
        t.backward(length/2)
    t.up()

def treeType(type):
    """
    This function draws a tree randomly
    :param type: type is any integer between 1-3
    :pre: pos (0,0), heading (east), up
    :post: pos (100,0), heading (east), up
    :return: wood used to make the tree
    """
    global maxheight
    randvalue = 0
    if type == 1:
        randvalue = random.randint(50, 200)
        makeTrunk(randvalue)
        makePolygon(3, 50)
    if type == 2:
        randvalue = random.randint(50, 150)
        makeTrunk(randvalue)
        makePolygon(4, 50)
    if type == 3:
        randvalue = random.randint(50, 150)
        makeTrunk(randvalue)
        makePolygon(0, 25)

    t.right(90)
    t.forward(randvalue)
    t.left(90)
    t.forward(100)
    if randvalue + 50 > maxheight:
        maxheight = randvalue + 50
    return randvalue

def makeHome(length):
    '''
    This function makes home with length of wall as length
    and length of roof as length/sqrt(2)
    :param length: length of wall of a home
    :pre: pos (0,0), heading (east), up
    :post: pos (100,0), heading (east), up
    :return:total wood used to draw home
    '''
    t.down()
    t.left(90)
    t.forward(length)
    t.right(45)
    t.forward(math.sqrt(math.pow(length/2, 2) + math.pow(length/2, 2)))
    t.right(90)
    t.forward(math.sqrt(math.pow(length/2, 2) + math.pow(length/2, 2)))
    t.right(45)
    t.forward(length)
    t.left(90)
    t.up()
    t.forward(100)

    return 2 * length + 2 * math.sqrt(math.pow(length/2, 2) + math.pow(length/2, 2))

def makeStar():
    '''
    This function draws a star at height of 10 pixels higher than
    maximum height of any object(included height of leaves)
    :param: None
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return:none
    '''
    t.backward(100)
    t.left(90)
    t.forward(maxheight + 10)
    t.down()
    t.forward(5)
    for i in range(0, 8):
        t.forward(5)
        t.backward(5)
        t.right(45)
    t.hideturtle()
    t.up()

def makeTree():
    '''
    This function draws any tree randomly
    :param: None
    :pre: pos (0,0), heading (east), up
    :post: pos (100,0), heading (east), up
    :return: wood used for making a tree
    '''
    type = random.randint(1, 3)
    treewood = treeType(type)
    return treewood

def makeTrunk(length):
    '''
    This function draws trunk of a tree with length l which varies with the
    type of tree:
    Pine Tree: min length:50; max length:200
    Maple Tree: min length:50; max length:150
    Custom Tree: min length:50; max length:150
    :param length: length of trunk of a tree
    :pre: pos (0,0), heading (east), up
    :post: pos (0,length), heading (east), up
    :return:none
    '''
    t.down()
    t.left(90)
    t.forward(length)
    t.right(90)
    t.up()

def makesun(height, radius):
    '''
    This function draws a sun
    :param height: total height of home made during day
    :param radius: radius of sun(circle)
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    '''
    t.left(90)
    t.forward(height + 20)
    t.down()
    t.circle(radius)
    t.up()
    t.right(90)
    t.forward(height + 20)
    t.left(90)

def main():
    '''
    The main function
    :return: None
    '''
    treewood = 0
    homewood = 0
    init()
    numtrees = int(input("How many trees in the forest?"))
    ishouse = input("Is there a house in the forest (y/n)?")
#Special case: if number of trees entered by user is 1
    if numtrees == 1:
        if ishouse == "y":
            homewood = makeHome(100)
        treewood = treewood + makeTree()
#If number of trees>1
    else:
#Position of home is selected randomly
        homepos = random.randint(2,numtrees)
        for i in range(1, numtrees+1):

#Whenever home position and the number of tree which turtle is going to make
#matches then home is made first

            if i==homepos and ishouse == "y":
                homewood = makeHome(100)
#Total wood is getting stored in "treewood" for each loop
            treewood = treewood + makeTree()
#After making all trees and homes, a star is made
    makeStar()

#For making home in day

    input("Night is done, press enter for day")
#Resets the turtle
    t.reset()

    totalwood = treewood + homewood

    print ("We have %s units of lumber for building." % totalwood)
#Calculating length of wall of home
    daytimewood = totalwood / (2 + math.sqrt(2))

    print("We will build a house with walls %s tall." % daytimewood)
    makeHome(daytimewood)
#After making home in day, sun rises
    makesun((daytimewood+daytimewood/2), 20)
    input("Day is done, house is built, press enter to quit")


if __name__ == '__main__':
    main()