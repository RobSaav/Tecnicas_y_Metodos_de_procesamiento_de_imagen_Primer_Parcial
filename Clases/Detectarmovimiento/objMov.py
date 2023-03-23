import cv2
import urllib.request
import numpy as np

# URL de la transmisión de la cámara
url = 'http://172.26.128.56:8080/shot.jpg'

# Función para decodificar la imagen
def url_to_image(url):
    resp = urllib.request.urlopen(url)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img

# Abrir la transmisión de la cámara y mostrar la imagen en tiempo real
while True:
    img = url_to_image(url)
    cv2.imshow('IP Webcam Stream', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cerrar la ventana y liberar los recursos
cv2.destroyAllWindows()
