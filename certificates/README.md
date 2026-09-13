# Exact certificates for the six-vertex EPR counterexample

Supplement to *Generators of stability-preserving semigroups, spectral gaps, and classical ground-state computation*, by Dongsheng Wei, Appendix C, Theorem C.1.

The appendix gives the rational matrix, trial-vector data, and error estimates. These programs verify the finite rational assertions supporting a zero of the **exact** ground-state polynomial strictly inside the proposed radius at deformation parameter `s = 1/2` on the unweighted tree with edges `01, 02, 03, 14, 15`.

## Files and coverage

- [epr_six_vertex_certificate.py](epr_six_vertex_certificate.py) constructs the full 64-dimensional rational matrix, verifies charge preservation and inertia by exact elimination, bounds the trial-vector residual, and verifies the zero inequalities used in the proof.
- [epr_independent_certificate.py](epr_independent_certificate.py) provides a second verification using the reduced representation and rational error bounds. Its printed floating-point diagnostics are not used by the exact assertions.
- `SHA256SUMS` records the script hashes for checking the downloaded files.

These are certificates for Theorem C.1. They do not constitute executable verification of the other theorems in the manuscript. The mathematical passage from the rational bounds to a zero of the exact ground state is proved in Appendix C.

## Run

Python 3.10 or later with its standard library is sufficient (the full-space script uses `int.bit_count`). No packages, numerical eigensolver, network access, or input files are required.

Run both programs from the extracted directory:

```sh
python3 epr_six_vertex_certificate.py
python3 epr_independent_certificate.py
```

Both should finish with exit status zero and their success messages. Keep Python assertions enabled: run the commands as written, without `-O` or `-OO` and without setting `PYTHONOPTIMIZE`.

The two script files are unchanged from repository commit `593275b4834f3d58e2fecbc9257fc43a5bf20e77`, the fixed version cited in the manuscript's Data and code availability statement. This supplementary package adds execution instructions and checksums.

The repository's `epr-certificates.zip` contains these instructions, both scripts, and `SHA256SUMS` for use as a journal supplementary file. No Zenodo DOI has been assigned.

Contact: Dongsheng Wei, dongshengwei2025@icloud.com.
