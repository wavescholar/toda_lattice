import numpy as np
import matplotlib.pyplot as plt

# Initial values
p1 = 1.0
p2 = -1.0
q1_0 = 0.0
q2_0 = 1.0

# Compute initial coupling
a1 = np.exp((q2_0 - q1_0) / 2)

# Define initial Lax matrix
L0 = np.array([
    [p1, a1],
    [a1, p2]
])

# Eigendecomposition of L0
eigenvals, eigenvecs = np.linalg.eigh(L0)  # eigenvectors are orthonormal
l1, l2 = eigenvals
v1, v2 = eigenvecs[:, 0], eigenvecs[:, 1]

# Extract components
c1, d1 = v1[0], v1[1]
c2, d2 = v2[0], v2[1]

# Time grid
t_vals = np.linspace(0, 10, 500)

# Tau functions
tau_0 = c1**2 * np.exp(l1 * t_vals) + c2**2 * np.exp(l2 * t_vals)
tau_1 = d1**2 * np.exp(l1 * t_vals) + d2**2 * np.exp(l2 * t_vals)

# Positions q1(t), q2(t)
q1_t = np.log(tau_0 / tau_1)
q2_t = -np.log(tau_1)  # up to an additive constant

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t_vals, q1_t, label="$q_1(t)$", lw=2)
plt.plot(t_vals, q2_t, label="$q_2(t)$", lw=2)
plt.title("2-Particle Toda Lattice Positions via Tau Functions")
plt.xlabel("Time $t$")
plt.ylabel("Position $q_i(t)$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
