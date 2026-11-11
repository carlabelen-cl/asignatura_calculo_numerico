import numpy as np
import matplotlib.pyplot as plt

c = np.linspace(1, 25 , 1000)
def f(c):
      return ((c**3) + c + 1)
 # c = np.linspace(1, 25, 400)
plt.plot(c, f(c), color='#065A82')
plt.axhline(0, color='gray', lw=0.8)
plt.xlabel('c'); plt.ylabel('f(c)')
plt.grid(alpha=0.3)
plt.show()
# Reto: repita con sen(10x)+cos(3x)

