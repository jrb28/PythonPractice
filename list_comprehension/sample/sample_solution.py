# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:39:04 2020

@author: Jim
"""


'''
These files contain the red, green, and blue "channels" for an image, respectively, that is 475 pixels tall and 265 pixels wide:
    
    - r.txt
    - g.txt
    - b.txt
    
Create a list of lists of lists where the inner lists are the numberical pixel denities of R, G, and B and render that image using plt.imshow().
    
'''

import matplotlib.pyplot as plt

numRows = 265
numCols = 475

r = open('d:/deleteme/r.txt','r')
g = open('d:/deleteme/g.txt','r')
b = open('d:/deleteme/b.txt','r')

image = []
while True:    
    p_r = r.readline()
    if p_r == '':
        break
    p_r = p_r.strip().split(',')
    p_g = g.readline().strip().split(',')
    p_b = b.readline().strip().split(',')
    if p_r == '':
        break
    image.append([[int(p_r[j]),int(p_g[j]),int(p_b[j])] for j in range(len(p_r))])
          
r.close()
g.close()
b.close()

plt.imshow(image)
plt.show()