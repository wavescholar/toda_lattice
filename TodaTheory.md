% The Toda Lattice and Its Lax Pair
% August 2025
% Bruce Campbell & ChatGPT 

# Introduction

The Toda lattice is a famous integrable system in mathematical physics. It describes a one-dimensional chain of particles with nonlinear, exponential interactions between nearest neighbors. Its integrability and rich structure make it a central model in soliton theory, spectral analysis, and Hamiltonian mechanics.

In this note, we derive the Lax pair formulation of the Toda lattice, exploring how it was originally discovered. Along the way, we address key theoretical insights, dispel the notion that it was a product of trial and error, and show how the reformulation reveals the hidden linearity in a nonlinear system.



# The Classical Toda Lattice

## Hamiltonian Formulation

The Toda lattice with $N$ particles has the Hamiltonian:

$$ H = \sum_{i=1}^N \left( \frac{1}{2} p_i^2 + a e^{-(q_{i+1} - q_i)} \right) $$ 

where:

- $q_i$: position of the $i$-th particle,
- $p_i$: momentum of the $i$-th particle,
- $a$: interaction strength (often normalized to 1).

## Equations of Motion

From Hamilton's equations:

$$ \dot{q}_i = p_i $$
$$ \dot{p}_i = a \left( e^{-(q_i - q_{i-1})} - e^{-(q_{i+1} - q_i)} \right) $$

These are second-order nonlinear ODEs. While not linear, the structure hints at something special due to the form of the exponential interactions.



# From Nonlinear to Linear: The Need for a New Formulation

## Motivation

The Toda lattice exhibits soliton-like behavior and regular wave patterns, suggesting it may be integrable. In the late 1960s and early 1970s, Peter Lax introduced the idea of expressing nonlinear PDEs and ODEs as isospectral matrix flows:

$$ \frac{dL}{dt} = [B, L] $$ 

This Lax equation implies that the eigenvalues of $L$ are constants of motion — a signal of integrability. The question became: can we cast the Toda lattice in this form?



# Flaschka’s Change of Variables

The breakthrough came in **1974**, when **H. Flaschka** introduced a clever reparameterization to simplify the Toda equations and reveal their underlying linear algebraic structure.

Define new variables:

$$ a_i := \frac{1}{2} e^{-\frac{1}{2}(q_{i+1} - q_i)}, \quad b_i := -\frac{1}{2} p_i $$ 

This change turns the second-order nonlinear equations into a first-order, bilinear system:

$$ \dot{a}_i = a_i (b_{i+1} - b_i) \tag{1} $$
$$ \dot{b}_i = 2(a_i^2 - a_{i-1}^2) \tag{2} $$



# Why This Form is Significant

> *"These are now first-order, bilinear, and resemble commutator forms — perfect setup for matrix equations."*

### First-order

Equations (1) and (2) are first-order in time, which makes them compatible with matrix evolution equations of the form $\dot{L} = [B, L]$.

### Bilinear

Equation (1) is bilinear:

$$ \dot{a}_i = a_i (b_{i+1} - b_i) $$ 

Equation (2) is quadratic:

$$ \dot{b}_i = 2(a_i^2 - a_{i-1}^2) $$ 

These forms suggest a hidden matrix product structure.

### Commutator-Like

The differences $b_{i+1} - b_i$ and $a_i^2 - a_{i-1}^2$ are typical of commutators in tridiagonal matrices — a sign that the Toda lattice might be representable by a Lax pair.



# Constructing the Lax Pair

## The Lax Matrix $L$

Define a symmetric, tridiagonal matrix:

$$ L = \begin{bmatrix} b_1 & a_1 & 0 & \cdots & 0 \\ a_1 & b_2 & a_2 & \ddots & \vdots \\ 0 & a_2 & b_3 & \ddots & 0 \\ \vdots & \ddots & \ddots & \ddots & a_{N-1} \\ 0 & \cdots & 0 & a_{N-1} & b_N \end{bmatrix} $$ 

## The Skew-Symmetric Matrix $B$

Define:

