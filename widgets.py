import tkinter as tk
from ImageTransferService import *
from PIL import Image, ImageTk

class RiskMap():
    
    def __init__(self, root, remote, n):
        self.root = root
        self.remote = remote
        self.n = n
        self.label = tk.Label(root)
        self.label.pack()
        self.poll()
        
    def poll(self):
        im = self.remote.receiveImage()
        im = np.array([np.kron(im[:,:,0], np.ones((self.n,self.n))),
                        np.kron(im[:,:,1], np.ones((self.n,self.n))),
                        np.kron(im[:,:,2], np.ones((self.n,self.n)))])
        im = np.transpose(im, (1,2,0))

        b,g,r = cv2.split(im)
        im = cv2.merge((r,g,b))
        
        img = Image.fromarray(im.astype(np.uint8))
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.configure(image=imgtk)
        self.label.image = imgtk
        self.root.after(1000 // 24, self.poll)
        