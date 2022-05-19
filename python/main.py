import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('dataset/4.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    # +PIO 2020-05-13 lakukan operasi range pada hsv color space
    mask = cv2.inRange(hsv, l_b, u_b)

    # +PIO 2020-05-13 hitung object dengan algoritma connected component
    ret, labels = cv2.connectedComponents(mask)

    # +PIO lakukan operasi bitwise and agar diperoleh hasil dari mask pada rgb color
    res = cv2.bitwise_and(frame, frame, mask=mask)
 
    cv2.putText(res, str(ret-1), (50,50), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()