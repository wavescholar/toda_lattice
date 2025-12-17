# -*- coding: utf-8 -*-
"""
Concentration of Measure Examples:

*Chebyshev's inequality for i.i.d. Bernoulli sums  
*Hoeffding's inequality for bounded Rademacher sums  
*Sub-Gaussian concentration of \(\ell_2\)-norm of a Gaussian vector  
*Concentration of coordinates on the \(d\)-sphere  
*Chi-square tail vs. Chernoff bound  

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy import stats

# Matplotlib style
plt.rcParams['text.usetex'] = True  # Set to True if you have LaTeX installed
plt.rcParams['figure.figsize'] = (7, 4)

def _format_prob(x, pos=None):
    """Axis formatter for log-probabilities."""
    return f"{x:.1e}"
prob_formatter = FuncFormatter(_format_prob)

def show_plot(title):
    """Common layout tweaks and render."""
    plt.title(title, fontsize=12)
    plt.grid(alpha=0.3)
    plt.xlabel('Deviation $t$')
    plt.ylabel('Tail probability $P(|X-\mu|\ge t)$')
    plt.yscale('log')
    plt.gca().yaxis.set_major_formatter(prob_formatter)
    plt.tight_layout()
    plt.show()

def tail_prob(arr, t_vals, center=0.0):
    """Compute empirical tail probabilities |arr-center| >= t for each t in t_vals."""
    return np.array([(np.abs(arr - center) >= t).mean() for t in t_vals])

# Chebyshev's inequality for Bernoulli sums
"""
Let \(X_1,\dots,X_n \sim \text{Bernoulli}(1/2)\).
Define the sample mean \(\overline{X}=\tfrac1n\sum_{i=1}^n X_i\).

*Chebyshev's Inequality*

\[
\Pr(|\overline{X} - \tfrac12| \ge t) \le \frac{\operatorname{Var}(\overline{X})}{t^2}
          = \frac{1}{4n t^2}.
\]

Below we compare this bound with empirical frequencies.
"""
n = 100          # sample size per experiment
N = 50_000       # number of independent experiments
t_grid = np.linspace(0.02, 0.25, 50)

# Simulations
X = np.random.binomial(1, 0.5, size=(N, n))
means = X.mean(axis=1)

empirical_tail = tail_prob(means, t_grid, 0.5)
chebyshev_tail = 1 / (4 * n * t_grid**2)

plt.figure()
plt.plot(t_grid, empirical_tail, label='Empirical', linewidth=2)
plt.plot(t_grid, chebyshev_tail, linestyle='--', label='Chebyshev bound')
plt.legend()
#show_plot('Chebyshev Inequality - Bernoulli Sample Mean')
plt.savefig("./plots/chebyshev_inequality.png", dpi=300, bbox_inches="tight")
plt.close()

t0 = 0.1
emp_val = (np.abs(means - 0.5) >= t0).mean()
bound_val = 1 / (4 * n * t0**2)
print(f"[Chebyshev] For t={t0}, empirical={emp_val:.3e}, bound={bound_val:.3e}")

# Hoeffding's inequality for Rademacher sums
"""
Let \(\varepsilon_i\) be Rademacher random variables
(\(\Pr(\varepsilon_i=1)=\Pr(\varepsilon_i=-1)=1/2\)).
The sample mean \(S_n=\tfrac1n\sum \varepsilon_i\) satisfies **Hoeffding's inequality**

\[
\Pr(|S_n| \ge t) \le 2\exp(-2 n t^2).
\]
"""

n = 100
N = 50_000
t_grid = np.linspace(0.02, 0.5, 60)

Eps = np.random.choice([-1, 1], size=(N, n))
S = Eps.mean(axis=1)

emp_tail = tail_prob(S, t_grid, 0.0)
hoeff_tail = 2 * np.exp(-2 * n * t_grid**2)

plt.figure()
plt.plot(t_grid, emp_tail, label='Empirical', linewidth=2)
plt.plot(t_grid, hoeff_tail, '--', label='Hoeffding bound')
plt.legend()
plt.savefig("./plots/hoeffding_ineq.png", dpi=300, bbox_inches="tight")
#show_plot('Hoeffding Inequality - Rademacher Sample Mean')
print(f"[Hoeffding] Median of |S_n|: {np.median(np.abs(S)):.3e}")
plt.close()

# Concentration of \ell_2-norm of a Gaussian vector
"""
For \(g \sim \mathcal{N}(0,I_d)\), the squared norm \(\|g\|_2^2\) has
\(\chi^2_d\) distribution with mean \(d\) and variance \(2d\).
A 1-Lipschitz function of a Gaussian vector is sub-Gaussian:

