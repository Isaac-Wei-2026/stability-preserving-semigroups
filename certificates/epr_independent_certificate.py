"""Exact independent certificate; only Python standard-library rational arithmetic.

This verifies a zero inside the s^(-1/2) polydisk of the unique ground-state
polynomial for the unweighted six-vertex double-star at s=1/2.
The decimal trial vector is input data, never treated as an exact eigenvector.
All assertions supporting the conclusion use Fraction arithmetic.
"""

from fractions import Fraction as F
from itertools import product


EDGES = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)]
BITS = list(product((0, 1), repeat=6))


def charge(x):
    return x[0] + x[4] + x[5] - x[1] - x[2] - x[3]


def label(x):
    return x[0], x[1], x[2] + x[3], x[4] + x[5]


STATES = sorted({label(x) for x in BITS if charge(x) == 0})
assert len(STATES) == 10
INDEX = {a: i for i, a in enumerate(STATES)}
NEUTRAL = [x for x in BITS if charge(x) == 0]
assert len(NEUTRAL) == 20


def action_row(x):
    """Row of 4K on configurations; K=sum_e |00+.5 11><00+.5 11|."""
    row = {x: 0}
    for i, j in EDGES:
        if x[i] == x[j]:
            row[x] += 4 if x[i] == 0 else 1
            y = list(x)
            y[i] = 1 - y[i]
            y[j] = 1 - y[j]
            y = tuple(y)
            row[y] = row.get(y, 0) + 2
    return row


# Derive, rather than transcribe, the rational orbit-constant quotient matrix.
M = [[0] * 10 for _ in range(10)]
for state in STATES:
    representatives = [x for x in NEUTRAL if label(x) == state]
    rows = []
    for x in representatives:
        row = [0] * 10
        for y, coefficient in action_row(x).items():
            assert charge(y) == 0
            row[INDEX[label(y)]] += coefficient
        rows.append(row)
    assert all(row == rows[0] for row in rows)
    M[INDEX[state]] = rows[0]


# The whole neutral configuration graph is connected, not just the quotient.
seen = {NEUTRAL[0]}
todo = list(seen)
while todo:
    x = todo.pop()
    for y, c in action_row(x).items():
        if c > 0 and y not in seen:
            assert charge(y) == 0
            seen.add(y)
            todo.append(y)
assert seen == set(NEUTRAL)


# Every other charge block has Perron bound at most 20 for M=4K.
# Conjugate by the positive weights (1/2)^(|x|/2): each monochromatic
# edge has weighted row sum 5; other edges contribute zero.
for x in BITS:
    if charge(x) != 0:
        monochromatic = sum(x[i] == x[j] for i, j in EDGES)
        assert monochromatic <= 4
        assert 5 * monochromatic <= 20


trial = list(map(F, [
    "1", ".008942179087130", ".000136748346620",
    ".171232824560490", ".002452435031309",
    ".171232824560490", ".002452435031309",
    ".097255575326164", ".037858301388951",
    ".001200949534669",
]))
assert all(0 < a <= 1 for a in trial)
Ma = [sum(F(M[i][j]) * trial[j] for j in range(10)) for i in range(10)]
ratios = [Ma[i] / trial[i] for i in range(10)]
LOWER, UPPER = min(ratios), max(ratios)
assert LOWER > 21
assert UPPER - LOWER < F(1, 10**9)

# Perron-Frobenius and Collatz-Wielandt place the neutral Perron root lambda
# in [LOWER,UPPER]. Since LOWER>20 it is the unique global largest eigenvalue.
# Normalize the true per-configuration eigenvector by v_0=1.
# The principal submatrix with vacuum deleted has infinity norm exactly 18.
rest_norm = max(sum(M[i][j] for j in range(1, 10)) for i in range(1, 10))
assert rest_norm == 18
residual = max(
    max(abs(Ma[i] - LOWER * trial[i]), abs(Ma[i] - UPPER * trial[i]))
    for i in range(1, 10)
)
ETA = residual / (LOWER - rest_norm)
assert ETA < F(1, 10**9)


# Exact complex rational arithmetic as (real,imaginary) pairs.
ZERO, ONE = (F(0), F(0)), (F(1), F(0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def scale(a, b):
    return a[0] * b, a[1] * b


def norm2(a):
    return a[0]**2 + a[1]**2


# Coordinates of the tilted ground polynomial f(s^(-1/2) z), all rational.
CENTER = (F(175105, 10**6), F(981180, 10**6))
LEAF = (F(-379834, 10**6), F(921467, 10**6))
RADIUS = F(499, 500)
assert norm2(CENTER) < RADIUS**2
assert norm2(LEAF) < RADIUS**2
fixed = [CENTER, CENTER, LEAF, LEAF, LEAF]

# The last leaf remains free: tilted f=A+B*z_5.
A0 = B0 = ZERO
countA = countB = 0
for x in NEUTRAL:
    degree = sum(x)
    assert degree % 2 == 0
    tilt = F(2 ** (degree // 2))
    monomial = ONE
    for j in range(5):
        if x[j]:
            monomial = mul(monomial, fixed[j])
    value = scale(monomial, tilt * trial[INDEX[label(x)]])
    if x[5] == 0:
        A0 = add(A0, value)
        countA += 1
    else:
        B0 = add(B0, value)
        countB += 1
assert countA == countB == 10

# Every fixed-coordinate monomial has modulus <=1, and every tilt <=8.
# Consequently |A-A0|,|B-B0| <=80*ETA and |A0|,|B0|<=80.
DELTA = 80 * ETA
gap = RADIUS**2 * norm2(B0) - norm2(A0)
error = 320 * DELTA + 2 * DELTA**2
assert gap > F(1, 10**5)
assert gap > error

# Therefore RADIUS^2*|B|^2-|A|^2>0 for the TRUE ground eigenvector. B!=0,
# and z_5=-A/B lies strictly inside radius 499/500. All original coordinates
# sqrt(2)*z_j consequently lie strictly inside (499/500)*sqrt(2)<s^(-1/2),
# but the true ground-state polynomial vanishes at that tuple.
print("EXACT CERTIFICATE PASS")
print("states:", STATES)
print("matrix 4K:")
for row in M:
    print(row)
print("rationally certified: 21 < lambda(4K), width < 1e-9")
print("rationally certified: eigenvector sup error < 1e-9")
print("rationally certified: gap > 1e-5 and gap > full error bound")

# Decimal values below are diagnostics only, never used by any assertion.
print("diagnostic lambda interval:", float(LOWER), float(UPPER))
print("diagnostic eta:", float(ETA))
print("diagnostic squared-modulus gap / error:", float(gap), float(error))
