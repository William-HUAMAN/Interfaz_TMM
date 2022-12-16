import numpy as np
import matplotlib.pyplot as plt

'Primero hallamos tetha4'

a = 0.21993 #Eslabon 2
b = 0.81401 #Eslabon 3
c = 0.95858 #Eslabon 4
d = 1.20 #Eslabon 1
r6 = 0.64142


o2x = 0
o2y = 0
o4x = 0.96
o4y = 0.72

tetha1 = np.arctan2(o4y-o2y,o4x-o2x) * 180/np.pi

def t4(x):

    'NORTON'
    t2 = x - tetha1
    K1 = d/a
    K2 = d/c
    K3 = (a**2 - b**2 + c**2 +d**2)/(2*a*c)
    A = np.cos((t2) * np.pi / 180) - K1 - K2* (np.cos((t2)* np.pi / 180)) + K3
    B = -2 * np.sin((t2) * np.pi/ 180)
    C = K1 - (K2 + 1) * np.cos((t2) * np.pi / 180) + K3
    num1 = -B + np.sqrt((B ** 2)-(4 * A * C))
    den1 = 2 * A
    t4 = 2 * np.arctan2(num1,den1) * 180 / np.pi
    return t4 + tetha1


# 'Ahora hallamos tetha3'

def t3(x):

    'NORTON'
    t2 = x - tetha1
    K4 = d/b
    K1 = d/a
    K5 = (c**2 - d**2 - a**2 - b**2)/(2*a*b)
    D = np.cos((t2) * np.pi / 180) - K1 + K4*(np.cos((t2)* np.pi / 180)) + K5
    E = -2 * np.sin((t2) * np.pi/ 180)
    F = K1 + (K4 - 1) * np.cos((t2) * np.pi / 180) + K5

    num2 = - E + np.sqrt(E ** 2 - 4 * D * F)
    den2 = 2 * D
    t3 = 2 * np.arctan2(num2,den2) * 180 / np.pi
    return t3 +tetha1


# POSICIÓN DE LOS PUNTOS DE INTERÉS

tetha2 = 90 - tetha1 #THETA 2 VARÍA DE 0 A 360

'Punto A'

rax = a * np.cos((tetha2) * np.pi / 180) 
ray = a * np.sin((tetha2) * np.pi / 180) 
ax = []
ay = []
'Punto B'

rbx = a * np.cos((tetha2) * np.pi / 180) + b * np.cos((t3(tetha2)) * np.pi / 180) 
rby = a * np.sin((tetha2) * np.pi / 180) + b * np.sin((t3(tetha2)) * np.pi / 180) 
bx = []
by = []


for tetha2 in range(0,360,6):
    rx = d * np.cos((tetha1) * np.pi / 180) + r6 * np.cos((t4(tetha2)+180) * np.pi / 180)
    px.append(rx)
    ry = d * np.sin((tetha1) * np.pi / 180) + r6 * np.sin((t4(tetha2)+180) * np.pi / 180)
    py.append(ry)

for tetha2 in range(0,360,6):
    rx = a * np.cos((tetha2) * np.pi / 180) 
    ax.append(rx)
    ry = a * np.sin((tetha2) * np.pi / 180)
    ay.append(ry)

for tetha2 in range(0,360,6):
    rx = a * np.cos((tetha2) * np.pi / 180) + b * np.cos((t3(tetha2)) * np.pi / 180)
    bx.append(rx)
    ry = a * np.sin((tetha2) * np.pi / 180) + b * np.sin((t3(tetha2)) * np.pi / 180)
    by.append(ry)

for tetha2 in range(0,360,6):
    rx = a * np.cos((tetha2) * np.pi / 180) + (b*0.5) * np.cos((t3(tetha2)) * np.pi / 180)
    qx.append(rx)
    ry = a * np.sin((tetha2) * np.pi / 180) + (b*0.5) * np.sin((t3(tetha2)) * np.pi / 180)
    qy.append(ry)


# plt.plot(px,py,'r.')
plt.plot(ax,ay,'g.')
plt.plot(bx,by,'b.')
# plt.plot(qx,qy,'r.')
plt.title('Trayectoria de los puntos de interes')
plt.show()