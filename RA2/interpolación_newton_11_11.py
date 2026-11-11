import numpy as np

def dif_divididas(x, y):
    """Devuelve los coeficientes b_k de Newton (diagonal superior de la tabla)."""
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (x[i+j] - x[i])
    return F[0, :]

def newton_eval(x, b, xx):
    """Evalúa la forma de Newton con un esquema tipo Horner."""
    p = b[-1]
    for k in range(len(b) - 2, -1, -1):
        p = p * (xx - x[k]) + b[k]
    return p

T = np.array([1.0, 2.0, 3.0])
o = np.array([2.0, 1.0, 4.0])


b = dif_divididas(T, o)

print("Coeficientes b_k:", b) 



val_eval = newton_eval(T, b, 2.5)
print("Evaluación en xx = 2.5:", val_eval)
