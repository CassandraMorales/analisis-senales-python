# 📊 Análisis de Señales y Sistemas con Python

## 📌 Descripción
Este proyecto tiene como objetivo analizar señales en el dominio del tiempo y la frecuencia utilizando Python. Se aplica la Transformada de Fourier para observar cómo diferentes señales se representan en ambos dominios.

---

## 🧠 Conceptos aplicados
- Representación de señales en el dominio del tiempo
- Transformada de Fourier
- Espectro de magnitud y fase
- Propiedades de Fourier:
  - Linealidad
  - Desplazamiento en el tiempo
  - Escalamiento en frecuencia

---

## ⚙️ Tecnologías utilizadas
- Python
- NumPy
- Matplotlib

---

## 📈 Señales analizadas
- Señal senoidal
- Pulso rectangular
- Función escalón

---

## 🔬 Resultados

### ✅ Dominio del tiempo
Se observan las formas originales de cada señal.

### ✅ Dominio de la frecuencia
- La señal senoidal presenta picos en ±f
- El pulso rectangular muestra una forma tipo sinc
- La función escalón contiene principalmente bajas frecuencias

---

## 🔍 Propiedades verificadas

### Linealidad
Se verifica que:
FFT(x + y) = FFT(x) + FFT(y)

### Desplazamiento en el tiempo
La magnitud del espectro no cambia, pero la fase sí.

### Escalamiento en frecuencia
Al aumentar la frecuencia de la señal, los picos se desplazan en el espectro.

---

## 📁 Estructura del proyecto
