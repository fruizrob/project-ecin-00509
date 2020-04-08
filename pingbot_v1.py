import cv2
import numpy as np
import math  
import serial
import time

instruction = 9
connection = serial.Serial('/dev/ttyACM0', 9600)
connection.flushInput()

cap = cv2.VideoCapture(0)

# celeste
lowBlue = np.array([80, 100, 50], np.uint8)
highBlue = np.array([110, 255, 255], np.uint8)
# rojo
lowRed = np.array([170,120,70], np.uint8)
highRed = np.array([180,255,255], np.uint8)

cont = 0
#cant pelotas recolectadas
rec = 0

x = 0
proximity = 0

def color(area,height,altxdist,tamMin):
    global proximity, x
    if area > tamMin:
        M = cv2.moments(c)
        if(M["m00"] == 0): M["m00"]=1
        x = int(M["m10"]/M["m00"])
        y = int(M["m01"]/M["m00"])
        proximity = (altxdist / height)
        cv2.circle(frame, (x,y), 7, (0,255,0), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'X = {}, {}'.format(x, y),(x+10, y), font, 0.75, (0,255,0), 1, cv2.LINE_AA) 
        newContour = cv2.convexHull(c)
        cv2.putText(frame, "%.2fcm" % proximity, (frame.shape[1] - 300, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), 3)
        cv2.drawContours(frame, [newContour], 0, (255, 0, 0), 3)
def reset():
    global x,proximity
    x = 0
    proximity = 0

while True:
    cont += 1
    ret, frame = cap.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        if(rec < 2):
            mask = cv2.inRange(frameHSV, lowBlue, highBlue)
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for c in contours:
                area = cv2.contourArea(c)
                height = 2*math.sqrt(area/math.pi)
                color(area,height,2400,500)   
        else:
            mask = cv2.inRange(frameHSV, lowRed, highRed)
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for c in contours:
                area = cv2.contourArea(c)
                height = math.sqrt(area)
                color(area,height,6750,600)
                
        if cont%10 == 0:
            if connection.in_waiting:
                print ("Current State: " + str(connection.read()))
                
            if connection.out_waiting:
                print ("Out" + connection.out_waiting)
           
            if instruction == 4:
                reset()
            if proximity == 0 and x == 0:
                if instruction > 3:
                    connection.reset_output_buffer()
                    instruction = 0
                    print("scan")
                if instruction == 0:
                    connection.write(bytes('0',"utf-8"))
            else:
                if x < 380 and x > 260 and proximity > 26 and rec < 2:
                    if instruction < 4:
                        if instruction != 1:
                            connection.reset_output_buffer()
                            instruction = 1
                            print("move forward")
                        connection.write(bytes('1',"utf-8"))
                elif x < 380 and x > 260 and proximity > 38 and rec == 2:
                    if instruction < 4:
                        if instruction != 1:
                            connection.reset_output_buffer()
                            instruction = 1
                            print("move forward")
                        connection.write(bytes('1',"utf-8"))

                elif x > 380:
                    if instruction < 4:
                        if instruction != 2:
                            connection.reset_output_buffer()
                            instruction = 2
                            print("move right")
                        connection.write(bytes('2',"utf-8"))

                elif x < 260:
                    if instruction < 4:
                        if instruction != 3:
                            connection.reset_output_buffer()
                            instruction = 3
                            print("move left")
                        connection.write(bytes('3',"utf-8"))

                elif rec < 2 and proximity < 26:
                    if instruction != 4:
                        connection.reset_output_buffer()
                        instruction = 4
                        print("collect")
                        rec += 1
                    connection.write(bytes('4',"utf-8"))
                    time.sleep(2)
                
                elif rec == 2 and proximity < 38:
                    if instruction != 5:
                        connection.reset_output_buffer()
                        instruction = 5
                        print("drop")
                    connection.write(bytes('5',"utf-8"))


        cv2.imshow('pingbot', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv2.destroyAllWindows()