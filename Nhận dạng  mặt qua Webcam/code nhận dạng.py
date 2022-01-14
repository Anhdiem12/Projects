import cv2
import face_recognition as f
import os   # dùng để load ảnh
import numpy as np
"Xử lý đầu vào"
path = "picture"
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)  # ['elon check.jpg', 'elon musk.jpg', 'elon1.jpg', 'jeff1.jpg', 'tokuda.jpg']

for i in mylist:
    # print(i)                                  # Ví dụ i = elon check.jpg    i[0] = elon musk = Tên đối tượng, i[1] =ipg
    img = cv2.imread(f"{path}/{i}")             # ví dụ đọc picture/elon1.jpg
    images.append(img)                          # Cho từng img đọc được trong mylist vào tập ảnh images
    classNames.append(os.path.splitext(i)[0])   # Lấy tên các bố trong input rồi cho vào files rỗng classNames tạo ở trên để sau detect dc thì xuất ra màn hình
print(len(images))
print(classNames)

" Mã hóa thư viện ảnh đầu vào "
def Mahoa(images):
    encodeList = []
    for j in images:
        im = cv2.cvtColor(j,cv2.COLOR_BGR2RGB)
        encode = f.face_encodings(im)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = Mahoa(images)
print(" Số ảnh mã hóa thành công :",len(encodeListKnown))

" Khởi động cammera "
cap = cv2.VideoCapture(1)
#cap = cv2.VideoCapture("videoTest.mp4")
while True:
   _, frame0 = cap.read()
   frame = cv2.resize(frame0,(0,0),None,fx=0.5,fy=0.5)   # (0,0): Tọa độ bắt đầu -- fx,fy kia là khung hình bằng nửa khung ban đầu
   frame = cv2.cvtColor(frame0,cv2.COLOR_BGR2RGB)

   # Xác định vị trí khuôn mặt trong khung hình
   faceFrame   = f.face_locations(frame)      # Lấy từng khuôn mặt và vị trí khuôn mặt hiện tại
   encodeFrame = f.face_encodings(frame)

   for encodeface,faceLocation in zip(encodeFrame,faceFrame):
       kq           = f.compare_faces(encodeListKnown,encodeface)
       faceDistance = f.face_distance(encodeListKnown,encodeface)
       mathIndex = np.argmin(faceDistance)     # Đẩy về chỉ số của faceDistance nhỏ nhất

       if faceDistance[mathIndex]<0.5:
           name = classNames[mathIndex].upper()
       else:
           name = "unknown"

        # in ra tên
       y1,x2,y2,x1 = faceLocation
       cv2.rectangle(frame0,(x1,y1),(x2,y2),(255,233,23),2)
       cv2.putText(frame0,name,(x2,y2),cv2.FONT_HERSHEY_SIMPLEX,1,(233,23,232),2)


   cv2.imshow(" Ket qua:", frame0)
   key = cv2.waitKey(5)
   if key == 27:
       break
#cv2.waitKey(1)