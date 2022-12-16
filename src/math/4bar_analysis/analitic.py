# import numpy as np
# import matplotlib.pyplot as plt

'Parámetros de entrada'

a = 0.21993 #Eslabon 2
b = 0.81401 #Eslabon 3
c = 0.95858 #Eslabon 4
d = 1.20 #Eslabon 1



o2x = 0
o2y = 0
o4x = 0.96
o4y = 0.72

tetha1 = np.arctan2(o4y-o2y,o4x-o2x) * 180/np.pi
print(tetha1)
def t4(x1):
    
    t2 = x1 - tetha1
    K1 = d/a
    K2 = d/c
    K3 = (a**2 - b**2 + c**2 +d**2)/ (2*a*c)
    A = np.cos((t2) * np.pi / 180) - K1 - K2* (np.cos((t2)* np.pi / 180)) + K3
    B = -2 * np.sin((t2) * np.pi/ 180)
    C = K1 - (K2 + 1) * np.cos((t2) * np.pi / 180) + K3
    num1 = -B + np.sqrt((B ** 2)-(4 * A * C))
    den1 = 2 * A
    t4 = 2 * np.arctan2(num1,den1) * 180 / np.pi
    # print(t4)
    return t4 + tetha1

'Ahora hallamos tetha3'

def t3(x2):
    
    t2 = x2 - tetha1
    K4 = d/b
    K1 = d/a
    K5 = (c**2 - d**2 - a**2 - b**2)/ (2*a*b)
    D = np.cos((t2) * np.pi / 180) - K1 + K4* (np.cos((t2)* np.pi / 180)) + K5
    E = -2 * np.sin((t2) * np.pi/ 180)
    F = K1 + (K4 - 1) * np.cos((t2) * np.pi / 180) + K5

    num2 = - E + np.sqrt(E ** 2 - 4 * D * F)
    den2 = 2 * D
    t3 = 2 * np.arctan2(num2,den2) * 180 / np.pi
    # print(t3)
    return t3 + tetha1

t2 = 90 - tetha1
print(t3(t2))
print(t4(t2))