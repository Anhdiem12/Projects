import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

while True:
    _, frame1 = cap.read()
    frame = cv2.resize(frame1,(1000,800))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_Yellow = np.array([0, 46, 64])
    upper_Yellow = np.array([31, 255, 255])

    lower_Green = np.array([49, 56, 64])
    upper_Green = np.array([96, 255, 255])

    lower_Blue = np.array([86, 56, 64])
    upper_Blue = np.array([175, 255, 255])

    mask1 = cv2.inRange(hsv, lower_Yellow,upper_Yellow)
    mask2 = cv2.inRange(hsv, lower_Green, upper_Green)
    mask3 = cv2.inRange(hsv, lower_Blue, upper_Blue)

    ct1 = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #Tìm đường bao quanh hình màu vàng
    ct1 = imutils.grab_contours(ct1)

    ct2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    ct2 = imutils.grab_contours(ct2)

    ct3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    ct3 = imutils.grab_contours(ct3)

    for c in ct1:
        area1 = cv2.contourArea(c)
        print(area1)
        approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
        #print(approx)
       # print(len(approx))
        if area1 > 1000:
             cv2.drawContours(frame,[c],-1,(0,255,0),3)
             # Xác định trọng tâm của đường bao
             M = cv2.moments(c)
             cx = int(M["m10"]/M["m00"])
             cy = int(M["m01"] / M["m00"])
             #Vẽ đường tròn nhỏ lên hình vừa detect
             cv2.circle(frame, (cx, cy), 7, (252, 1, 10), -1)

             if len(approx) == 3:
                 cv2.putText(frame,"YELLOW TRIANGLE",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX , 1,(25,0,255),2)
             elif len(approx) == 4:
                 x1, y1, w, h = cv2.boundingRect(approx)
                 a = float(w / h)
                 if (a > 0.9) and (a <= 1.1):
                     cv2.putText(frame, "YELLOW SQUARE", (cx-20, cy-20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1, 1, 0),2)
                 else:
                     cv2.putText(frame, "YELLOW RECTANGLE",(cx-20, cy-20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (1, 1, 0),2)

             elif (len(approx) > 9 and len(approx) < 13):
                 cv2.putText(frame, "YELLOW STAR ", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1,(25, 0, 255), 2)
             elif ( len(approx) > 12 and len(approx)<17):
                 cv2.putText(frame, "YELLOW CIRCLE", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 0, 255), 2)

             else:
                 break

    for c in ct2:
        area2 = cv2.contourArea(c)
        approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
       # print(len(approx))
        if area2 >1000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 2, (255, 255, 255), 1)

            if len(approx) == 3:
                cv2.putText(frame, "GREEN TRIANGLE", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 5, 255),2)
            elif len(approx) == 4:
                x1, y1, w, h = cv2.boundingRect(approx)
                a = float(w / h)
                if (a > 0.9) and (a <= 1.1):
                    cv2.putText(frame, "GREEN SQUARE", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(1, 1, 0), 2)
                else:
                    cv2.putText(frame, "GREEN RECTANGLE", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(1, 1, 0), 2)
            elif (len(approx) > 9 and len(approx) < 13):
                cv2.putText(frame, "GREEN STAR ", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 0, 255), 2)
            elif (len(approx) > 12 and len(approx) < 17):
                cv2.putText(frame, "GREEN CIRCLE ", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 0, 255), 2)
            else:
                break

    for c in ct3:
        area3 = cv2.contourArea(c)
        approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
        if area3 >1000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 2, (255, 255, 255), 1)

            if len(approx) == 3:
                cv2.putText(frame, "BLUE TRIANGLE ", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (55, 255, 255),2)
            elif len(approx) == 4:
                x1, y1, w, h = cv2.boundingRect(approx)
                a = float(w / h)
                if (a > 0.9) and (a <= 1.1):
                    cv2.putText(frame, "BLUE SQUARE", (cx - 20, cy - 20), cv2.FONT_HERSHEY_COMPLEX, 0.5,(1, 1, 0), 2)
                else:
                    cv2.putText(frame, "BLUE RECTANGLE ", (cx - 20, cy - 20), cv2.FONT_HERSHEY_COMPLEX, 0.5,(1, 1, 0), 2)
            elif (len(approx) > 9 and len(approx) < 13):
                cv2.putText(frame, "BLUE STAR ", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 0, 255), 2)
            elif (len(approx) > 12 and len(approx) < 17):
                cv2.putText(frame, "BLUE CIRCLE ", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 0, 255), 2)
            else:
                break

    cv2.imshow(" Ket qua:",frame)
    key = cv2.waitKey(5)
    if key == 27:
        break
cv2.waitKey(0)

