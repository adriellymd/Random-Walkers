import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
from matplotlib.animation import FuncAnimation  # Adição da importação necessária
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def caminhante(num_caminhantes, num_passos):
    if num_caminhantes > 10:
        raise ValueError("O número de caminhantes não pode exceder 10.")

    n = num_passos
    x = np.zeros((num_caminhantes, n))
    y = np.zeros((num_caminhantes, n))
    z = np.zeros((num_caminhantes, n))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    linhas = []  # Alteração do nome da variável para 'linhas'

    for i in range(num_caminhantes):
        linha, = ax.plot([], [], [], color=plt.cm.tab10(i))  # Alteração para 'linha'
        linhas.append(linha)

    def init():
        ax.set_xlim((-n / 2), (n / 2))
        ax.set_ylim((-n / 2), (n / 2))
        ax.set_zlim((-n / 2), (n / 2))
        return linhas

    def update(frame):
        for i in range(num_caminhantes):
            r = random.randint(1, 6)
            if r == 1:
                x[i, frame] = x[i, frame - 1] + 1
                y[i, frame] = y[i, frame - 1]
                z[i, frame] = z[i, frame - 1]
            elif r == 2:
                x[i, frame] = x[i, frame - 1] - 1
                y[i, frame] = y[i, frame - 1]
                z[i, frame] = z[i, frame - 1]
            elif r == 3:
                x[i, frame] = x[i, frame - 1]
                y[i, frame] = y[i, frame - 1] + 1
                z[i, frame] = z[i, frame - 1]
            elif r == 4:
                x[i, frame] = x[i, frame - 1]
                y[i, frame] = y[i, frame - 1] - 1
                z[i, frame] = z[i, frame - 1]
            elif r == 5:
                x[i, frame] = x[i, frame - 1]
                y[i, frame] = y[i, frame - 1]
                z[i, frame] = z[i, frame - 1] + 1
            else:
                x[i, frame] = x[i, frame - 1]
                y[i, frame] = y[i, frame - 1]
                z[i, frame] = z[i, frame - 1] - 1

            linhas[i].set_data(x[i, :frame + 1], y[i, :frame + 1])
            linhas[i].set_3d_properties(z[i, :frame + 1])

        return linhas

    ani = FuncAnimation(fig, update, frames=range(1, n), init_func=init, blit=True)

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f"Caminho aleatório em {n} passos")
    ax.grid()
    print("Carregando...")
    ani.save('random_walk.gif', writer='ffmpeg')

def start_random_walk():
    num_caminhantes = int(spinbox_walkers.get())
    num_passos = int(entry_steps.get())
    caminhante(num_caminhantes, num_passos)

janela = Tk()
janela.title("Caminho aleatório 3D")

label_walkers = Label(janela, text="Número de Caminhantes:")
label_walkers.grid(row=0, column=0, padx=10, pady=10)

spinbox_walkers = Spinbox(janela, from_=1, to=10)
spinbox_walkers.grid(row=0, column=1, padx=10, pady=10)

label_steps = Label(janela, text="Número de passos:")
label_steps.grid(row=1, column=0, padx=10, pady=10)

entry_steps = Entry(janela)
entry_steps.grid(row=1, column=1, padx=10, pady=10)

start_button = Button(janela, text="Simular", command=start_random_walk)
start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()
