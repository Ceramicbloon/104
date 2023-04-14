import cv2
pic = cv2.imread("solar-system.jpg")
text = ["sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
cv2.putText(pic, text[0], (20, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(pic, text[1], (110, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(pic, text[2], (190, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(pic, text[3], (285, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(pic, text[4], (385, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(pic, text[5], (485, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
cv2.putText(pic, text[6], (705, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(pic, text[7], (935, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(pic, text[8], (1085, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.imshow("a", pic)
cv2.waitKey(0)
