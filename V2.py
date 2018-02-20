'''
Created on Dec 5, 2017

@author: lihy
'''
from PIL import Image
import random
import math
import time

class Node:
    def __init__(self):
        self.nx=0
        self.ny=0
        self.nr=0
        self.ng=0
        self.nb=0
        self.near=[]
        
def generateVoronoiArt(img,num_cells):
    w=img.width
    h=img.height
    N=num_cells
    lamda=4*math.sqrt(w*h/N)
    nodeList=[Node() for i in range(N)]
    
    image = Image.new("RGB", (w, h))
    putpixel = image.putpixel
    for i in range(N):
        nodeList[i].nx=random.randrange(w)
        nodeList[i].ny=random.randrange(h)
        (nodeList[i].nr,nodeList[i].ng,nodeList[i].nb)=img.getpixel((nodeList[i].nx,nodeList[i].ny))
    
    for i in range(N):
        for j in range(N):
            d = math.hypot(nodeList[i].nx-nodeList[j].nx, nodeList[i].ny-nodeList[j].ny)
            if d<lamda:
                nodeList[i].near.append(nodeList[j])

    for y in range(h):
        dmin = math.hypot(w-1, h-1)
        j = -1
        for i in range(N):
            d = math.hypot(nodeList[i].nx, nodeList[i].ny-y)
            if d < dmin:
                dmin = d
                j = i
        for x in range(w):
            dmin=w
            for n in nodeList[j].near:
                d = math.hypot(n.nx-x, n.ny-y)
                if d < dmin:
                    dmin = d
                    j=nodeList.index(n)
            putpixel((x, y), (nodeList[j].nr, nodeList[j].ng, nodeList[j].nb))
        
    image.save("download5000.png", "PNG")
    image.show()
    
    for n in nodeList[0].near:
        print(str(n.nx)+' '+str(n.ny))
    print('current node position:'+str(nodeList[0].nx)+','+str(nodeList[0].ny))    
    print('number of nearest node is:'+str(len(nodeList[0].near)))

start = time.time()
im1 = Image.open("download.jpg")
generateVoronoiArt(im1,5000)
im1.close()
end = time.time()

print('Running time is:'+str(end-start))

