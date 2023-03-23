import cv2
import pytesseract

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Ciclo infinito para procesar cada frame de la cámara
while True:
    # Leer el frame de la cámara
    ret, frame = cap.read()

    # Convertir el frame a escala de grises para simplificar el procesamiento
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar un filtro de umbral para detectar los bordes de las letras
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Encontrar los contornos de los objetos en el frame
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear una lista para almacenar las letras detectadas
    letters = []

    # Iterar sobre los contornos para identificar las letras
    for contour in contours:
        # Calcular el área del contorno
        area = cv2.contourArea(contour)

        # Si el área es muy pequeña, probablemente no sea una letra
        if area > 100:
            # Dibujar un rectángulo alrededor de la letra
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Extraer la región de la imagen correspondiente a la letra
            letter = gray[y:y + h, x:x + w]

            # Agregar la letra detectada a la lista
            letters.append(letter)

    # Mostrar el frame procesado en una ventana
    cv2.imshow('frame', frame)

    # Imprimir las letras detectadas en la consola
    if letters:
        print('Letras detectadas:')
        for letter in letters:
            letter_text = pytesseract.image_to_string(letter)
            print(letter_text)

    # Esperar a que se presione la tecla 'q' para salir del ciclo
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
