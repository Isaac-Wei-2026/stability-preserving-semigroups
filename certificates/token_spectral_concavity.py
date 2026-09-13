"""Numerical diagnostic (not a proof); Python 3 + NumPy."""
from itertools import combinations
import numpy as np
rng = np.random.default_rng(20260913)
for n in range(2, 9):
    for trial in range(10):
        W = np.triu(rng.integers(0, 8, (n, n)), 1); W = W + W.T
        for a in np.linspace(-1, 1, 9):
            lam = []
            for k in range(n + 1):
                states = list(combinations(range(n), k)); index = {s: i for i, s in enumerate(states)}
                A = np.zeros((len(states), len(states)))
                for i, S in enumerate(states):
                    for u in S:
                        for v in set(range(n)) - set(S):
                            A[i, index[tuple(sorted((set(S) - {u}) | {v}))]] = W[u, v]
                lam.append(np.linalg.eigvalsh(A + a * np.diag(A.sum(axis=1)))[-1])
            tol = 1e-10 * max(1., max(np.abs(lam)))
            assert max(np.diff(lam, 2), default=-np.inf) <= tol and np.allclose(lam, lam[::-1], rtol=0, atol=tol)
print("PASS: 630 weighted graph/parameter cases; numerical checks only.")
