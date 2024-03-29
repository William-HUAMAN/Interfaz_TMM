import numpy as np
import math


def sen(a):
    a = np.radians(a)
    return np.sin(a)


def cos(a):
    a = np.radians(a)
    return np.cos(a)


def arctangente(a, b):
    return math.degrees(np.arctan2(a, b))


def raiz_cuadrada(a):
    return np.sqrt(a)


# Función principal que realiza el análisis
def analyze(O2_x, O2_y, O4_x, O4_y, L_2, L_3, L_4, p, theta_2, omega_2, alpha_2, delta_3):
    O2x = float(O2_x)
    O2y = float(O2_y)
    O4x = float(O4_x)
    O4y = float(O4_y)
    L2 = float(L_2)
    L3 = float(L_3)
    L4 = float(L_4)
    P = float(p)
    theta2 = float(theta_2)
    omega2 = float(omega_2)
    alpha2 = float(alpha_2)
    delta3 = float(delta_3)
    lista = [O2x, O2y, O4x, O4y, L2, L3, L4, P, theta2, omega2, alpha2, delta3]
    # print(lista)
    # Obteniendo valores:
    L1 = raiz_cuadrada((O4x - O2x) ** 2 + (O4y - O2y) ** 2)

    # print(lista_grashof[0]+lista_grashof[3])

    Ax = L2 * cos(theta2)
    Ay = L2 * sen(theta2)
    S_aux = ((L2 ** 2) - (L3 ** 2) + (L4 ** 2) - (L1 ** 2)) / (2 * (Ax - L1))
    P_aux = ((Ay ** 2) / (Ax - (L1 ** 2))) + 1
    Q_aux = (2 * Ay * (L1 - S_aux)) / (Ax - L1)
    R_aux = ((L1 - S_aux) ** 2) - (L4 ** 2)
    By = -Q_aux + (raiz_cuadrada((Q_aux ** 2) - 4 * P_aux * R_aux) / (2 * P_aux))
    Bx = S_aux - ((2 * Ay * By) / (2 * (Ax - L1)))
    theta3 = arctangente((By - Ay), (Bx - Ax))  # valores en sexagesimales
    theta4 = arctangente(By, (Bx - L1))  # valores en sexagesimales
    omega3 = (L2 * omega2 / L3) * ((sen(theta4 - theta2)) / (sen(theta3 - theta4)))
    omega4 = (L2 * omega2 / L4) * ((sen(theta2 - theta3)) / (sen(theta4 - theta3)))
    V_A = L2 * omega2
    V_BA = L3 * omega3
    V_B = L4 * omega4

    Vax = -L2 * omega2 * sen(theta2)
    Vay = L2 * omega2 * cos(theta2)
    Vpax = -P * omega3 * sen(theta3 + delta3)
    Vpay = P * omega3 * cos(theta3 + delta3)
    V_P = raiz_cuadrada(((Vax + Vpax) ** 2 )+ ((Vpay + Vay) ** 2))

    nA = L4 * sen(theta4)
    nB = L3 * sen(theta3)
    nC = L2 * alpha2 * sen(theta2) + L2 * (omega2 ** 2) * cos(theta2) + L3 * (omega3 ** 2) * cos(theta3) - L4 * (
                omega4 ** 2) * cos(theta4)
    nD = L4 * cos(theta4)
    nE = L3 * cos(theta3)
    nF = L2 * alpha2 * cos(theta2) - L2 * (omega2 ** 2) * sen(theta2) - L3 * (omega3 ** 2) * sen(theta3) + L4 * (
                omega4 ** 2) * sen(theta4)

    alpha3 = (nC * nD - nA * nF) / (nA * nE - nB * nD)
    alpha4 = (nC * nE - nB * nF) / (nA * nE - nB * nD)

    mod_A = raiz_cuadrada(float((L2 * (omega2 ** 2)) ** 2 + (L2 * alpha2) ** 2))
    mod_BA = raiz_cuadrada(float((L3 * (omega3 ** 2)) ** 2 + (L3 * alpha3) ** 2))
    mod_B = raiz_cuadrada(float((L4 * (omega4 ** 2)) ** 2 + (L4 * alpha4) ** 2))

    tabla = [theta2, round(Ax, 2), round(Ay, 2), round(Bx, 2), round(By, 2), round(theta3, 2), round(theta4, 2),
             round(omega2, 2), round(omega3, 2), round(omega4, 2), round(V_A, 2), round(V_B,2), round(V_P,2),
             round(mod_A,2),round(mod_BA,2), round(mod_B,2)]
    return tabla
