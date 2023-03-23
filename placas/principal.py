import cv2

# Configuración de la cámara
cap = cv2.VideoCapture(0)
cap.set(3, 640) # Ancho
cap.set(4, 480) # Altura

# Configuración de la fuente y el color
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 255, 0)

# Configuración de la región de interés (ROI)
x, y, w, h = 50, 50, 300, 300

# Inicializa la lista de letras detectadas
detected_letters = []

while True:
    # Captura el fotograma de la cámara
    ret, frame = cap.read()
    
    # Si se captura correctamente
    if ret:
        # Recorta la región de interés
        roi = frame[y:y+h, x:x+w]
        
        # Aplica umbralización y dilatación para resaltar las letras
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        dilate = cv2.dilate(thresh, kernel, iterations=4)
        
        # Encuentra los contornos de las letras
        contours, _ = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        # Dibuja un rectángulo alrededor de cada letra detectada y muestra la letra en la pantalla
        for contour in contours:
            (x1, y1, w1, h1) = cv2.boundingRect(contour)
            if w1 >= 5 and h1 >= 25: # Ajusta estos valores según las letras que quieras detectar
                cv2.rectangle(roi, (x1, y1), (x1+w1, y1+h1), color, 2)
                letter = chr(65 + int(x1/35))
                cv2.putText(roi, letter, (x1, y1-10), font, 1, color, 2)
                detected_letters.append(letter)
        
        # Muestra la imagen en la pantalla
        cv2.imshow("Letras", frame)
        
        # Si se presiona la tecla 'q', detiene el programa
        if cv2.waitKey(1) == ord('q'):
            break
            
    # Imprime las letras detectadas en la consola
    letters_str = ''.join(detected_letters)
    print(f'Letras detectadas: {letters_str}')

# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()