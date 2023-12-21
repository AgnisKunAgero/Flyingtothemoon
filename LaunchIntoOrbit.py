import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv("data.csv")
parameters = ['Time',
              'Velocity',
              'GForce',
              'Acceleration',
              'Thrust',
              'TWR','Mass',
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
    data.drop(col, axis = 1, inplace= True)
data.head()
plt.plot(data["Time"],data["Velocity"])
plt.xlabel('t')
plt.ylabel('v')
plt.show()
plt.plot(data["Time"],data["Acceleration"])
plt.xlabel('t')
plt.ylabel('a')
plt.show()
plt.plot(data["Time"],data["Mass"])
plt.xlabel('t')
plt.ylabel('m')
plt.show()
plt.plot(data["Time"],data["AltitudeFromSea"])
plt.xlabel('t')
plt.ylabel('h')
plt.show()