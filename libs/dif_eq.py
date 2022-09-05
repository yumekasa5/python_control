"""常微分方程式"""
from cProfile import label
from scipy.integrate import odeint  #常微分方程式のライブラリ
import numpy as np
import matplotlib.pyplot as plt


def system(y: float, t: float) -> float:
    """微分方程式の定義"""
    if t < 10.0:
        u = 0.0
    else:
        u = 1.0
    dydt = (-y + u)/5.0
    return dydt

y0 = 0.5
t = np.arange(0, 40, 0.04)
y = odeint(system, y0, t)

fig, ax = plt.subplots()
ax.plot(t, y, label='y')
ax.plot(t, 1 * (t>=10), ls='--', label='u')
ax.set_xlabel('t')
ax.set_ylabel('y, u')
ax.legend(loc='best')
ax.grid(ls=':')
plt.show()