import io
import base64
from PIL import Image
from flask import Flask, request, jsonify, render_template # type: ignore
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Cargar el modelo previamente entrenado
model = tf.keras.models.load_model('modelo_postal_3.h5')

@app.route('/')
def index():
    return render_template('index.html')  # Servir el archivo index.html desde la carpeta 'templates'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener la imagen en base64 desde el formulario
        image_data = request.form['image']

        # Verificar si la imagen contiene el prefijo "data:image/png;base64,"
        if image_data.startswith('data:image/png;base64,'):
            image_data = image_data.split(',')[1]  # Eliminar el prefijo

        # Decodificar la imagen base64
        image = base64.b64decode(image_data)

        # Convertir la imagen a un objeto PIL
        image = Image.open(io.BytesIO(image))
        
        # Convertir la imagen a escala de grises y redimensionar a 28x28 píxeles
        image = image.convert('L')
        image = image.resize((28, 28))  # Redimensionar a 28x28 píxeles

        # Convertir la imagen a un array numpy y normalizar
        image = np.array(image) / 255.0
        image = image.reshape(1, 28, 28, 1)  # Formato esperado por el modelo

        # Realizar la predicción
        prediction = model.predict(image)
        digit = np.argmax(prediction)

        # Retornar el resultado como JSON
        return jsonify({'digit': str(digit)})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Hubo un problema procesando la imagen.'}), 400

if __name__ == '__main__':
    app.run(debug=True)