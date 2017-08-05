import cv2
import numpy as np

FONTE = cv2.FONT_HERSHEY_SIMPLEX

img_binaria = cv2.imread('formas_binario.jpg')
blurred = cv2.GaussianBlur(img_binaria, (5, 5), 0)

img_binaria_gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

img, cont, hier = cv2.findContours(img_binaria_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for c in cont:
    perimetro = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * perimetro, True)
    cv2.drawContours(img_binaria, [c], -1, (0,255,0), 1)
    x, y, w, h = cv2.boundingRect(c)

    if len(approx) == 3:
        forma = "Triangulo"

    elif len(approx) == 4:
        forma = "Quadrado" if (w/h) >= 0.95 and (w/h) <= 1.05 else "Retangulo"

    elif len(approx) == 5:
        forma = "Pentagono"

    else:
        forma = "Circulo"

    cv2.putText(img_binaria, forma,(x, y), FONTE, 0.5,(0,255,0),1,cv2.LINE_AA)

cv2.imshow('RESULTADO', img_binaria)
cv2.waitKey(0)
