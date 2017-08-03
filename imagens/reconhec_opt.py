#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from SimpleCV import *
import time
 
 
img = Image("ret.png")
 
blobs = img.findBlobs()
print "Objetos Encontrados --> %i\n" % (len(blobs))
if blobs:
    blobs = blobs[-1]
    print "Angulo do Objeto --> %i\n" % (blobs.angle())
    print "Aplicando rotação para desinclinação da imagem!"
    img = img.smartRotate()    
    bin = img.binarize()
    text = bin.readText()[:-5]
    if text:
        string = "Texto reconhecido da Imagem:-->%s" % (text)
        img.drawText(string,35,15,color=Color.AZURE,fontsize=35)
       
img.show()   
time.sleep(5)