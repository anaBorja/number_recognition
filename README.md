# 🤖 Reconocimiento de Dígitos - Código Postal

Este proyecto utiliza una **Red Neuronal Convolucional (CNN)** para el reconocimiento de dígitos escritos a mano, basado en el dataset **MNIST**. El modelo es desplegado a través de una aplicación web utilizando **Flask** y un frontend interactivo en **HTML** y **CSS**. Los usuarios pueden dibujar un dígito en una pizarra virtual o cargar una imagen para obtener una predicción.

---

## 🚀 Tecnologías Utilizadas

- **TensorFlow**: Para construir y entrenar el modelo de red neuronal.
- **Flask**: Framework web para desplegar el modelo.
- **HTML/CSS**: Para la creación del frontend interactivo.
- **NumPy**: Para el manejo de datos numéricos.
- **Matplotlib/Seaborn**: Para la visualización de los resultados.
- **scikit-learn**: Para la división de datos y otras tareas de preprocesamiento.

---

## 🛠️ Preparación del Entorno

 **Instalación de bibliotecas**

   Asegúrate de tener instaladas las siguientes bibliotecas:

   ```bash
   pip install tensorflow matplotlib numpy scikit-learn flask imbalanced-learn
   ```
   
---
# 📊 Carga y Preprocesamiento del Dataset
- Cargar el dataset **MNIST** y normalizar las imágenes.
- Visualizar las primeras imágenes del conjunto de entrenamiento.

---

# 🧠 Construcción del Modelo
- Definir la arquitectura del modelo de **Red Neuronal Convolucional (CNN)**.
- Compilar el modelo con **Adam** y la función de pérdida adecuada.

---

# 🚀 Entrenamiento y Evaluación del Modelo
- Entrenar el modelo durante varias **épocas** y registrar el rendimiento.
- Evaluar el modelo en el conjunto de prueba y obtener la precisión.

---

# 🎨 Visualización de Resultados
- Graficar la **precisión** y **pérdida** durante el entrenamiento.
- Mostrar la **matriz de confusión** para evaluar el rendimiento de las predicciones.

---

# 🌐 Despliegue del Modelo
- Guardar el modelo entrenado en un archivo `.h5`.
- Crear la aplicación **Flask** para recibir imágenes y hacer predicciones.

---

# 🌍 Interfaz Web
El frontend consiste en una interfaz interactiva donde los usuarios pueden:
- Dibujar un dígito en una pizarra virtual.
- Subir una imagen para realizar la predicción.
- Mostrar el resultado de la predicción del dígito.

---

# 📄 Conclusión
Este proyecto demuestra cómo construir un sistema de reconocimiento de dígitos utilizando una **Red Neuronal Convolucional** y desplegarlo en una **aplicación web interactiva**. Es una excelente manera de aprender sobre la construcción y despliegue de modelos de **IA**.

---

# 📚 Recursos
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)

---

🎉 ¡Listo para probarlo! 😄


