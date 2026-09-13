# Token-graph spectral concavity: numerical illustration

`token_spectral_concavity.py` is a 20-line numerical diagnostic for the token-graph theorem in *Generators of stability-preserving semigroups, spectral gaps, and classical ground-state computation* and its self-contained sector-growth excerpt.

It constructs token adjacency and weighted-degree matrices on 70 pseudorandom graphs (10 for each vertex count from 2 through 8), using integer edge weights from 0 through 7 and seed 20260913. For each graph it checks the largest-eigenvalue concavity and complementation symmetry of `A_k + a D_k` at nine equally spaced parameters in `[-1, 1]`, for 630 graph/parameter cases in total.

Run with Python 3 and NumPy, with assertions enabled:

```sh
python3 token_spectral_concavity.py
```

The expected output is `PASS: 630 weighted graph/parameter cases; numerical checks only.` The tolerance is `1e-10` times the larger of 1 and the maximum absolute sector eigenvalue. These floating-point checks are an illustration, not a proof or an exact certificate. They do not verify the general nonsymmetric sector-growth theorem. The mathematical proof is in the excerpt and the full manuscript, DOI [10.5281/zenodo.22733335](https://doi.org/10.5281/zenodo.22733335).

The existing two rational EPR certificates, their checksums, and `epr-certificates.zip` are separate and unchanged.
