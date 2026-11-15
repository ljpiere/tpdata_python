import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


# DESCOMENTA LAS SECCIONES DE ACUERDO A LO QUE QUIERAS PONER A LA SUERTE DE LA RULETA

rules = [
    # # Datos personales
    # "El más joven",
    # "El que vive más lejos",
    # "El más alto",
    # "El que tiene más mascotas",
    # "El que tiene más hermanos",
    # "El que cumple años más pronto",

    # # Tecnología
    # "Más experiencia programando",
    # "Menos experiencia programando",
    # "El que usa más monitores",
    # "El que tiene más pestañas abiertas",
    # "El que tiene más repositorios en GitHub",
    # "El que aprendió una tecnología nueva este mes",

    # Estudio
    "Más cursos terminados",
    "El que terminó primero el sprint",
    "El que más preguntas hizo esta semana",
    "El que más ayudó a un compañero",
    "El que tomó más notas",
    "El que revisó más veces su proyecto antes de entregarlo",

    # # Hábitos
    # "El que durmió más tarde",
    # "El que se despertó más temprano",
    # "Más café hoy",
    # "Menos café hoy",
    # "El que lleva más tiempo sentado",
    # "El que hizo ejercicio hoy",

    # # Curiosidades
    # "Username más largo",
    # "Username más corto",
    # "El que tiene el fondo de pantalla más extraño",
    # "El que escuchó más música hoy",
    # "El que tiene más aplicaciones abiertas",
    # "El que tiene más stickers en WhatsApp",

    # Azar divertido
    "El nombre con más letras",
    "El nombre con menos letras",
    "El que tenga el objeto más cercano de color rojo",
    "El que tenga más batería en su dispositivo",
    "El que tenga menos batería en su dispositivo",
    "El último que escribió en el chat",
    "El que tenga el número favorito más grande",
    "El que haya viajado a más ciudades"
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