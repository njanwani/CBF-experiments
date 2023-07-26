import matplotlib.pyplot as plt
import numpy as np

HORIZON = 2
DT = 0.01
DIM = 2


def integrate(v, w, dt, horizon, theta=0):
    states = [np.zeros(DIM)]
    for i in range(1, int(horizon / dt)):
        curr = dt * np.array([v * np.cos(theta), v * np.sin(theta)])
        states.append(states[i - 1] + curr)
        theta += w * dt

    return np.array(states)


x = np.array([0,0])
v = np.array([0.5, np.pi / 4])

states = x + integrate(v[0], v[1], DT, HORIZON)
plt.plot(states[:,0], states[:,1])
plt.show()