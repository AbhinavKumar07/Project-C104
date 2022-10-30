import cv2

image = cv2.imread('solar-system.jpg')
cv2.putText(image, 'Sun', (60,400),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.9,color=(0,239,255))
cv2.putText(image, 'Mercury', (130,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,239,255))
cv2.putText(image, 'Venus', (200,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,239,255))
cv2.putText(image, 'Earth', (290,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,239,255))
cv2.putText(image, 'Mars', (390,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,239,255))
cv2.putText(image, 'Jupiter', (540,400),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,239,255))
cv2.putText(image, 'Saturn', (760,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,239,255))
cv2.putText(image, 'Uranus', (960,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,239,255))
cv2.putText(image, 'Neptune', (1100,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,239,255))
cv2.imshow('output',image)
cv2.waitKey(0)
