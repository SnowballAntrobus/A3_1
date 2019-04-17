import numpy as np
import cv2

#black image
img = np.zeros((512,512,3), np.uint8)

#Draw diagonal blue line thickness of 5px
img = cv2.line(img,(0,0),(200,200),(255,0,0),50)

#Draw rectangle
img = cv2.rectangle(img,(384,0),(200,200),(0,255,0),3)

#Draw circle
img = cv2.circle(img,(200,200),5,(0,0,255),-1)

#Draw ellipse
img = cv2.ellipse(img,(300,300),(100,50),0,0,180,255,-1)

#Draw polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],False,(0,255,255))

#Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Dante!',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

#Show
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('draw.png',img)
    cv2.destroyAllWindows()
  
