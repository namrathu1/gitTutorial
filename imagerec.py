# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:29:23 2018

@author: SmithaK
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce
from collections import Counter

#i = Image.open('images/dot.png')
'''i = Image.open('images/numbers/y0.4.png')
iar = np.asarray(i)

print (iar)
plt.imshow(iar)
plt.show()'''


def createExample():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)
    
    for eachNum in numbersWeHave:
        for eachVersion in versionsWeHave:
           # print (str(eachNum)+'.'+str(eachVersion))
           imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVersion)+'.PNG'
           ei = Image.open(imgFilePath)
           eiar = np.array(ei)
           eiar1 = str(eiar.tolist())
           
           lineToWrite = str(eachNum)+'::'+eiar1+'\n'
           numberArrayExamples.write(lineToWrite)
    
    
#Convert color image to black and white
def threshold(imageArray):
    balanceArr = []
    newArr = imageArray
    
    for eachRow in imageArray:
        for eachPixel in eachRow:
            avgnum = reduce(lambda x,y:x+y, eachPixel[:3])/len(eachPixel[:3])
            balanceArr.append(avgnum)
            '''print(eachPixel)
            time.sleep(5)'''
    balance = reduce(lambda x,y:x+y, balanceArr)/len(balanceArr)
          
            
            
    for eachRow in newArr:
        for eachPixel in eachRow:
            if reduce(lambda x,y:x+y, eachPixel[:3])/len(eachPixel[:3])> balance:
                eachPixel[0] = 255
                eachPixel[1] = 255
                eachPixel[2] = 255
                eachPixel[3] = 255
                
            else:                
                eachPixel[0] = 0
                eachPixel[1] = 0
                eachPixel[2] = 0
                eachPixel[3] = 255
                
    return newArr


def whatNumIsThis(filePath):
    matchedArr=[]
    loadExamples = open('numArEx.txt','r').read()
    loadExamples = loadExamples.split('\n')
    
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    
    inQuestion = str(iarl)
    
    for eachExmple in loadExamples:
        if len(eachExmple) >3:
            
            splitEx = eachExmple.split('::')
            currentNum = splitEx[0]
            currentArr = splitEx[1]
            
            eachPixExample = currentArr.split('],')
            
            eachPixInQuestion = inQuestion.split('],')
            
            x = 0
            print(currentNum)
            while x < len(eachPixExample):
                if eachPixExample[x] == eachPixInQuestion[x]:
                    matchedArr.append(int(currentNum))
                    
                x += 1
                
                
    print (matchedArr)
    x = Counter(matchedArr)
    print(x)
    
    
    graphX = []
    graphY = []
    
    for eachThing in x:
        print(eachThing)
        graphX.append(eachThing)
        print(x[eachThing])
        graphY.append(x[eachThing])
        
    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')
    plt.ylim(400)
    
    xloc = plt.MaxNLocator(12)
    
    ax2.xaxis.set_major_locator(xloc)
    plt.show()
    
    
    
    
whatNumIsThis('images/test.png')
    
    
    
    
'''i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)
            
threshold(iar2)
threshold(iar3)
threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()'''