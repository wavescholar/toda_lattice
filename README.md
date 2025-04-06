
## 🔹 Step 1: Define the Lax Pair \( L \) and \( B \)

We begin with the 2-particle Toda lattice. The Lax pair consists of two \( 2 \times 2 \) matrices:

- \( L \): symmetric matrix encoding momenta and coupling
- \( B \): skew-symmetric matrix defining the flow

The matrices are:

$$
L = \begin{bmatrix}
p_1 & a_1 \\
a_1 & p_2
\end{bmatrix},
\quad
B = \begin{bmatrix}
0 & -a_1 \\
a_1 & 0
\end{bmatrix}
$$

Where:

- \( p_1, p_2 \) are the momenta of particles 1 and 2
- \( a_1 = e^{(q_2 - q_1)/2} \) depends on positions \( q_1 \) and \( q_2 \)

The Lax equation is:

$$
\frac{dL}{dt} = [B, L] = BL - LB
$$

This leads to the Toda lattice equations of motion:

$$
\dot{p}_1 = a_1^2, \quad \dot{p}_2 = -a_1^2, \quad \dot{a}_1 = \frac{1}{2}(p_2 - p_1)a_1
$$

---

## 🔹 Step 2: Evolve the System via Matrix Exponentials

The Lax equation implies the solution evolves by conjugation:

$$
L(t) = e^{tB} L(0) e^{-tB}
$$

Because \( B \) is skew-symmetric, \( e^{tB} \) is a rotation matrix. Define:

$$
J = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}, \quad B = a_1 J
$$

Then:

$$
e^{tB} = \cos(a_1 t) I + \sin(a_1 t) J
= \begin{bmatrix}
\cos(a_1 t) & -\sin(a_1 t) \\
\sin(a_1 t) & \cos(a_1 t)
\end{bmatrix}
$$

So the time-evolved Lax matrix is:

$$
L(t) = e^{tB} L(0) e^{-tB}
$$

The eigenvalues of \( L(t) \) remain constant over time — a hallmark of integrability (isospectral evolution).



```
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate
pip install -r requirements.txt
```