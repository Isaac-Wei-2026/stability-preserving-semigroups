# Stability-preserving semigroups

**Dongsheng Wei** · Independent Researcher

Contact: dongshengwei2025@icloud.com

The original comprehensive manuscript has been reorganized into three companion papers. Each paper has a matching PDF and self-contained LaTeX source.

## 1. Generators of stability-preserving semigroups, spectral gaps, and classical ground-state computation

Finite-box generator classification and exact local-input recognition, strict spectral control, and classical ground-state computation, with Hamiltonian and token-graph applications. The full Gibbs-tensor Hamiltonian converse and strict positive-field radius theorem answer two questions posed in [Wong, Bravyi, Gosset, and Liu (2026), Sections 6 and 5.3](https://arxiv.org/html/2602.03605v1).

**69 pages** · [PDF](Generators%20of%20stability-preserving%20semigroups%2C%20spectral%20gaps%2C%20and%20classical%20ground-state%20computation.pdf) · [LaTeX](Generators%20of%20stability-preserving%20semigroups%2C%20spectral%20gaps%2C%20and%20classical%20ground-state%20computation.tex)

## 2. Lee-Yang preserving quantum Markov semigroups and channels

Physical quantum Markov dynamics at finite spins, static and covariant Lee–Yang channels, and quantitative rigidity.

**63 pages** · [PDF](Lee-Yang%20preserving%20quantum%20Markov%20semigroups%20and%20channels.pdf) · [LaTeX](Lee-Yang%20preserving%20quantum%20Markov%20semigroups%20and%20channels.tex)

## 3. Positive stability-preserving semigroups and particle capacities

Positive stability-preserving dynamics at finite, infinite, and mixed capacities, with ancillary tests, domains, and semigroup generation.

**35 pages** · [PDF](Positive%20stability-preserving%20semigroups%20and%20particle%20capacities.pdf) · [LaTeX](Positive%20stability-preserving%20semigroups%20and%20particle%20capacities.tex)

## Source and certificates

Each PDF was compiled from its accompanying LaTeX file. The LaTeX embeds its bibliography; separate section files and bibliography files are not required. The flagship's rational certificate data remain in Appendix C, and its verification scripts are provided separately below. Compile a selected `.tex` file with Tectonic or a compatible LaTeX installation using the standard AMS packages.

The [certificates](certificates/) directory contains two independent exact verification procedures for the first paper's six-vertex EPR counterexample:

- [Full-space certificate](certificates/epr_six_vertex_certificate.py)
- [Independent reduced certificate](certificates/epr_independent_certificate.py)
- [Execution instructions and certificate scope](certificates/README.md)
- [Download the supplementary package](https://github.com/Isaac-Wei-2026/stability-preserving-semigroups/raw/refs/heads/main/certificates/epr-certificates.zip)

The supplementary package contains both scripts, execution instructions, and SHA256 checksums. Both scripts run with Python 3.10 or later and its standard library. The second procedure also prints floating-point diagnostics, which are not used by its exact assertions. These certificates cover the stated counterexample, not the other theorems.

## AI disclosure

The manuscripts disclose substantial mathematical and writing assistance from GPT-6 Pro in ChatGPT chat mode and GPT-6 Astra in Codex, both using the ultra reasoning setting. The flagship also discloses several rounds of revision suggestions from Claude Fable 5.1 in chat mode. The manuscripts describe the author's role in directing and organizing the research and state the author's responsibility. Complete proof-assistant verification is not claimed.
