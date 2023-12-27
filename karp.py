import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

data = pd.read_csv("data.csv")
parameters = ['Time',
              'Velocity',
              'GForce',
              'Acceleration',
              'Thrust',
              'TWR', 'Mass',
              'AltitudeFromTerrain',
              'AltitudeFromSea',
              'DownrangeDistance',
              'Latitude',
              'Longitude',
              'Apoapsis',
              'Periapsis',
              'Inclination',
              'OrbitalVelocity']
for col in data.columns:
    if col not in parameters:
        data.drop(col, axis=1, inplace=True)
data.head()

s = 20
c = 0.045
p = 1.29
p0 = 1.29
m = 42900
kT = 414 * (10 ** -23)
b = 0.45
GM = 39.85992 * (10 ** 13)
R = 6400000
F = m * 5.54
g = 9.8
q = 1.2
V = 0
h = 0
a = 5.54
eps = 1
alfa = 0
pi = math.pi

t = np.arange(0.0, 200, 0.1)
dots_count = len(t)
all_Vy = [0] * dots_count
all_Vx = [0] * dots_count
all_V = [0] * dots_count
all_m = [m] + ([0] * (dots_count - 1))
all_a = [a] + ([0] * (dots_count - 1))
all_h = [0] * dots_count

for dot in t[1:]:
    i = int(dot * 10)
    alfa_rad = alfa * pi / 180
    a_x = (F * math.cos(alfa_rad) - 0.5 * c * p * s * (V ** 2) * math.cos(alfa_rad)) / m
    a_y = (F * math.sin(alfa_rad) - 0.5 * c * p * s * (V ** 2) * math.sin(alfa_rad) - m * g) / m
    alfa = b * dot
    p = p0 * math.exp(-m * g * h / kT)
    F += eps * 0.1
    m -= q * 0.1
    g = GM / (R + h) ** 2
    h = (all_V[i - 1] ** 2) / (2 * a)
    all_Vy[i] = all_Vy[i - 1] + a_y * 0.1
    all_Vx[i] = all_Vx[i - 1] + a_x * 0.1
    all_V[i] = (all_Vy[i] ** 2 + all_Vx[i] ** 2) ** 0.5
    all_m[i] = m
    all_a[i] = a_y + 15
    all_h[i] = h

plt.figure(figsize=(12, 10))

plt.subplot(221)
plt.grid(True)
plt.xlabel(r'$t, с$')
plt.title(r'$V, м/с$')
plt.plot(t, all_V)
plt.plot(data['Time'], data['Velocity'])
plt.subplot(222)
plt.xlabel(r'$t, с$')
plt.title(r'$a, м/с^2$')
plt.plot(t, all_a)
plt.plot(data['Time'], data['Acceleration'])
plt.grid(True)

plt.subplot(223)
plt.xlabel(r'$t, с$')
plt.title(r'$m, кг$')
plt.plot(t, all_m)
plt.plot(data["Time"], data["Mass"])
plt.grid(True)

plt.subplot(224)
plt.xlabel(r'$t, с$')
plt.title(r'$h, м/с$')
plt.plot(t, all_h)
plt.plot(data["Time"], list(map(lambda x: -1 * int(x) * 100, data["AltitudeFromSea"])))
plt.grid(True)
plt.show()