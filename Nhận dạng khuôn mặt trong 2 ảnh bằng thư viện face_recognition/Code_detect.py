import cv2
import face_recognition as f
import math
import numpy as np
import dlib as dl

imgElon = cv2.imread("../Nhận dạng  mặt qua Webcam/picture/elon musk.jpg")
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgCheck = cv2.imread("../Nhận dạng  mặt qua Webcam/picture/jeff1.jpg")
imgCheck = cv2.cvtColor(imgCheck,cv2.COLOR_BGR2RGB)

"Xác định vị trí khuôn mặt ảnh đầu vào "
facelocation = f.face_locations(imgElon)[0]
print(facelocation) # trả về facelocation(0,1,2,3) = (y1,x2,y2,x1) ( ví dụ : (53, 397, 182, 268) = (y1,x2,y2,x1))
" Mã hóa hình ảnh đầu vào "
encodeElon = f.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(facelocation[3],facelocation[0]),(facelocation[1],facelocation[2]),[233,0,222],2)

faceCheck = f.face_locations(imgCheck)[0]
encodeCheck = f.face_encodings(imgCheck)[0]
cv2.rectangle(imgCheck,(faceCheck[3],faceCheck[0]),(faceCheck[1],faceCheck[2]),[233,0,222],2)

"So sánh hai bức ảnh"
result = f.compare_faces([encodeElon],encodeCheck)
print(result)
"Tính khoảnh cách (sai số) giữa hai bức ảnh"
lost = f.face_distance([encodeElon],encodeCheck)
print(lost)
cv2.putText(imgCheck,f"{result}{round(lost[0],2)}",(faceCheck[3], faceCheck[0]),cv2.FONT_HERSHEY_COMPLEX,1,(122,12,233),3)

cv2.imshow("",imgElon)
cv2.imshow(" ",imgCheck)
cv2.waitKey(0)