$$ B = \begin{bmatrix} 0 & a_1 & 0 & \cdots & 0 \\ -a_1 & 0 & a_2 & \ddots & \vdots \\ 0 & -a_2 & 0 & \ddots & 0 \\ \vdots & \ddots & \ddots & \ddots & a_{N-1} \\ 0 & \cdots & 0 & -a_{N-1} & 0 \end{bmatrix} $$ 



# Verifying the Lax Equation

Compute:

$$ \dot{L} = [B, L] = BL - LB $$ 

## Diagonal Entries

From matrix multiplication:

$$ (\dot{L})_{ii} = 2(a_i^2 - a_{i-1}^2) = \dot{b}_i $$ 

## Off-Diagonal Entries

For $i \neq j$, particularly $i, i+1$:

$$ (\dot{L})_{i,i+1} = a_i (b_{i+1} - b_i) = \dot{a}_i $$ 

This confirms:

$$ \dot{L} = [B, L] \Longleftrightarrow \begin{cases} \dot{a}_i = a_i (b_{i+1} - b_i) \\ \dot{b}_i = 2(a_i^2 - a_{i-1}^2) \end{cases} $$ 



# Insights Behind the Derivation

You asked:

> Was it trial and error or was there theory driving the solution?

### Theoretical Motivation

- Lax's 1968 theory of isospectral flows
- Spectral theory of Jacobi matrices
- Hamiltonian structure and conservation laws
- The algebraic pattern in Flaschka’s equations

### Creative Guesses

- Exact substitution to define $a_i$
- Form of the skew-symmetric matrix $B$
- Choosing a matrix framework aligned with nearest-neighbor interactions

So: theory-driven, but with insightful experimentation.



# Consequences of the Lax Pair

- The Toda lattice is completely integrable
- The eigenvalues of $L$ are conserved
- The solution can be obtained via the inverse scattering transform
- The model generalizes to:
  - Quantum Toda systems
  - Lie algebraic Toda chains
  - Toda field theories



# Example: The 2-Particle Toda Lattice

To make the abstract formulation concrete, let's examine the simplest non-trivial case: a Toda lattice with two particles. This example illustrates how the Lax pair formulation works in practice and connects back to the physical variables.

## Define the Lax Pair $L$ and $B$

We begin with the 2-particle Toda lattice. The Lax pair consists of two $2 \times 2$ matrices.

$L$: A symmetric matrix encoding the momenta and particle interaction.
$B$: A skew-symmetric matrix defining the temporal evolution of the system.

The matrices are defined as:

$$ 
L = \begin{bmatrix}
 p_1 & a_1 \\ a_1 & p_2
\end{bmatrix}, 
 \quad
B = \begin{bmatrix}
 0 & -a_1/2 \\ a_1/2 & 0
\end{bmatrix}
$$ 

Where:

- $p_1, p_2$ are the momenta of particles 1 and 2.
- $a_1 = e^{-(q_2 - q_1)/2}$ is the interaction term, which depends on the particle positions $q_1$ and $q_2$. Note the negative sign in the exponent, which is consistent with the Hamiltonian defined earlier.

The dynamics are governed by the **Lax equation**:

$$ 
\frac{dL}{dt} = [B, L] = BL - LB
$$ 

Computing this commutator yields the Toda lattice equations of motion:

$$ 
\dot{p}_1 = -a_1^2, \quad \dot{p}_2 = a_1^2, \quad \dot{a}_1 = \frac{1}{2}(p_1 - p_2)a_1
$$ 

This formulation uses the physical variables $p_i$ directly in the Lax matrix $L$, which is a different (but equivalent) approach to Flaschka's variables, where $L$ contains $b_i = -p_i/2$.

---


## Evolve the System via Matrix Exponentials

The solution to the Lax equation evolves by a unitary conjugation (since B is skew-symmetric):

$$ 
L(t) = e^{tB} L(0) e^{-tB}
$$ 

Because $B$ is skew-symmetric, $e^{tB}$ is an orthogonal matrix representing a rotation. Let's define the generator of rotations in 2D:

$$ 
J = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
$$ 

Then $B$ can be written as:

$$ 
B = \frac{a_1}{2} J
$$ 

