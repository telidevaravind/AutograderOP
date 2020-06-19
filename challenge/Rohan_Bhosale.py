# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:48:43 2019

@author: ROHAN BHOSALE
"""

import numpy as np
import sys
sys.path.append('..')
#It's kk to import whatever you want from the local util module if you would like:
#from util.X import ... 
def filter_2d(im, kernel):

    M = kernel.shape[0] 
    N = kernel.shape[1]
    H = im.shape[0]
    W = im.shape[1]
    
    filtered_image = np.zeros((H-M+1, W-N+1), dtype = 'float64')
    
    for i in range(filtered_image.shape[0]):
        for j in range(filtered_image.shape[1]):
            image_patch = im[i:i+M, j:j+N]
            filtered_image[i, j] = np.sum(np.multiply(image_patch, kernel))
            
    return filtered_image



def classify(im):
    Kx = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

    Ky = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])
    
    gray = np.mean(im/255, axis = 2)
    Gx = filter_2d(gray[20:230,15:250], Kx)
    Gy = filter_2d(gray[20:230,15:250], Ky)
    G = np.sqrt(Gx**2+Gy**2)
    thresh=0.65
    edges = G > thresh
    classes = ['ball', 'brick', 'cylinder']

    count=np.count_nonzero(edges)
    if count>1350:
        return classes[1]
    elif count>1000 and count<=1350 :
        return classes[2]
    elif count<999:
        return classes[0]
        
