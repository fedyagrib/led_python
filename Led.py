from typing import List
import cv2
import numpy as np
from random import randint
import asyncio

loop = asyncio.get_event_loop()

class Led:
    def __init__(self, led_num:int = 20, pix_width: int = 40, pix_offset:int = 20) -> None:
        self.__led_num = led_num
        self.__pix_width = pix_width
        self.__pix_offset = pix_offset

        self.__width = (pix_width + pix_offset) * led_num + pix_offset
        self.__height = 2 * pix_offset + pix_width
        
        self.array = np.zeros((self.__height, self.__width, 3))
        self.array[:,:,:] = 1
        # self.clear_all()

    def __len__(self) -> int:
        return self.__led_num

    def show(self, delay) -> None:
        cv2.imshow('Frame',self.array)
        cv2.waitKey(delay)

    def __set_pixel(self, pix_num:slice, clr: List) -> None:
        clr = [c/255 for c in clr]
        self.array[ self.__pix_offset: self.__pix_offset + self.__pix_width, 
        pix_num * (self.__pix_offset + self.__pix_width) + self.__pix_offset : (pix_num + 1) * (self.__pix_offset + self.__pix_width)] = clr

    def __setitem__(self, pix_num, clr: List) -> None:
        if type(pix_num) == int:
            self.__set_pixel(pix_num, clr)

        if type(pix_num) == slice:
            start = pix_num.start if pix_num.start else 0
            stop = pix_num.stop if pix_num.stop else len(self)
            step = pix_num.step if pix_num.step else 1

            for i in range(pix_num):
                self.__set_pixel(i, clr)
        

    def __getitem__(self, pix_num: int) -> List:
        clr = self.array[self.__pix_offset, pix_num * (self.__pix_offset + self.__pix_width) + self.__pix_width]
        return [c*255 for c in clr]

    def random_clr(self, pix_num:int) -> None:
        self[pix_num] = [randint(0,255),randint(0,255),randint(0,255)] 
    
    def clear_pix(self, pix_num:int) -> None:
        self[pix_num] = [255,255,255]
    
    def clear_all(self) -> None:
        for i in range(len(self)):
            self.clear_pix(i)
    
    def clearing(self, coef) -> None:
        for i in range(len(self)):
            self[i] = [c-coef for c in self[i]]
