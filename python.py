import numpy as np
import matplotlib.pyplot as plt

GRAVEDAD = 6.67430e-11

print("Simulador de Órbita en un Campo Gravitatorio")

masa_cuerpo_central = float(input("Introduce la masa del cuerpo central (kg): "))
distancia_inicial = float(input("Introduce la distancia inicial del satélite (m): "))
velocidad_inicial = float(input("Introduce la velocidad inicial del satélite (m/s): "))
masa_satelite = float(input("Introduce la masa del satélite (kg): "))

delta_tiempo = 10
numero_pasos = 10000

posicion_inicial = np.array([distancia_inicial, 0])
velocidad_inicial_vector = np.array([0, velocidad_inicial])

posiciones = np.zeros((numero_pasos, 2))
velocidades = np.zeros((numero_pasos, 2))
posiciones[0] = posicion_inicial
velocidades[0] = velocidad_inicial_vector

for paso in range(1, numero_pasos):
    distancia_actual = np.linalg.norm(posiciones[paso - 1])
    aceleracion = -GRAVEDAD * masa_cuerpo_central * posiciones[paso - 1] / distancia_actual**3
    velocidades[paso] = velocidades[paso - 1] + aceleracion * delta_tiempo
    posiciones[paso] = posiciones[paso - 1] + velocidades[paso] * delta_tiempo

posicion_final = posiciones[-1]
velocidad_final = velocidades[-1]
distancia_final = np.linalg.norm(posicion_final)
velocidad_final_magnitud = np.linalg.norm(velocidad_final)

energia_cinetica = 0.5 * masa_satelite * velocidad_final_magnitud**2
energia_potencial = -GRAVEDAD * masa_cuerpo_central * masa_satelite / distancia_final
energia_mecanica_total = energia_cinetica + energia_potencial

print("\n--- Resultados Finales ---")
print(f"Posición final: x = {posicion_final[0]:.2f} m, y = {posicion_final[1]:.2f} m")
print(f"Velocidad final: vx = {velocidad_final[0]:.2f} m/s, vy = {velocidad_final[1]:.2f} m/s")
print(f"Energía cinética final: {energia_cinetica:.2e} J")
print(f"Energía potencial gravitatoria final: {energia_potencial:.2e} J")
print(f"Energía mecánica total final: {energia_mecanica_total:.2e} J")

plt.figure(figsize=(8, 8))
plt.plot(posiciones[:, 0], posiciones[:, 1], label="Órbita del satélite")
plt.plot(0, 0, 'yo', label="Cuerpo central")
plt.xlabel("Posición X (m)")
plt.ylabel("Posición Y (m)")
plt.title("Simulación de la órbita")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()