\[
\Pr\big(|\|g\|_2 - \sqrt{d}| \ge t\big) \le 2\exp(-t^2/2).
\]
"""

d = 500
N = 40_000
g = np.random.randn(N, d)
norms = np.linalg.norm(g, axis=1)
center = np.sqrt(d)

t_grid = np.linspace(0.05, 5.0, 80)
emp_tail = tail_prob(norms, center + t_grid, center)  # deviations from center
gauss_tail = 2 * np.exp(-t_grid**2 / 2)

plt.figure()
plt.plot(t_grid, emp_tail, label='Empirical', linewidth=2)
plt.plot(t_grid, gauss_tail, '--', label='Gaussian Lipschitz bound')
plt.legend()
#show_plot(f'Gaussian Norm Concentration (d={d})')
print(f"[Gaussian] Mean norm: {norms.mean():.3f}, sqrt(d): {center:.3f}")
plt.savefig("./plots/gaussian_norm_concentraion.png", dpi=300, bbox_inches="tight")
plt.close()



# Coordinate concentration on the unit sphere
"""
Draw \(X\) uniform on the unit sphere \(S^{d-1}\).
For large \(d\), a single coordinate \(X_1\) behaves approximately as
\(\mathcal{N}(0, 1/d)\) (Poincaré lemma).
We verify this numerically and inspect radius concentration.
"""

def sample_sphere(n_samples, d):
    x = np.random.randn(n_samples, d)
    x /= np.linalg.norm(x, axis=1, keepdims=True)
    return x

d = 10
N = 100_000
X = sample_sphere(N, d)
coord = X[:, 0]              # first coordinate
radius = np.linalg.norm(X, axis=1)

# Coordinate histogram
plt.figure()
plt.hist(np.sqrt(d)*coord, bins=60, density=True, alpha=0.7)
xs = np.linspace(-4, 4, 400)
plt.plot(xs, stats.norm.pdf(xs), linewidth=2)
plt.title(r'First coordinate $\sqrt{d}\,X_1$ vs $\mathcal{N}(0,1)$')
plt.xlabel(r'$\sqrt{d}\,X_1$')
plt.ylabel('Density')
plt.grid(alpha=0.3)
plt.tight_layout()
#plt.show()
plt.savefig("./plots/first_coord.png", dpi=300, bbox_inches="tight")
plt.close()


# Radius histogram
plt.figure()
radii = np.linalg.norm(np.random.randn(N, d), axis=1) / np.sqrt(d)

plt.figure()
plt.hist(radii, bins=50, density=True, alpha=0.7)
plt.axvline(1, linestyle="--", color="k")
plt.title("Radius of a d-dimensional Gaussian / $\sqrt{d}$")
plt.xlabel(r"$\|g\|_2 / \sqrt{d}$")
plt.ylabel("Density")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("./plots/relative_deviationradius_of_pts_Sn.png", dpi=300, bbox_inches="tight")
plt.close()

# Chernoff bound for \chi^2 tails
"""
For \(Z \sim \chi^2_d\) and \(\lambda > 0\),

\[
\Pr(Z \ge (1+\delta)d) \le \exp\Big(-\tfrac\delta2 d + (1+\delta)\tfrac d2\ln(1+\delta)\Big).
\]
"""

d = 20
N = 100_000
Z = np.random.chisquare(d, size=N)

delta_grid = np.linspace(0.1, 3.0, 40)
emp_tail = np.array([(Z >= (1 + delta) * d).mean() for delta in delta_grid])
chernoff_tail = np.exp(-0.5 * delta_grid * d + 0.5 * (1 + delta_grid) * d * np.log1p(delta_grid))

plt.figure()
plt.plot(delta_grid, emp_tail, label='Empirical', linewidth=2)
plt.plot(delta_grid, chernoff_tail, '--', label='Chernoff bound')
plt.legend()
plt.yscale('log')
plt.xlabel(r'Relative deviation $\delta$')
plt.ylabel(r'$\Pr(Z \ge (1+\delta)d)$')
plt.grid(alpha=0.3)
plt.tight_layout()
#plt.show()
plt.savefig("./plots/relative_deviation.png", dpi=300, bbox_inches="tight")
plt.close()

print("Replace Bernoulli(1/2) with p=0.1 and study Bernstein's inequality.")
print("Explore concentration for sub-exponential variables.")
print("Investigate Talagrand's inequality for product measures.")
