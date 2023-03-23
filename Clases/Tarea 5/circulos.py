import cv2
import numpy as np

img = cv2.imread("portada2.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    
    for (x, y, r) in circles:
        roi = img[y-r:y+r, x-r:x+r]
        (B, G, R) = [int(i) for i in cv2.mean(roi)[:3]]
        
        if R > 200 and G < 50 and B < 50:
            color = "rojo"
        elif R < 50 and G > 200 and B < 50:
            color = "verde"
        elif R < 50 and G < 50 and B > 200:
            color = "azul"
        else:
            color = "otro"
            
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        cv2.putText(img, color, (x - 20, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

cv2.imshow("Circulos", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
