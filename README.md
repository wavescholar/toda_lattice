
## Define the Lax Pair $\( L \)$ and $\( B \)$

We begin with the 2-particle Toda lattice. The Lax pair consists of two $\( 2 \times 2 \)$ matrices:

$\( L \)$: symmetric matrix encoding momenta and coupling
$\( B \)$: skew-symmetric matrix defining the flow

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

$\( p_1, p_2 \)$ are the momenta of particles 1 and 2 and
$\( a_1 = e^{(q_2 - q_1)/2} \)$ depends on positions $\( q_1 \)$ and $\( q_2 \)$

The Lax equation is:

$$
\frac{dL}{dt} = [B, L] = BL - LB
$$

This leads to the Toda lattice equations of motion:

$$
\dot{p}_1 = a_1^2, \quad \dot{p}_2 = -a_1^2, \quad \dot{a}_1 = \frac{1}{2}(p_2 - p_1)a_1
$$

---

## Evolve the System via Matrix Exponentials

The Lax equation implies the solution evolves by conjugation:

$$
L(t) = e^{tB} L(0) e^{-tB}
$$

Because $\( B \)$ is skew-symmetric, $\( e^{tB} \)$ is a rotation matrix. Define:

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

The eigenvalues of $\( L(t) \)$ remain constant over time — a hallmark of integrability (isospectral evolution).


## Toda Tau Functions (2-Particle Case)

For the finite Toda lattice, the particle positions can be expressed in terms of **tau functions**. In the case of two particles, we define:

$$
q_i(t) = \log \frac{\tau_{i-1}(t)}{\tau_i(t)}
$$

For the 2-particle system, we have two tau functions $\( \tau_0(t) \)$ and $\( \tau_1(t) \)$, constructed from the eigenvalues and eigenvectors of the initial Lax matrix $\( L(0) \)$. Specifically:

$$
\tau_0(t) = \sum_{k=1}^2 c_k^2 \, e^{\lambda_k t}, \quad
\tau_1(t) = \sum_{k=1}^2 d_k^2 \, e^{\lambda_k t}
$$

Where:
$\( \lambda_k \)$ are the eigenvalues of $\( L(0) \)$

$$
\mathbf{v}_k =
\begin{bmatrix} c_k \\ d_k \end{bmatrix}
$$ 

are the normalized eigenvectors corresponding to $\( \lambda_k \)$

Then the positions evolve as:

$$
q_1(t) = \log \left( \frac{\tau_0(t)}{\tau_1(t)} \right), \quad
q_2(t) = -\log \tau_1(t) + \text{const}
$$

This formulation arises from the **inverse scattering method**, where the full nonlinear dynamics of the Toda lattice are encoded into the spectral data (eigenvalues and eigenvectors) of the Lax matrix.

Tau functions provide an elegant way to reconstruct the solution using only linear algebra and exponential functions.


```
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate
pip install -r requirements.txt
```