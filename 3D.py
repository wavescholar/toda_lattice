import numpy as np
from scipy.linalg import expm, eigvals
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Initial conditions
p = np.array([1.0, 0.0, -1.0])
q = np.array([0.0, 1.0, 2.0])
a = np.exp(0.5 * (q[1:] - q[:-1]))  # a1, a2

# Construct initial Lax matrix L0 (symmetric tridiagonal)
L0 = np.zeros((3, 3))
np.fill_diagonal(L0, p)
L0[0, 1] = L0[1, 0] = a[0]
L0[1, 2] = L0[2, 1] = a[1]

# Construct B matrix (skew-symmetric tridiagonal)
B = np.zeros((3, 3))
B[0, 1] = -a[0]
B[1, 0] = a[0]
B[1, 2] = -a[1]
B[2, 1] = a[1]

# Time grid
t_vals = np.linspace(0, 10, 300)

# Store positions for each particle (we’ll extract from diagonalized L later)
positions = np.zeros((3, len(t_vals)))

for i, t in enumerate(t_vals):
    expBt = expm(t * B)
    exp_minusBt = expm(-t * B)
    Lt = expBt @ L0 @ exp_minusBt

    # Approximate positions by using a mock inverse map (for illustration only)
    # In a real integrable system solver, q(t) is found via inverse scattering or tau functions.
    # Here, we track momenta as proxy for motion.
    positions[0, i] = Lt[0, 0]
    positions[1, i] = Lt[1, 1]
    positions[2, i] = Lt[2, 2]

# Set up the 3D animation
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
lines = [ax.plot([], [], [], 'o-', lw=2)[0] for _ in range(3)]
colors = ['red', 'green', 'blue']

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 2)
    ax.set_zlim(0, 3)
    ax.set_xlabel("Time")
    ax.set_ylabel("Momentum (proxy)")
    ax.set_zlabel("Particle Index")
    return lines

def update(frame):
    t = t_vals[frame]
    for i, line in enumerate(lines):
        x = t_vals[:frame]
        y = positions[i, :frame]
        z = np.full_like(x, i)  # particle index as z
        line.set_data(x, y)
        line.set_3d_properties(z)
        line.set_color(colors[i])
    return lines

ani = FuncAnimation(fig, update, frames=len(t_vals), init_func=init,
                    blit=False, interval=30)

plt.title("3-Particle Toda Lattice – 3D Animation")
plt.tight_layout()
plt.show()
