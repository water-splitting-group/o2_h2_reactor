import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from matplotlib import rcParams
from matplotlib.patches import Rectangle
import math as math

# Setting font properties
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['font.size'] =12

np.set_printoptions(suppress=True)

class BET_Spectrum:

    def __init__(self, name, delimiter='	'):
        self.name = name
        self.data_exp = np.loadtxt(name, delimiter=delimiter)

    def pick_peaks(self, height, prominence):
        peaks, _ = find_peaks(self.data_exp[:, 1], height=height, prominence=prominence)
        self.peaks = self.data_exp[peaks]

    def plot_experimental(self, ax, label='Experimental', linestyle='-', color=(0, 0.3294, 0.6235)):
        ax.set_xlabel('Relative pressure [P/P$_{0}$]')
        ax.set_ylabel('Quantity Adsorbed [cm$^{3}$/g]')
        ax.plot(self.data_exp[:, 0], self.data_exp[:, 1], color=color, linewidth=0.7, linestyle=linestyle, label=label)
        ax.legend(loc='upper left')

    def plot_all_points(self, ax, color='black'):
        ax.scatter(self.data_exp[:, 0], self.data_exp[:, 1], color=color, zorder=5, marker='o', s=50)
        
def add_simple_box_with_text(ax, x, y, width, height, text,
                             facecolor='honeydew', edgecolor='grey', textcolor='black', alpha=0.5):
    rect=Rectangle((x, y), width, height, linewidth=1, edgecolor=edgecolor, facecolor=facecolor, alpha=alpha, zorder=10)
    ax.add_patch(rect)
    cx= x + 0.01
    cy= y + height/2
    ax.text(cx, cy, text, ha='left', va='center', fontsize=15, color=textcolor, zorder=11, linespacing=1.5, wrap=True)

def plot_overlayed_BET():
    fig, ax = plt.subplots(figsize=(9, 5))
    fig.subplots_adjust(bottom=0.12, top=0.95, left=0.1, right=0.98)

    # Plotting the 1-ads BET spectrum with a solid line
    BET_spectrum1 = BET_Spectrum('20251204_EA_402_NB_352_BET _N2_77_K-ads.csv', delimiter=',')
    BET_spectrum1.plot_experimental(ax=ax, color='indigo', linestyle='-', label='Rh$_{2-y}$Cr$_y$O$_3$/Al:SrTiO$_3$-ads')
    BET_spectrum1.plot_all_points(ax=ax, color='indigo')

    # Plotting the 1-des BET spectrum with a dashed line
    BET_spectrum2 = BET_Spectrum('20251204_EA_402_NB_352_BET _N2_77_K-des.csv', delimiter=',')
    BET_spectrum2.plot_experimental(ax=ax, color='darkorchid', linestyle='--', label='Rh$_{2-y}$Cr$_y$O$_3$/Al:SrTiO$_3$-des')
    BET_spectrum2.plot_all_points(ax=ax, color='darkorchid')

    # Setting the x and y limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 6)

    info_box_text = "Rh$_{2-y}$Cr$_y$O$_3$/Al:SrTiO$_3$ Surface area = 3.273 m$^2$/g"
    add_simple_box_with_text(ax, 0.05, 3.5, 0.62, 1.0, info_box_text, facecolor='pink')

    # Saving the figure
    fig.savefig('EA-402-BET-Poster.pdf')
    
    plt.show()

if __name__ == '__main__':
    plot_overlayed_BET()
