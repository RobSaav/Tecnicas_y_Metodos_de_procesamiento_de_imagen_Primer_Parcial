import cv2
from cv2 import VideoCapture
import numpy as np

# Iniciar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar un fotograma
    ret, frame = cap.read()

    # Convertir a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir los rangos de color para la detección
    lower_red = np.array([0,100,100])
    upper_red = np.array([10,255,255])

    lower_green = np.array([45,100,50])
    upper_green = np.array([75,255,255])

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    lower_yellow = np.array([20,100,100])
    upper_yellow = np.array([30,255,255])

    # Crear máscaras para cada color
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Encontrar contornos en cada máscara
    contours_red, hierarchy = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, hierarchy = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue, hierarchy = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, hierarchy = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en el fotograma
    for cnt in contours_green:
        area = cv2.contourArea(cnt)
        if area > 300:
            epsilon = 0.1 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            if len(approx) == 3:
                shape = "Triángulo"
                color = (0,255,0)
            elif len(approx) == 4:
                shape = "Cuadrado"
                color = (0,255,0)
            elif len(approx) == 5:
                shape = "Pentágono"
                color = (0,255,0)
            elif len(approx) == 6:
                shape = "Hexágono"
                color = (0,255,0)
            elif len(approx) >= 7:
                shape = "Círculo"
                color = (0,255,0)
            elif len(approx) >= 9:
                shape = "Rectangulo"
                color = (0,255,0)
            else:
                shape = "Otro"
                color = (0,255,0)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.drawContours(frame, [approx], 0, color, 2)
            cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    for cnt in contours_blue:
        area = cv2.contourArea(cnt)
        if area > 300:
            epsilon = 0.1 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            if len(approx) == 3:
                shape = "Triangulo"
                color = (255,0,0)
            elif len(approx) == 4:
                shape = "Cuadrado"
                color = (255,0,0)
            elif len(approx) == 5:
                shape = "Pentagono"
                color = (255,0,0)
            elif len(approx) == 7:
                shape = "Hexagono"
                color = (255,0,0)
            elif len(approx) >= 8:
                shape = "Círculo"
                color = (255,0,0)
            elif len(approx) >= 9:
                shape = "Rectangulo"
                color = (0,255,0)
            else:
                shape = "Nulo"
                color = (255,0,0)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.drawContours(frame, [approx], 0, color, 2)
            cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    for cnt in contours_red:
        area = cv2.contourArea(cnt)
        if area > 300:
            epsilon = 0.1 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            if len(approx) == 3:
                shape = "Triángulo"
                color = (0,0,255)
            elif len(approx) == 4:
                shape = "Cuadrado"
                color = (0,0,255)
            elif len(approx) == 5:
                shape = "Pentágono"
                color = (0,0,255)
            elif len(approx) == 6:
                shape = "Hexágono"
                color = (0,0,255)
            elif len(approx) >= 7:
                shape = "Círculo"
                color = (0,0,255)
            elif len(approx) >= 9:
                shape = "Rectangulo"
                color = (0,255,0)
            else:
                shape = "Nulo"
                color = (0,0,255)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.drawContours(frame, [approx], 0, color, 2)
            cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    for cnt in contours_yellow:
        area = cv2.contourArea(cnt)
        if area > 300:
            epsilon = 0.1 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            if len(approx) == 3:
                shape = "Triángulo"
                color = (0,255,255)
            elif len(approx) == 4:
                shape = "Cuadrado"
                color = (0,255,255)
            elif len(approx) == 5:
                shape = "Pentágono"
                color = (0,255,255)
            elif len(approx) == 6:
                shape = "Hexágono"
                color = (0,255,255)
            elif len(approx) >= 7:
                shape = "Círculo"
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                color = (0,255,255)
            elif len(approx) >= 9:
                shape = "Rectangulo"
                color = (0,255,0)
            else:
                shape = "Indefinido"
                color = (0,255,255)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.drawContours(frame, [approx], 0, color, 2)
            cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
VideoCapture.release()
cv2.destroyAllWindows()