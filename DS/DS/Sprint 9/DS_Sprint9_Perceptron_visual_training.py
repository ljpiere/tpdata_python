import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.datasets import make_blobs

# -----------------------------
# Datos de ejemplo (lineales)
# -----------------------------
X, y = make_blobs(
    n_samples=50,
    centers=2,
    random_state=1,
    cluster_std=3,
    center_box= (0.0,20.0)
)

# -----------------------------
# Perceptrón
# -----------------------------
class Perceptron:
    def __init__(self, lr=0.1):
        self.lr = lr
        self.w = np.zeros(2)
        self.b = 0
        self.history = []

    def activation(self, z):
        return 1 if z >= 0 else 0

    def train_step(self, x, y_true):
        z = np.dot(x, self.w) + self.b
        y_pred = self.activation(z)
        error = y_true - y_pred

        self.w += self.lr * error * x
        self.b += self.lr * error

# -----------------------------
# Entrenamiento paso a paso
# -----------------------------
model = Perceptron(lr=0.1)

for epoch in range(50):

    for i in range(len(X)):
        model.train_step(X[i], y[i])

    # guardar solo al final de la época
    model.history.append((model.w.copy(), model.b))
# -----------------------------
# Visualización
# -----------------------------
fig, ax = plt.subplots()

# Puntos
ax.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color="blue", label="Clase 0")
ax.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color="red", label="Clase 1")

line, = ax.plot([], [], 'k--', linewidth=2)
title = ax.text(0.5, 1.05, "", transform=ax.transAxes, ha="center")

ax.legend()

# -----------------------------
# Función de animación
# -----------------------------
def update(frame):
    w, b = model.history[frame]

    if w[1] != 0:
        x_vals = np.array([0, 30])
        y_vals = -(w[0] * x_vals + b) / w[1]
        line.set_data(x_vals, y_vals)

    title.set_text(f"Iteración {frame + 1}")
    return line, title

ani = FuncAnimation(
    fig,
    update,
    frames=len(model.history),
    interval=300,
    repeat=False
)

plt.show()
