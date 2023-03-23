import cv2
import numpy as np

# Define los límites de los colores que se van a detectar
color_limits = {
    "red": ([0, 50, 50], [10, 255, 255]),
    "green": ([50, 100, 100], [70, 255, 255]),
    "blue": ([110, 50, 50], [130, 255, 255]),
    "yellow": ([25, 50, 50], [35, 255, 255])
}

# Función para encontrar los contornos de las figuras en la imagen
def find_contours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# Función para encontrar el color dominante en un contorno
def find_color(contour, img):
    mask = np.zeros(img.shape[:2], np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, -1)
    mean_color = cv2.mean(img, mask=mask)[:3]
    color = max(color_limits.keys(), key=lambda x: cv2.inRange(np.array(mean_color), *color_limits[x]))
    return color

# Inicializa la cámara
cap = cv2.VideoCapture(0)

while True:
    # Captura una imagen de la cámara
    ret, frame = cap.read()

    # Encuentra los contornos en la imagen
    contours = find_contours(frame)

    # Procesa cada contorno
    for contour in contours:
        # Encuentra el perímetro del contorno y aproxima los vértices
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

        # Si el contorno tiene 4 vértices, lo identifica como un cuadrilátero
        if len(approx) == 4:
            color = find_color(contour, frame)
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
            cv2.putText(frame, f"{color} square", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Si el contorno tiene 3 vértices, lo identifica como un triángulo
        elif len(approx) == 3:
            color = find_color(contour, frame)
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
            cv2.putText(frame, f"{color} triangle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Muestra la imagen procesada en una ventana
    cv2.imshow("Frame", frame)

    # Si se presiona la tecla 'q', sale del bucle y termina el programa
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    # Función principal del programa
def main():
    # Inicializa la cámara
    cap = cv2.VideoCapture(0)

    while True:
        # Captura una imagen de la cámara
        ret, frame = cap.read()

        # Encuentra los contornos en la imagen
        contours = find_contours(frame)

        # Procesa cada contorno
        for contour in contours:
            # Encuentra el perímetro del contorno y aproxima los vértices
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

            # Si el contorno tiene 4 vértices, lo identifica como un cuadrilátero
            if len(approx) == 4:
                color = find_color(contour, frame)
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
                cv2.putText(frame, f"{color} square", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # Si el contorno tiene 3 vértices, lo identifica como un triángulo
            elif len(approx) == 3:
                color = find_color(contour, frame)
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
                cv2.putText(frame, f"{color} triangle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Muestra la imagen procesada en una ventana
        cv2.imshow("Frame", frame)

        # Si se presiona la tecla 'q', sale del bucle y termina el programa
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera los recursos de la cámara y cierra las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Llama a la función principal del programa
if __name__ == "__main__":
    main()