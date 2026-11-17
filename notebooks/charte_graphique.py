import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb, to_hex, LinearSegmentedColormap

BLEU = "#2B3A67"
ROUGE = "#E6332A"
BLANC = "#FFFFFF"
GRIS = "#F0F0F0"

# Heatmaps signées : -1 en bleu, 0 en blanc, +1 en rouge
CMAP_DIV = LinearSegmentedColormap.from_list("charte_div", [BLEU, BLANC, ROUGE])


def appliquer_charte():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Poppins", "Avenir", "Arial", "DejaVu Sans"],
        "figure.facecolor": BLANC,
        "axes.facecolor": BLANC,
        "savefig.facecolor": BLANC,
        "text.color": BLEU,
        "axes.labelcolor": BLEU,
        "axes.edgecolor": BLEU,
        "xtick.color": BLEU,
        "ytick.color": BLEU,
        "axes.titlecolor": BLEU,
        "axes.titleweight": "semibold",
        "axes.titlesize": 12,
        "axes.linewidth": 1.2,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
    })


def teintes(n, eclaircissement_max=0.75):
    base = np.array(to_rgb(BLEU))
    return [
        to_hex(base + (1 - base) * t)
        for t in np.linspace(0, eclaircissement_max, n)
    ]