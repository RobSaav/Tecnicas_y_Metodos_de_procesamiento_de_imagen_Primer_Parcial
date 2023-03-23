import cv2
import tensorflow as tf

# Carga el modelo de aprendizaje automático previamente entrenado
model = tf.keras.models.load_model('frutas.h5')

# Crea una lista con los nombres de las frutas que el modelo puede identificar
frutas = ['manzana', 'naranja', 'platano']

# Inicializa la cámara
camara = cv2.VideoCapture(0)

while True:
    # Lee una imagen de la cámara
    _, imagen = camara.read()
    
    # Preprocesa la imagen para que sea compatible con el modelo
    imagen = cv2.resize(imagen, (224, 224))
    imagen = imagen / 255.0
    imagen = imagen.reshape(1, 224, 224, 3)
    
    # Utiliza el modelo para predecir qué fruta aparece en la imagen
    prediccion = model.predict(imagen)
    indice_maximo = tf.argmax(prediccion, axis=1)
    etiqueta = frutas[indice_maximo[0]]
    
    # Muestra la imagen y la etiqueta en la pantalla
    cv2.imshow('Frutas', imagen)
    cv2.putText(imagen, etiqueta, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Resultado', imagen)
    
    # Espera a que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) == ord('q'):
        break

# Libera los recursos utilizados por la cámara y cierra las ventanas
camara.release()
cv2.destroyAllWindows()
