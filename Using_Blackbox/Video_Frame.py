# import cv2
# cap = cv2.VideoCapture('/Users/User/PycharmProjects/network/ML_Camp/Using_Blackbox/test.mp4')
# count = 0
# while cap.isOpened():
#     ret,frame = cap.read()
#     cv2.imshow('window-name',frame)
#     # cv2.imwrite("frame%d.jpg" % count, frame)
#     count = count + 1
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
#
#
# cap.release()
# cap.destroyAllWindows()


import cv2

cap = cv2.VideoCapture('/Users/User/PycharmProjects/network/ML_Camp/Using_Blackbox/test.mp4')
c=1

if cv2.isOpened():
    rval , frame = cv2.read()
else:
    rval = False

while rval:
    rval, frame = cv2.read()
    cv2.imwrite(str(c) + '.jpg',frame)
    c = c + 1
    cv2.waitKey(1)
cv2.release()