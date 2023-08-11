import tkinter as tk
import numpy as np
import cv2
import data_transfer

from widgets import *

colors = ['red', 'black', 'blue', 'yellow', 'green']

class App():
    
    REF = 'reference'
    TOP = tk.TOP
    BOTTOM = tk.BOTTOM
    LEFT = tk.LEFT
    RIGHT = tk.RIGHT
    
    def __init__(self, name, size, host='0.0.0.0'):
        self.root = tk.Tk()
        self.root.title(name)
        self.root.geometry(size)
        self.remote = data_transfer.DataTransferService(host)
        self.frames = {}
        self.build_frames()
        self.build_widgets()
        
    def add_frame(self, frame, anchor, reference, w=None, h=None, bg=None):
        if anchor in frame:
            raise Exception(f'{anchor} frame already exists in reference')
        
        if App.REF not in frame:
            frame[App.REF] = tk.Frame(reference)
            frame[App.REF].pack()
            print('this should never happen')
            
        frame[anchor] = {}
        frame[anchor][App.REF] = tk.Frame(frame[App.REF], bg=bg, width=w, height=h)
        frame[anchor][App.REF].pack(side=anchor)
        
    def build_frames(self):
        self.frames[App.REF] = tk.Frame(self.root)
        self.frames[App.REF].pack(side=App.TOP)
        
        self.add_frame(self.frames, App.TOP, self.root, w=300, h=50)
        self.add_frame(self.frames[self.TOP], App.LEFT, self.frames[App.REF], w=100, h=50)
        self.add_frame(self.frames[self.TOP], App.RIGHT, self.frames[App.REF], w=200, h=50)
        self.add_frame(self.frames[self.TOP][App.RIGHT], App.RIGHT, self.frames[self.TOP][App.REF], w=100, h=50)
        self.add_frame(self.frames[self.TOP][App.RIGHT], App.LEFT, self.frames[self.TOP][App.REF], w=100, h=50)
        # self.add_frame(self.frames, App.BOTTOM, self.root, w=100, h=100, bg=colors[1])
        self.add_frame(self.frames, App.LEFT, self.root, w=100, h=100)
        self.add_frame(self.frames, App.RIGHT, self.root, w=None, h=None)
        self.add_frame(self.frames[App.RIGHT], App.TOP, self.frames[App.REF])
        self.add_frame(self.frames[App.RIGHT], App.BOTTOM, self.frames[App.REF])
        
    def build_widgets(self):
        self.risk_map = RiskMap(self.frames[App.LEFT][App.REF], self.remote, n=3)
        self.heartbeat = Heartbeat(self.frames[App.RIGHT][App.TOP][App.REF], self.remote)
        self.speedometer = GaugeChart(self.frames[App.RIGHT][App.BOTTOM][App.REF], self.remote)
        self.darpa = Picture(self.frames[App.TOP][App.LEFT][App.REF], r'darpa.png', w=100, h=50)
        self.caltech = Picture(self.frames[App.TOP][App.RIGHT][App.LEFT][App.REF], r'caltech.png', w=100, h=50)
        self.sandia = Picture(self.frames[App.TOP][App.RIGHT][App.RIGHT][App.REF], r'sandia.png', w=100, h=50)

if __name__ == '__main__':
    app = App('PackBot Interface', '600x400')
    app.root.mainloop()
        