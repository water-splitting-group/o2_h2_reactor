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

# ---- Read data ----

df_uni = pd.read_csv(
    "H2_gas_phase_calibration.txt",
    sep="\t",
    decimal=",",
    header=None,
    names=["X", "Y"]
)

x = df_uni["X"].values
y_uni = df_uni["Y"].values


# ---- Linear fits ----

# Unisense fit
coef_uni = np.polyfit(x, y_uni, 1)
fit_uni = np.poly1d(coef_uni)

# ---- R^2 calculation ----
def r_squared(y, y_fit):
    ss_res = np.sum((y - y_fit) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    return 1 - ss_res / ss_tot

r2_uni = r_squared(y_uni, fit_uni(x))

# ---- Plot ----
plt.figure()

plt.scatter(x, y_uni, label="Calibration points")
plt.plot(x, fit_uni(x),
         label=f" y = {coef_uni[0]:.3f}x + {coef_uni[1]:.3f}\nR² = {r2_uni:.4f}")

plt.xlabel("H$_2$ concentration, vol%")
plt.ylabel("Sensor signal, mV")
plt.title("Gas phase calibration")
plt.legend()
plt.grid(True)

plt.show()
