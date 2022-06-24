import matplotlib.pyplot as plt
import numpy as np
import io
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QApplication
def add_figure_to_clipboard(event):
    if event.key == "ctrl+c":
       with io.BytesIO() as buffer:
            fig.savefig(buffer)
            QApplication.clipboard().setImage(QImage.fromData(buffer.getvalue()))

if 'fig' not in locals():
    fig = plt.figure()
    fig.set_size_inches(5,3)
    fig.canvas.mpl_connect('key_press_event', add_figure_to_clipboard)
    fig.tight_layout()
    ax = fig.add_subplot(111)
    
n_t = 1000
t_range = (0, 3)
t = np.linspace(t_range[0], t_range[1], n_t)
f = 1
sig = np.sin(2 * np.pi * f * t)

ax.cla()
noise = np.random.
ax.plot(t, sig, linewidth=3, color='blue',label='Input')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude')
ax.set_xlim(0,3)
ax.set_ylim(-2,2)
ax.grid()
ax.legend()
