import tkinter as tk
from speedometer import Speedometer
from data_transfer import *
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class RiskMap:
    
    def __init__(self, root, remote: DataTransferService, n):
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


class Heartbeat:
    
    topics = ['Mobility Data',
              'IMU Data',
              'Front Lower Cam',
              'Front Upper Cam',
              'VN100 IMU',
              'Pose\t',
              'Elevation Map',
              'Chicane Seg']
    # topics = ['bruh'] * 8
    
    def __init__(self, root, remote: DataTransferService):
        self.root = root
        self.remote = remote
        self.labels = []
        for _ in range(8):
            self.labels.append(tk.Label(root, text='RATES GO HERE',font=('Courier', 13))) #borderwidth=2,relief="groove"))
            self.labels[-1].pack(anchor='w')
        self.poll()
        
    def poll(self):
        rates = self.remote.receive_rate()
        for label, r, topic in zip(self.labels, rates, Heartbeat.topics):
            label.config(text=f'{topic}\t{r:<1.1f}\tHz')
            if r < 0.05:
                label.config(fg='red')
            else:
                label.config(fg='white')
        # self.label.config(text='\n'.join(rates.astype(str)))
        self.root.after(1000 // 100, self.poll)
        

class Picture:
    
    def __init__(self, root, path, w, h):
        self.root = root
        
        canvas = tk.Canvas(root, width=w, height=h)
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open(path).resize((w, h), Image.ANTIALIAS))
        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
        

class Logos:
    
    def __init__(self, root, caltech, jpl, sandia, darpa, w, h):
        self.root = root
        
        
        
class GaugeChart:
    
    def __init__(self, root, remote):
        self.label = tk.Label(root)
        self.label.pack()
        self.root = root
        self.remote = remote
        self.vx = 0
        self.poll()
        
    def poll(self):
        self.vx = self.remote.receive_vx()
        im = np.zeros((500, 500, 4))
        im = cv2.circle(im, (250, 250), 180, (0,0,255,255), 15)
        r = 150
        for theta in np.linspace(np.pi/2, np.pi/2 + self.vx * 2 * np.pi, 40):
            im = cv2.line(im,
                          (int(r * np.cos(theta) + 250), int(r * np.sin(theta) + 250)),
                          (int(r * np.cos(theta + 0.15) + 250), int(r * np.sin(theta + 0.15) + 250)),
                          (abs((theta - np.pi/2) / (2 * np.pi)) * 255, 255 - abs((theta - np.pi/2) / (2 * np.pi)) * 255, 0, 255),
                          10)
        im = cv2.putText(im, f'{self.vx:.2f}', (200, 260), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255, 255), 2, cv2.LINE_AA)
        img = Image.fromarray(im.astype(np.uint8)).resize((150, 150))
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.configure(image=imgtk)
        self.label.image = imgtk
        self.root.after(1000 // 24, self.poll)