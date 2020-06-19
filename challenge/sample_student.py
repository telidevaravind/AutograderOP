
import numpy as np
import sys
sys.path.append('..')
from util.filters import filter_2d

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
    if count>1360:
        return classes[1]
    elif count>1000 and count<=1360 :
        return classes[2]
    elif count<999:
        return classes[0]
    
    #Let's guess randomly! Maybe we'll get lucky.
   # labels = ['brick', 'ball', 'cylinder']
    #random_integer = np.random.randint(low = 0, high = 3)
    
   # return labels[random_integer]