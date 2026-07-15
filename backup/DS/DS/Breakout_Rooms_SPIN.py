import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

rules = [
    "El más joven",
    "El que vive más lejos",
    "El más alto",
    "El más deportista",
    "Más experiencia programando",
    "El que durmió más tarde",
    "Más café hoy",
    "Más cursos terminados",
    "Username más largo",
    "Más mascotas"
]

n = len(rules)

angles = np.linspace(0, 2*np.pi, n, endpoint=False)

fig, ax = plt.subplots(figsize=(6,6))

ax.set_aspect("equal")
ax.axis("off")

colors = plt.cm.tab20(np.linspace(0,1,n))

wedges = []

for i, angle in enumerate(angles):
    wedge = plt.matplotlib.patches.Wedge(
        (0,0),
        1,
        np.degrees(angle),
        np.degrees(angle + 2*np.pi/n),
        facecolor=colors[i]
    )
    ax.add_patch(wedge)

    x = 0.7*np.cos(angle + np.pi/n)
    y = 0.7*np.sin(angle + np.pi/n)

    ax.text(
        x, y,
        rules[i],
        ha="center",
        va="center",
        fontsize=9,
        rotation=np.degrees(angle + np.pi/n)
    )

pointer, = ax.plot([0,0],[0,1.1], lw=4, color="black")

spin_speed = 0.3
angle = 0

chosen_index = random.randint(0, n-1)

target_angle = 2*np.pi*(5) + angles[chosen_index]

def update(frame):
    global angle

    if angle < target_angle:
        angle += spin_speed

    pointer.set_data(
        [0, np.cos(angle)],
        [0, np.sin(angle)]
    )

    return pointer,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=200,
    interval=30,
    blit=True
)

plt.show()

print("Elegido:", rules[chosen_index])