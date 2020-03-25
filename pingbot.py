import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# color
lowBlue = np.array([100, 100, 20], np.uint8)
highBlue = np.array([125, 255, 255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        # cambia formato
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # detecta objeto con los limites enviados
        mask = cv2.inRange(frameHSV, lowBlue, highBlue)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in contours:
            area = cv2.contourArea(c)
            if area > 2000:
                M = cv2.moments(c)
                if(M["m00"] == 0): M["m00"]=1
                x = int(M["m10"]/M["m00"])
                y = int(M["m01"]/M["m00"])
                cv2.circle(frame, (x,y), 7, (0,255,0), -1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,'{}, {}'.format(x,y),(x+10, y), font, 0.75, (0,255,0), 1, cv2.LINE_AA)
                newContour = cv2.convexHull(c)
                cv2.drawContours(frame, [newContour], 0, (255, 0, 0), 3)
        
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv2.destroyAllWindows()
