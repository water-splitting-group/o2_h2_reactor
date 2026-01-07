import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
#
# ----------------------------------------
# Font settings of Water Splitting Group
# ----------------------------------------
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['font.size'] = 12 
rcParams['mathtext.fontset'] = 'custom'
rcParams['mathtext.rm'] = 'Arial'
rcParams['mathtext.it'] = 'Arial:italic'
rcParams['mathtext.bf'] = 'Arial:bold'

# ================= USER OPTION =================
plot_theoretical_line = True   # Set to False to hide the theoretical prediction
# ===============================================

# ---- Read the first file ----
df1 = pd.read_csv(
    "GC_vs_theor_H2.txt",
    sep="\t",
    decimal=",",
    header=None,
    names=["X", "GC"]
)

# ---- Read the second file ----
df2 = pd.read_csv(
    "Unisense_vs_theor_H2.txt",
    sep="\t",
    decimal=",",
    header=None,
    names=["X", "Unisense"]
)

# ---- Optional check: ensure X axes match ----
if not df1["X"].equals(df2["X"]):
    raise ValueError("X axes in the two files do not match")

# ---- Plot ----
plt.figure()

# --- Theoretical prediction (plotted FIRST) ---
if plot_theoretical_line:
    x_theor = np.linspace(0, 1, 200)
    y_theor = x_theor  # y = x (through origin)

    plt.plot(
        x_theor,
        y_theor,
        linestyle="--",
        color="grey",
        linewidth=2,
        zorder=0
    )

# --- Experimental curves ---
plt.plot(df1["X"], df1["GC"], marker="o", label="Gas chromatography", zorder=2)
plt.plot(df2["X"], df2["Unisense"], marker="s", label="Unisense sensor", zorder=2)

plt.xlabel("Theoretical value, vol%")
plt.ylabel("Experimental value, vol%")
plt.title("Gas phase measurements")
plt.legend()
plt.grid(True)

# --- Force axes to start at zero ---
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.show()