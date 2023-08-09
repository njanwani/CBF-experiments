#!/usr/bin/env python3

import ImageTransferService
import numpy as np
import cv2, time
import tkinter as tk
from PIL import Image, ImageTk

host = '0.0.0.0' # this is here as an open signal for images (will accept data from anywhere i think)
src = ImageTransferService.ImageTransferService(host)
n = 3

# A root window for displaying objects
root = tk.Tk() 
root.geometry('1000x500')
imgtk = None
lbl = None
def poll():
    global root, imgtk, src, lbl
    # Load an color image
    im = src.receiveImage()
    # print(type(im))
    im = np.array([np.kron(im[:,:,0], np.ones((n,n))),
                    np.kron(im[:,:,1], np.ones((n,n))),
                    np.kron(im[:,:,2], np.ones((n,n)))])
    im = np.transpose(im, (1,2,0))

    #Rearrang the color channel
    b,g,r = cv2.split(im)
    im = cv2.merge((r,g,b))
    
    # Convert the Image object into a TkPhoto object
    img = Image.fromarray(im.astype(np.uint8))
    imgtk = ImageTk.PhotoImage(image=img)
    lbl.configure(image=imgtk)
    lbl.image = imgtk
    root.after(1000 // 24, poll)
    
# Put it in the display window
lbl = tk.Label(root, image=imgtk)
lbl.pack()
poll()

root.mainloop() # Start the GUI


    # # Check Redis is running 
    # print(src.ping())
    # n = 5
    # while True:
    #     im = src.receiveImage()
    #     # print(type(im))
    #     im = np.array([np.kron(im[:,:,0], np.ones((n,n))),
    #                    np.kron(im[:,:,1], np.ones((n,n))),
    #                    np.kron(im[:,:,2], np.ones((n,n)))])
    #     im = np.transpose(im, (1,2,0))
    #     # print(im)
    #     # print()
    #     cv2.imshow('Image',im.astype(np.uint8))
    #     cv2.waitKey(1)
    #     # time.sleep(1 / 30)
    #     # break