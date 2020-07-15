# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:49:40 2020

@author: HP
"""

import cv2
# THIS IS MY WEBCAM
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read() #HERE IS AM SIMPLY READING FROM MY WEBCAM
    if ret:
        # back is what the camera is reading
        cv2.imshow("image", back)
        #waitkey is your refresh rate for 5 miliseconds
             # ord is just giving a unicode value of q
             #when you press q on your computer iyt will comes 
             #out from loop,then it will save the image
        if cv2.waitKey(5) == ord('q'):
            # save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()