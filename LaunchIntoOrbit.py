import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
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
V, h, g, F, m, ugol, p = 0, 0, 9.8, 237666, 42900, 0, 1.29
t = np.arange(0.0, 200, 0.1)
Vy, Vx, deltav, deltah = [0] * len(t), [0] * len(t), [0] * len(t), [0] * len(t)
deltam, deltaa = [m] + ([0] * (len(t) - 1)), [5.54] + ([0] * (len(t) - 1))
for dot in t[1:]:
    dot_indx = int(dot * 10)
    radian = ugol * math.pi / 180
    a_x = (F * math.cos(radian) - 0.5 * 0.055 * p * 20 * (V ** 2) * math.cos(radian)) / m
    a_y = (F * math.sin(radian) - m * g - 0.5 * 0.055 * p * 20 * (V ** 2) * math.sin(radian)) / m
    p = 1.29 * math.exp(-m * g * h / 414 * (10 ** -23))
    g = (39.85992 * (10 ** 13)) / (6400000 + h) ** 2
    h = (deltav[dot_indx - 1] ** 2) / (2 * deltaa[dot_indx - 1])
    ugol = 0.45 * dot
    F += 0.13
    m -= 0.14
    Vx[dot_indx] = Vx[dot_indx - 1] + a_x * 0.1
    Vy[dot_indx] = Vy[dot_indx - 1] + a_y * 0.1
    deltav[dot_indx] = (Vy[dot_indx] ** 2 + Vx[dot_indx] ** 2) ** 0.5
    deltam[dot_indx] = m
    deltaa[dot_indx] = a_y + 15
    deltah[dot_indx] = h
plt.figure(figsize=(12, 10))
plt.subplot(221)
plt.xlabel(r'$t$')
plt.title(r'$V$')
plt.plot(t, deltav)
plt.plot(data['Time'], data['Velocity'])
plt.grid(True)
plt.subplot(222)
plt.xlabel(r'$t$')
plt.title(r'$a$')
plt.plot(t, deltaa)
plt.plot(data['Time'], data['Acceleration'])
plt.grid(True)
plt.subplot(223)
plt.xlabel(r'$t$')
plt.title(r'$m$')
plt.plot(t, deltam)
plt.plot(data["Time"], data["Mass"])
plt.grid(True)
plt.subplot(224)
plt.xlabel(r'$t$')
plt.title(r'$h$')
plt.plot(t, deltah)
plt.plot(data["Time"], list(map(lambda x: -1 * int(x) * 100, data["AltitudeFromSea"])))
plt.grid(True)
plt.show()
