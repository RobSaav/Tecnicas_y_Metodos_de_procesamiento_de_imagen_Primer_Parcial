import cv2
import numpy as np

video = cv2.VideoCapture(0)
def figColor(imagenHSV):
	color_ranges = [
    (np.array([0, 100, 20]), np.array([10, 255, 255])),
    (np.array([175, 100, 20]), np.array([180, 255, 255])),
    (np.array([11, 100, 20]), np.array([19, 255, 255])),
    (np.array([20, 100, 20]), np.array([32, 255, 255])),
    (np.array([36, 100, 20]), np.array([70, 255, 255])),
    (np.array([130, 100, 20]), np.array([145, 255, 255])),
    (np.array([146, 100, 20]), np.array([170, 255, 255]))
	]
	# Rojo
	rojoBajo1 = np.array([0, 100, 20], np.uint8)
	rojoAlto1 = np.array([10, 255, 255], np.uint8)
	rojoBajo2 = np.array([175, 100, 20], np.uint8)
	rojoAlto2 = np.array([180, 255, 255], np.uint8)

	# Naranja
	naranjaBajo = np.array([11, 100, 20], np.uint8)
	naranjaAlto = np.array([19, 255, 255], np.uint8)

	#Amarillo
	amarilloBajo = np.array([20, 100, 20], np.uint8)
	amarilloAlto = np.array([32, 255, 255], np.uint8)

	#Verde
	verdeBajo = np.array([36, 100, 20], np.uint8)
	verdeAlto = np.array([70, 255, 255], np.uint8)

	#Violeta
	violetaBajo = np.array([130, 100, 20], np.uint8)
	violetaAlto = np.array([145, 255, 255], np.uint8)

	#Rosa
	rosaBajo = np.array([146, 100, 20], np.uint8)
	rosaAlto = np.array([170, 255, 255], np.uint8)

	# Se buscan los colores en la imagen, segun los límites altos 
	# y bajos dados
	maskRojo1 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
	maskRojo2 = cv2.inRange(imagenHSV, rojoBajo2, rojoAlto2)
	maskRojo = cv2.add(maskRojo1, maskRojo2)
	maskNaranja = cv2.inRange(imagenHSV, naranjaBajo, naranjaAlto)
	maskAmarillo = cv2.inRange(imagenHSV, amarilloBajo, amarilloAlto)
	maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
	maskVioleta = cv2.inRange(imagenHSV, violetaBajo, violetaAlto)
	maskRosa = cv2.inRange(imagenHSV, rosaBajo, rosaAlto)
	
	cntsRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3	
	cntsNaranja = cv2.findContours(maskNaranja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3
	cntsAmarillo = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3
	cntsVerde = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3
	cntsVioleta = cv2.findContours(maskVioleta, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3
	cntsRosa = cv2.findContours(maskRosa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Reemplaza por 1, si tienes OpenCV3

	if len(cntsRojo)>0: color = 'Rojo'
	elif len(cntsNaranja)>0: color = 'Naranja'
	elif len(cntsAmarillo)>0: color = 'Amarillo'
	elif len(cntsVerde)>0: color = 'Verde'
	elif len(cntsVioleta)>0: color = 'Violeta'
	elif len(cntsRosa)>0: color = 'Rosa'

	return color

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(frame,cnt,-1,(255,0,0),3)
            perimetro = cv2.arcLength(cnt,True)
            #buscar bordes
            aprrox = cv2.approxPolyDP(cnt,0.02*perimetro,True)
            objCorner = len(aprrox)
            x,y,w,h = cv2.boundingRect(aprrox)
            if objCorner ==3:
                namefig='Triangulo'
            elif objCorner ==4:
                aspecto = w/float(h)
                if aspecto >0.95 and aspecto<1.05:
                    namefig='Cuadrado'
                else:
                    namefig='Rectangulo'
            elif objCorner ==5:
                namefig='Pentagono'
            elif objCorner ==6:
                namefig='Hexagono'
            elif objCorner >10:
                namefig='Circulo'
            else:
                namefig='Circulo'
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,namefig,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
    
    
while True:
    ret,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(7,7),1)
    imgcanny = cv2.Canny(blur,50,50)
    getContours(imgcanny)
    cv2.imshow("figuras Geometricas",frame)
    if cv2.waitKey(1) == ord('q'):
        break