import tkinter as tk
import numpy as np
import cv2
import ImageTransferService

from widgets import RiskMap

colors = ['red', 'black', 'blue', 'yellow', 'green']

class App():
    
    REF = 'reference'
    TOP = tk.TOP
    BOTTOM = tk.BOTTOM
    LEFT = tk.LEFT
    RIGHT = tk.RIGHT
    
    def __init__(self, name, size, host='0.0.0.0'):
        self.root = tk.Tk()
        self.root.geometry(size)
        self.remote = ImageTransferService.ImageTransferService(host)
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
        
        self.add_frame(self.frames, App.TOP, self.root, w=100, h=100, bg=colors[0])
        self.add_frame(self.frames, App.BOTTOM, self.root, w=100, h=100, bg=colors[1])
        self.add_frame(self.frames, App.LEFT, self.root, w=100, h=100, bg=colors[2])
        self.add_frame(self.frames, App.RIGHT, self.root, w=100, h=100, bg=colors[3])
        
    def build_widgets(self):
        self.risk_map = RiskMap(self.frames[App.LEFT][App.REF], self.remote, n=2)
            

if __name__ == '__main__':
    app = App('tk', '500x500')
    app.root.mainloop()
        