The matrix exponential is then:

$$ 
e^{tB} = \cos(a_1 t/2) I + \sin(a_1 t/2) J
=\begin{bmatrix}
\cos(a_1 t/2) & -\sin(a_1 t/2) \\
\sin(a_1 t/2) & \cos(a_1 t/2)
\end{bmatrix}
$$ 

The time-evolved Lax matrix $L(t)$ is found by applying this rotation to the initial matrix $L(0)$. A key consequence is that the eigenvalues of $L(t)$ remain constant over time. This property, known as **isospectral evolution**, is a hallmark of integrability.


## Toda Tau Functions (2-Particle Case)

For the finite Toda lattice, the particle positions can be expressed in terms of **tau functions**. In the case of two particles, we define:

$$ 
_i(t) = \log \frac{\tau_{i-1}(t)}{\tau_i(t)}
$$ 

For the 2-particle system, we have two tau functions $\tau_0(t)$ and $\tau_1(t)$, constructed from the eigenvalues and eigenvectors of the initial Lax matrix $L(0)$. Specifically:

$$ 
\tau_0(t) = \sum_{k=1}^2 c_k^2 \, e^{\lambda_k t}, \quad
\tau_1(t) = \sum_{k=1}^2 d_k^2 \, e^{\lambda_k t}
$$ 

Where:
- $\lambda_k$ are the eigenvalues of $L(0)$.
- $\mathbf{v}_k = \begin{bmatrix} c_k \\ d_k \end{bmatrix}$ are the normalized eigenvectors corresponding to $\lambda_k$.

Then the positions evolve as:

$$ 
 q_1(t) = \log \left( \frac{\tau_0(t)}{\tau_1(t)} \right), \quad
 q_2(t) = -\log \tau_1(t) + \text{const}
$$ 

This formulation arises from the **inverse scattering method**, where the full nonlinear dynamics of the Toda lattice are encoded into the spectral data (eigenvalues and eigenvectors) of the Lax matrix. Tau functions provide an elegant way to reconstruct the solution using only linear algebra and exponential functions.

# Conclusion

The discovery of the Lax pair for the Toda lattice reveals a profound insight: many nonlinear systems harbor linear, algebraic structures when recast properly. Flaschka’s transformation and the resulting Lax equation show how spectral methods and matrix theory can unlock hidden symmetries and conservation laws in nonlinear dynamics.



# Appendix: Computing the Commutator $[B, L]$

Let’s verify that $\dot{L} = [B, L]$ gives the Flaschka equations.

Let $L$ and $B$ be as defined above.

## Diagonal Entries $i = j$

$$ (\dot{L})_{ii} = \sum_k B_{ik} L_{ki} - L_{ik} B_{ki} $$ 

Only terms with $k = i-1, i+1$ contribute. Explicitly:

$$ (\dot{L})_{ii} = B_{i,i+1} L_{i+1,i} + B_{i,i-1} L_{i-1,i} - L_{i,i+1} B_{i+1,i} - L_{i,i-1} B_{i-1,i} $$ 

Plug in values:

$$ 
\begin{aligned} \\ &= a_i a_i - a_{i-1} a_{i-1} + a_i a_i - a_{i-1} a_{i-1} \\ &= 2(a_i^2 - a_{i-1}^2) \\ &= \dot{b}_i \\ \end{aligned} $$ 

## Off-Diagonal Entries $i, i+1$

$$ (\dot{L})_{i,i+1} = \sum_k B_{ik} L_{k,i+1} - L_{ik} B_{k,i+1} $$ 

Only nonzero terms involve $k = i$ and $k = i+1$:

$$ = B_{i,i} L_{i,i+1} + B_{i,i+1} L_{i+1,i+1} - L_{i,i} B_{i,i+1} - L_{i,i+1} B_{i+1,i+1} $$ 

Simplifies to:

$$ 
\begin{aligned} \\ &= a_i b_{i+1} - b_i a_i = a_i(b_{i+1} - b_i) \\ &= \dot{a}_i \\ \end{aligned} $$ 

The commutator indeed reproduces the Toda lattice dynamics in Flaschka variables.