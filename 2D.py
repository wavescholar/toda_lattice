import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

# Initial conditions
p1 = 1.0
p2 = -1.0
q1 = 0.0
q2 = 1.0

# Compute coupling a1
a1 = np.exp((q2 - q1) / 2)

# Lax matrix and B matrix
L0 = np.array([[p1, a1],
               [a1, p2]])

B = np.array([[0, -a1],
              [a1, 0]])

# Time grid
t_vals = np.linspace(0, 10, 500)

# Storage for matrix entries and eigenvalues
L11, L12, L22 = [], [], []
eig1, eig2 = [], []

# Loop over time and compute L(t)
for t in t_vals:
    expBt = expm(t * B)
    exp_minusBt = expm(-t * B)
    Lt = expBt @ L0 @ exp_minusBt

    L11.append(Lt[0, 0])
    L12.append(Lt[0, 1])
    L22.append(Lt[1, 1])

    eigs = np.linalg.eigvals(Lt)
    eig1.append(np.max(eigs))  # max/min to keep ordering consistent
    eig2.append(np.min(eigs))

# Plot matrix entries
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t_vals, L11, label="L[0,0] (p1)", lw=2)
plt.plot(t_vals, L12, label="L[0,1] (a1)", lw=2)
plt.plot(t_vals, L22, label="L[1,1] (p2)", lw=2)
plt.title("Lax Matrix Entries Over Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

# Plot eigenvalues
plt.subplot(1, 2, 2)
plt.plot(t_vals, eig1, label="Eigenvalue 1", lw=2)
plt.plot(t_vals, eig2, label="Eigenvalue 2", lw=2)
plt.title("Eigenvalues of L(t) Over Time")
plt.xlabel("Time")
plt.ylabel("Eigenvalue")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print("Lax matrix entries and eigenvalues computed and plotted successfully.")
# This code computes the time evolution of the Lax matrix and its eigenvalues
# and visualizes them using matplotlib. The Lax matrix is defined by the initial conditions
# and the coupling parameter, and the eigenvalues are computed at each time step.
# The plots show how the matrix entries and eigenvalues change over time.
# Note: Ensure you have the required libraries installed:
# pip install numpy scipy matplotlib

