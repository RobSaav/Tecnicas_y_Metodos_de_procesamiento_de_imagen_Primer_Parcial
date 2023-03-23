import cv2
import numpy as np
import datetime


# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Configurar el codec de video y crear el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

# Inicializar el objeto cv2.hist
hist = None

def create_histogram(image):
    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    # Crear histograma de valores de canal
    hist_h = cv2.calcHist([h], [0], None, [180], [0, 180])
    hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])
    hist_v = cv2.calcHist([v], [0], None, [256], [0, 256])

    # Normalizar los histogramas
    cv2.normalize(hist_h, hist_h, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(hist_s, hist_s, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(hist_v, hist_v, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Concatenar los histogramas verticalmente
    hist = np.concatenate((hist_h, hist_s, hist_v), axis=0)

    return hist



while True:
    # Leer cuadro de video
    ret, frame = cap.read()

    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir el rango de colores de la piel humana en HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Aplicar la segmentación de piel para detectar la mano
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Aplicar una operación morfológica de apertura para eliminar pequeñas manchas
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Encontrar los contornos de la mano
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        # Encontrar el contorno de la mano más grande
        max_contour = max(contours, key=cv2.contourArea)

        # Encerrar la mano en un rectángulo
        x, y, w, h = cv2.boundingRect(max_contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Detectar el color de la mano
        hand_color = frame[y+h//2, x+w//2]
        hue = hand_color[0]
        if 0 <= hue < 15:
            hand_color_name = "Rojo"
        elif 15 <= hue < 30:
            hand_color_name = "Naranja"
        elif 30 <= hue < 45:
            hand_color_name = "Amarillo"
        elif 45 <= hue < 75:
            hand_color_name = "Verde"
        elif 75 <= hue < 105:
            hand_color_name = "Azul"
        elif 105 <= hue < 135:
            hand_color_name = "Azul"
        elif 135 <= hue < 165:
            hand_color_name = "Morado"
        else:
            hand_color_name = "Rosa"

        # Mostrar el color de la mano en la pantalla
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'Color de la mano: {hand_color_name}', (10, 30), font, 0.7, (0, 255, 0), 2)
        


    # Grabar el cuadro actual en el objeto VideoWriter
    out.write(frame)

    # Mostrar imagen en tiempo real
    cv2.imshow('frame', frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Crear y guardar histograma
hist = create_histogram(frame)
np.savetxt('histogram.txt', hist)

# Crear y guardar histograma
hist = create_histogram(frame)
hist_image = np.zeros((hist.shape[0], 256, 3), np.uint8)
for i in range(hist.shape[0]):
 cv2.line(hist_image, (0, i), (int(hist[i]), i), (255, 255, 255), 1)
cv2.imwrite('histogram.png', hist_image)

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()

