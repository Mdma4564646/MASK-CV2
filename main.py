

from lib2to3.pgen2 import driver
from tkinter import W
from turtle import Screen
import numpy as np
from PIL import ImageGrab
import cv2
import time
from trs import PressKey, ReleaseKey, Left, Down, Up, Right
from matplotlib import pyplot as pltd 


 
t = time.process_time()
print(t)

#k=0

x1 = 300
y1 = 580


def dlines(screen, lines):
 
    
             try:
                for line in lines:
                 cor=line[0]
                cv2.line(screen,(cor[0], cor[1]), (cor[2], cor[3]), [0,255,50], 5)
                global x1, y1
                x1 = lines[0] [0] [0]
                y1 = lines[0] [0] [1]
             except:
                    pass

def maskk(screen, vertex):
    mask = np.zeros_like(screen)
    cv2.fillPoly(mask, vertex, 255)
    mask1 =  cv2.bitwise_and(screen,mask)
    return mask1

                      

while True:
    window = np.array(ImageGrab.grab(bbox = (20,10,800 ,600)))

    print("Время Кадра "+ str(time.process_time()-t))
    t = time.process_time()
    im = cv2.cvtColor(window, cv2.COLOR_BGR2GRAY)
    window1 =cv2.cvtColor(window, cv2.COLOR_BGR2RGB)

    #sobelx = cv2.Sobel(im, cv2.CV_32F, 1,0, ksize=3 )
    #sobely = cv2.Sobel(im, cv2.CV_32F, 0,1, ksize=3 )
    #sob = (sobelx+sobely)

    Can = cv2.Canny (im, 100, 300,7)

    #vertex = np.array([[0,600],[0,500],[300,360],[365,360],[800,540],[800,720]])
    #левая часть
    vertex1 = np.array([[0,490],[0,400],[300,360],[365,590]])
    #середина
    vertex2 = np.array([[0,360],[365,300],[500,360],[0,360]])
    #правая часть
    vertex3 = np.array([[300,360],[500,360],[700,460],[700,360]])



    
   




    Can1 = maskk(Can, [vertex1,vertex2,vertex3])
    lines =  cv2.HoughLinesP(Can1, 1, np.pi/180, 50, 100, 5)
    dlines(window1, lines)

    cv2.line(window1, (x1, y1),(300,590),[100,0,100],5)

    d1 = np.sqrt((x1-490)**2+(y1-590)**2)
    cv2.putText(window1, " " + str(d1)+ " ", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,125,0),2)
    
    #d2 = np.sqrt((x1-360)**2+(y1-590)**2)
    #cv2.putText(window1, " " + str(d2)+ " ", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,175,1),2)
             
    #d3 = np.sqrt((x1-300)**2+(y1-590)**2)wwwww w
    #cv2.putText(window1, " " + str(d3)+ " ", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,115,0),2)
    


    drive = d1
    if d1 > 380:
        PressKey(0x1E)
        time.sleep(0.2) 
        ReleaseKey(0x1E)
        time.sleep(0.2)
    else:
        PressKey(0x1E)
        time.sleep(0.2)
        ReleaseKey(0x1E)
        time.sleep(0.2)   



    cv2.imshow("window_new",window1)
    

    #PressKey(0x11)
    #time.sleep(0.2)
    #ReleaseKey(0xC8)
    #time.sleep(0.2)
    

    if cv2.waitKey(30) ==ord("q"):
        cv2.destroyAllWindows()
    
    
