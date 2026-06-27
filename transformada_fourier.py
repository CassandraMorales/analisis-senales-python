import numpy as np
import matplotlib.pyplot as plt

# ANÁLISIS DE SEÑALES Y SISTEMAS

# PARÁMETROS GENERALES
fs = 1000                    # Frecuencia de muestreo (Hz)
T = 2                        # Duración total (s)
t = np.arange(-1, 1, 1/fs)   # Vector de tiempo

# DEFINICIÓN DE LAS SEÑALES

# Señal senoidal
f = 5
senal_seno = np.sin(2*np.pi*f*t)

# Pulso rectangular
pulso = np.where((t >= -0.2) & (t <= 0.2), 1, 0)

# Función escalón
escalon = np.where(t >= 0, 1, 0)

# FUNCIÓN PARA CALCULAR LA TRANSFORMADA DE FOURIER

def calcular_fft(senal):

    N = len(senal)

    fft = np.fft.fft(senal)

    # Normalización
    fft = fft / N

    fft = np.fft.fftshift(fft)

    freqs = np.fft.fftfreq(N, d=1/fs)

    freqs = np.fft.fftshift(freqs)

    return freqs, fft


# FUNCIÓN PARA GRAFICAR

def graficar_senal(t, senal, freq, fft, titulo):

    plt.figure(figsize=(13,8))

    # Dominio del tiempo
    plt.subplot(3,1,1)
    plt.plot(t, senal)
    plt.title(f"{titulo} - Dominio del tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # Magnitud
    plt.subplot(3,1,2)
    plt.plot(freq, np.abs(fft))
    plt.title("Magnitud del espectro")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|X(f)|")
    plt.grid(True)

    # Fase
    plt.subplot(3,1,3)
    plt.plot(freq, np.angle(fft))
    plt.title("Fase del espectro")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Fase (rad)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# CALCULAR FFT DE CADA SEÑAL

freq_seno, fft_seno = calcular_fft(senal_seno)

freq_pulso, fft_pulso = calcular_fft(pulso)

freq_escalon, fft_escalon = calcular_fft(escalon)

# GRAFICAR LAS SEÑALES

graficar_senal(t, senal_seno, freq_seno, fft_seno,
               "Señal senoidal")

graficar_senal(t, pulso, freq_pulso, fft_pulso,
               "Pulso rectangular")

graficar_senal(t, escalon, freq_escalon, fft_escalon,
               "Función escalón")


# PROPIEDAD DE LINEALIDAD

senal_suma = senal_seno + pulso

freq_suma, fft_suma = calcular_fft(senal_suma)

plt.figure(figsize=(10,5))

plt.plot(freq_suma,
         np.abs(fft_suma),
         label="FFT{x+y}")

plt.plot(freq_suma,
         np.abs(fft_seno + fft_pulso),
         "--",
         label="FFT{x}+FFT{y}")

plt.title("Verificación de la propiedad de linealidad")

plt.xlabel("Frecuencia (Hz)")

plt.ylabel("Magnitud")

plt.grid(True)

plt.legend()

plt.show()


# DESPLAZAMIENTO EN EL TIEMPO

desplazamiento = 0.3

senal_desplazada = np.sin(
    2*np.pi*f*(t-desplazamiento)
)

freq_des, fft_des = calcular_fft(senal_desplazada)

plt.figure(figsize=(12,8))

plt.subplot(2,1,1)

plt.plot(freq_seno,
         np.abs(fft_seno),
         label="Original")

plt.plot(freq_des,
         np.abs(fft_des),
         "--",
         label="Desplazada")

plt.title("Magnitud del espectro")

plt.grid(True)

plt.legend()

plt.subplot(2,1,2)

plt.plot(freq_seno,
         np.angle(fft_seno),
         label="Original")

plt.plot(freq_des,
         np.angle(fft_des),
         "--",
         label="Desplazada")

plt.title("Fase del espectro")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()


# ESCALAMIENTO EN FRECUENCIA

# Señal original (5 Hz)

senal_5 = np.sin(2*np.pi*5*t)

# Señal con frecuencia duplicada (10 Hz)

senal_10 = np.sin(2*np.pi*10*t)

freq5, fft5 = calcular_fft(senal_5)

freq10, fft10 = calcular_fft(senal_10)

plt.figure(figsize=(11,5))

plt.plot(freq5,
         np.abs(fft5),
         label="5 Hz")

plt.plot(freq10,
         np.abs(fft10),
         "--",
         label="10 Hz")

plt.title("Escalamiento en frecuencia")

plt.xlabel("Frecuencia (Hz)")

plt.ylabel("Magnitud")

plt.grid(True)

plt.legend()

plt.show()
