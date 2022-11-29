import cv2
import matplotlib.pyplot as plt 


img = cv2.imread('Cars.jpg')
img = cv2.resize(img, (650,500))

imgray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY) 

ret , thresh = cv2.threshold(imgray, 50, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#for each contours , find the convex hull and draw it 
for i in range(len(contours)) :
    hull = cv2.convexHull(contours[i])
    cv2.drawContours(img, [hull], -1, (0,255,0), 2)
    
    
cv2.imshow('ConvexHull', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

    