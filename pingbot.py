import cv2
import numpy as np
import math  
import serial

instruction = -1
connection = serial.Serial('/dev/ttrACM0', 9600)
connection.flushInput()

cap = cv2.VideoCapture(0)

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
        
        x = 0
        proximity = 0
        for c in contours:
            area = cv2.contourArea(c)
            height = 2*math.sqrt(area/math.pi) #sqrt solo en cuadrados, calcular diferente en pelota (para obtener el alto de la pelota, r*2)
            if area > 800:
                M = cv2.moments(c)
                if(M["m00"] == 0): M["m00"]=1
                x = int(M["m10"]/M["m00"])
                y = int(M["m01"]/M["m00"])
                proximity = (2400 / height)
                cv2.circle(frame, (x,y), 7, (0,255,0), -1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,'X = {}, {}'.format(x, y),(x+10, y), font, 0.75, (0,255,0), 1, cv2.LINE_AA) 
                newContour = cv2.convexHull(c)
                # 1298 = 22 cm (distancia camara a objeto) * 59 px (altura del objeto, se debe reemplazar).
                cv2.putText(frame, "%.2fcm" % proximity, (frame.shape[1] - 300, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), 3)
                cv2.drawContours(frame, [newContour], 0, (255, 0, 0), 3)
    
        if proximity == 0 and x == 0:
            if(instruction != 0):
                instruction = 0
                connection.write(bytes('0', 'UTF-8'))
                print("scan")
        else:
            if x < 350 and x > 290 and proximity > 23:
                if instruction != 1:
                    instruction = 1
                    connection.write(bytes('1', 'UTF-8'))
                    print("move forward")

            elif x > 350:
                if instruction != 2:
                    instruction = 2
                    connection.write(bytes('2', 'UTF-8'))
                    print("move right")

            elif x < 290:
                if instruction != 3:
                    instruction = 3
                    connection.write(bytes('3', 'UTF-8'))
                    print("move left")

            elif proximity < 23:
                if instruction != 4:
                    instruction = 4
                    connection.write(bytes('4', 'UTF-8'))
                    print("collect")

        cv2.imshow('pingbot', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv2.destroyAllWindows()