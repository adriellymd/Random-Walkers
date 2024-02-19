import numpy as np  # para np.zeros()
import random  # para gerar os range's
import matplotlib.pyplot as plt  # para os gráficos
from matplotlib.animation import FuncAnimation  # para animação
from tkinter import *  # para janela
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # para usar um gráfico dentro do tkinter

def caminhante(num_caminhantes, num_passos):  # tudo é definido com base na quantidade de caminhantes e a quantidade de passos
    if num_caminhantes > 10:  # limitei para 10 caminhantes para sempre rodar direitinho
        raise ValueError("O número de caminhantes não pode exceder 10.")

    n = num_passos  # Quantos passos vamos dar
    x = np.zeros((num_caminhantes, n))  # armazena o valor de x
    y = np.zeros((num_caminhantes, n))  # armazena o valor de y
    fig, ax = plt.subplots()  # desempacotando os valores
    pontos = []

    for i in range(num_caminhantes):
        scatter, = ax.plot([], [], 'ro', color=plt.cm.tab10(i))
        pontos.append(scatter)
    linhas = []
    for i in range(num_caminhantes):
        line, = ax.plot([], [], color=plt.cm.tab10(i))
        linhas.append(line)

    def init():
        ax.set_xlim((-n / 2), (n / 2))
        ax.set_ylim((-n / 2), (n / 2))
        return pontos + linhas

    def update(frame):
        for i in range(num_caminhantes):
            r = random.randint(0, 4)
            if r == 1:
                x[i, frame] = x[i, frame - 1] + 1
                y[i, frame] = y[i, frame - 1]
            elif r == 2:
                x[i, frame] = x[i, frame - 1] - 1
                y[i, frame] = y[i, frame - 1]
            elif r == 3:
                x[i, frame] = x[i, frame - 1]
                y[i, frame] = y[i, frame - 1] + 1
            else:
                x[i, frame] = x[i, frame - 1]
                y[i, frame] = y[i, frame - 1] - 1

            pontos[i].set_data(x[i, :frame + 1], y[i, :frame + 1])
            linhas[i].set_data(x[i, :frame + 1], y[i, :frame + 1])

        return pontos + linhas

    ani = FuncAnimation(fig, update, frames=range(1, n), init_func=init, blit=True)

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    plt.title(f"Caminho aleatório em {n} passos")
    plt.grid()
    print("Carregando...")
    ani.save('random_walk.gif', writer='ffmpeg')

def start_random_walk():
    num_caminhantes = int(spinbox_walkers.get())
    num_passos = int(entry_steps.get())
    caminhante(num_caminhantes, num_passos)

# parte tkinter
janela = Tk()
janela.title("Caminho aleatório 2D")

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
