import cv2

# Configurar la captura de video desde la cámara
cap = cv2.VideoCapture(0)

while True:
    # Leer una imagen desde la cámara
    ret, frame = cap.read()

    # Voltear la imagen horizontalmente para el efecto de espejo
    frame = cv2.flip(frame, 1)

    # Convertir la imagen de BGR a RGB para mostrarla correctamente
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar fragmentos rojos en la imagen y pintarlos de rojo
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    low_red = (0, 120, 70)
    high_red = (10, 255, 255)
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red_areas = cv2.bitwise_and(frame, frame, mask=red_mask)
    red_areas[:, :, 0] = 0
    red_areas[:, :, 1] = 0

    # Mostrar la imagen en una ventana
    cv2.imshow('Espejo Rojo', red_areas)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
