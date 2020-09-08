# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:02:34 2020

@author: Jim
"""


from PIL import Image
import numpy as np

im = Image.open('D:/deleteme/miller-aerial.jpg')
r, g, b = np.array(im).T

for x in [('r.txt',r),('g.txt',g),('b.txt',b)]:
    with open('D:/deleteme/'+ x[0],'w') as f:
        for i in range(len(x[1])):
            f.write(','.join([str(y) for y in x[1][i]]) + '\n')
    