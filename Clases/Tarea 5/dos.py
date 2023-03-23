import cv2
import numpy as np

# Función para determinar la forma de un contorno
def detect_shape(cnt):
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
    if len(approx) == 3:
        return "Triangulo"
    elif len(approx) == 4:
        return "Cuadrado"
    elif len(approx) == 5:
        return "Pentagono"
    else:
        return "Circulo"

# Función para determinar el color predominante en un objeto
def detect_color(frame, cnt):
    mask = np.zeros(frame.shape[:2], np.uint8)
    cv2.drawContours(mask, [cnt], -1, 255, -1)
    hist = cv2.calcHist([frame], [0, 1, 2], mask, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    color = hist.argmax()
    if color == 0:
        return "Rojo"
    elif color == 1:
        return "Verde"
    else:
        return "Azul"

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar un fotograma
    ret, frame = cap.read()

    # Convertir el fotograma a una imagen en escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral para binarizar la imagen
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Encontrar los contornos de los objetos en la imagen binarizada
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos y etiquetar los objetos con su forma y color correspondiente
    for cnt in contours:
        shape = detect_shape(cnt)
        color = detect_color(frame, cnt)
        cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 2)
        cv2.putText(frame, shape + " " + color, tuple(cnt[cnt[:, :, 1].argmin()][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    # Mostrar la imagen resultante
    cv2.imshow('Reconocimiento de figuras y colores', frame)

    # Salir al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()