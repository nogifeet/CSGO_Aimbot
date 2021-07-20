import win32ui 
import win32con 
import win32gui 
import numpy as np 

class screen_grab:

    def __init__(self,h,w):
        self.h = int(h) 
        self.w = int(w)
        self.scName = 'Counter-Strike: Global Offensive'

    def window_capture(self):
     
        self.hwnd = win32gui.FindWindow(None,self.scName)
        self.wDC = win32gui.GetWindowDC(self.hwnd)
        self.dcObj=win32ui.CreateDCFromHandle(self.wDC)
        self.cDC=self.dcObj.CreateCompatibleDC()
        self.dataBitMap = win32ui.CreateBitmap()
        self.dataBitMap.CreateCompatibleBitmap(self.dcObj, self.w, self.h)
        self.cDC.SelectObject(self.dataBitMap)
        self.cDC.BitBlt((0,0),(self.w, self.h) , self.dcObj, (0,0), win32con.SRCCOPY)
        #dataBitMap.SaveBitmapFile(cDC, 'csgo_file.bmp')
        self.signedIntsArray = self.dataBitMap.GetBitmapBits(True)
        self.img = np.frombuffer(self.signedIntsArray,dtype='uint8')
        self.img.shape= (self.h,self.w,4)
        self.img = self.img[...,:3]
        self.img = np.ascontiguousarray(self.img)

        # Free Resources
        self.dcObj.DeleteDC()
        self.cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, self.wDC)
        win32gui.DeleteObject(self.dataBitMap.GetHandle())
        return self.img