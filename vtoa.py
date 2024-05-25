#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[7]:


import cv2
import tkinter as tk
from tkinter import font
import numpy as np





def createWindow():
    # Create a window
    window = tk.Tk()

    # Set the window title
    window.title("ASCII")

    # Set the window size
    window.geometry("1280x720")
    window.configure(bg="black")

    return window

# Open camera
window = createWindow()
cap = cv2.VideoCapture(0)

label = tk.Label(window, text="", font=("Consolas", 12), fg="green", bg="black")
label.pack()

# Check
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read() #read the frames 
    
    ascii_list = [' ', '.', "'", ',', ':', ';', 'c', 'l','x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N'] # list the asciis 


    if ret:
        ht, wth, channel = frame.shape
        ratio = (ht / wth) / 2
        newWth = 100
        newHt = int(ratio * newWth)
        frame = cv2.resize(frame, (newWth, newHt), cv2.INTER_CUBIC)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        asciiframe = ''
        
        for y in range(newHt): #over rows
            for x in range(newWth): #over coloumns 
                brightness = np.clip(int(frame[y, x]/25.5), 0, 10) #ensure specified range
                asciiframe += ascii_list[brightness] #mapping to ascii lower the brightness smaller(?) the character
            asciiframe += "\n" #build each row

        label.config(text=asciiframe)
        window.update() #uodate for every frame 

    else:
        print("Error")

    
    
    # q to exit loop 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close all windows
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




