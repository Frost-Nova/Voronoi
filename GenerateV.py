'''
Created on Nov 8, 2017

@author: lihy
'''
from PIL import Image
import random
import math

im1 = Image.open("sunset.jpg")

def generate_voronoi_diagram(img,num_cells):
    im=img
    w=im.width
    h=im.height
    r=[[0 for i in range(w)]for j in range(h)]
    g=[[0 for i in range(w)]for j in range(h)]
    b=[[0 for i in range(w)]for j in range(h)]
    
    image = Image.new("RGB", (w, h))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for i in range(num_cells):
        nx.append(random.randrange(imgx))
        ny.append(random.randrange(imgy))
        (r[ny[i]][nx[i]],g[ny[i]][nx[i]],b[ny[i]][nx[i]])=im.getpixel((nx[i],ny[i]))
        nr.append(r[ny[i]][nx[i]])
        ng.append(g[ny[i]][nx[i]])
        nb.append(b[ny[i]][nx[i]])
    for y in range(imgy):
        for x in range(imgx):
            dmin = math.hypot(imgx-1, imgy-1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(nx[i]-x, ny[i]-y)
                if d < dmin:
                    dmin = d
                    j = i
            putpixel((x, y), (nr[j], ng[j], nb[j]))
    image.save("sunset50000.png", "PNG")
    image.show()

generate_voronoi_diagram(im1, 50000)

print('Finished!')
im1.close()
