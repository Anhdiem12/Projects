import cv2
cap = cv2.VideoCapture(“data/video.mp4”)
while True:
success, img = cap.read()
cv2.imshow(“V”,img)
if cv2.waitKey(1) & 0xFF == ord(‘q’):
break
