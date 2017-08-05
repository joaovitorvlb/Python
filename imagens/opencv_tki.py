import Tkinter as tk
import cv2
import numpy as np
 
root = tk.Tk()
 
def captureVideo():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('Exemplo',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
 
 
button = tk.Button(root, text='Capturar video', command=captureVideo)
button.grid(row=0, column=0)
 
root.mainloop()
