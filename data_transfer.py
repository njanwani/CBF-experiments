#!/usr/bin/env python3

import redis
import cv2
import numpy as np

class DataTransferService:
    def __init__(self, host='localhost', port=6379):
        self.port = port
        self.host = host
        self.conn = redis.Redis(host,port,password="hello world")
        self.frameNum = 0

    def ping(self):
        return self.conn.ping()

    def sendImage(self,im, name='latest', Q=75):
        _, JPEG = cv2.imencode(".JPG", im, [int(cv2.IMWRITE_JPEG_QUALITY), Q])
        myDict = { 'frameNum': self.frameNum, 'Data':JPEG.tobytes() }
        self.conn.hmset(name, myDict)
        self.frameNum += 1

    def receiveImage(self,name='latest'):
        myDict  = self.conn.hgetall(name)
        Image = myDict.get(b'Image')
        im = cv2.imdecode(np.frombuffer(Image,dtype=np.uint8), cv2.IMREAD_COLOR)
        return im
    
    def receive_rate(self,name='latest'):
        myDict  = self.conn.hgetall(name)
        rates = np.frombuffer(myDict.get(b'Rates'))
        return rates
    
    def receive_vx(self,name='latest'):
        myDict  = self.conn.hgetall(name)
        vx = float(myDict.get(b'vx'))
        return vx