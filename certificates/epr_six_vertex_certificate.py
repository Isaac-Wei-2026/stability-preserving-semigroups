"""Exact standard-library certificate: a zero strictly inside radius sqrt(2).

No floating point or numerical eigensolver is used in any assertion.
K is the negative EPR Hamiltonian at s=1/2 on edges 01,02,03,14,15.
"""
from fractions import Fraction as F

EDGES = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)]
N = 64
K = [[F(0) for _ in range(N)] for _ in range(N)]
for b in range(N):
    for i, j in EDGES:
        bi, bj = (b >> i) & 1, (b >> j) & 1
        if bi == bj:
            for out in (0, 1):
                c = (b & ~(1 << i) & ~(1 << j)) | (out << i) | (out << j)
                K[c][b] += F(1, 2) ** (bi + out)
assert all(K[i][j] == K[j][i] for i in range(N) for j in range(N))

# Exact inertia proves that all but the largest eigenvalue are below 37/8.
def charge(b):
    return sum((b >> j) & 1 for j in (0, 4, 5)) - sum((b >> j) & 1 for j in (1, 2, 3))

assert all(not K[i][j] or charge(i) == charge(j) for i in range(N) for j in range(N))

negative = 0
pivot_signs = []
for q in range(-3, 4):
    sector = [b for b in range(N) if charge(b) == q]
    A = [[F(37 if i == j else 0) - 8 * K[i][j] for j in sector] for i in sector]
    signs = []
    for i in range(len(sector)):
        pivot = A[i][i]
        assert pivot != 0
        negative += pivot < 0
        signs.append('+' if pivot > 0 else '-')
        for j in range(i + 1, len(sector)):
            for k in range(j, len(sector)):
                A[k][j] -= A[j][i] * A[k][i] / pivot
                A[j][k] = A[k][j]
    pivot_signs.append((q, ''.join(signs)))
assert negative == 1
assert K[0][0] == 5

states = [(0,0,0,0),(0,0,1,1),(0,0,2,2),(0,1,0,1),(0,1,1,2),
          (1,0,1,0),(1,0,2,1),(1,1,0,0),(1,1,1,1),(1,1,2,2)]
numerators = [1000000000000000,8942179087130,136748346620,171232824560490,
              2452435031309,171232824560490,2452435031309,97255575326164,
              37858301388951,1200949534669]
amps = {state:F(num,10**15) for state,num in zip(states,numerators)}
v = []
for b in range(N):
    state = ((b >> 0)&1,(b >> 1)&1,((b >> 2)&1)+((b >> 3)&1),
             ((b >> 4)&1)+((b >> 5)&1))
    v.append(amps.get(state,F(0)))
assert v[0] == 1
lam = F(539109343678406,10**14)
r = [sum(K[i][j] * v[j] for j in range(N)) - lam*v[i] for i in range(N)]
assert sum(x*x for x in r) < F(1,10**24)
assert lam - F(37,8) > F(1,2)

# Therefore the orthogonal projection v_g onto the true top eigenspace
# obeys ||v-v_g||_2 < 2*10^-12. In particular v_g is nonzero.

def add(x,y): return x[0]+y[0],x[1]+y[1]
def mul(x,y): return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(c,x): return c*x[0],c*x[1]
def norm2(x): return x[0]*x[0]+x[1]*x[1]

zc=(F(175105,10**6),F(981180,10**6))
zl=(F(-379834,10**6),F(921467,10**6))
certified_radius=F(499,500)
assert norm2(zc)<certified_radius**2 and norm2(zl)<certified_radius**2
fixed=[zc,zc,zl,zl,zl]
A=(F(0),F(0));B=(F(0),F(0))
for b in range(N):
    if not v[b]: continue
    degree=b.bit_count()
    assert degree%2==0
    term=(v[b]*2**(degree//2),F(0))
    for j in range(5):
        if (b>>j)&1: term=mul(term,fixed[j])
    if (b>>5)&1:B=add(B,term)
    else:A=add(A,term)

# These wide rational bounds leave much more room than the eigenvector error.
assert norm2(A) < F(85,1000)**2
assert norm2(B) > F(852,10000)**2

# At the five fixed coordinates each monomial has modulus<1, and tilting
# by sqrt(2) multiplies each even coefficient by at most8. Each linear
# coefficient A or B involves at most32 terms. Thus replacing v by v_g
# changes A and B by less than 32*8*2e-12 < 1e-8.
err=F(1,10**8)
assert 32*8*F(2,10**12) < err
assert F(85,1000)+err < F(852,10000)-err
assert F(85,1000)+err < certified_radius*(F(852,10000)-err)

print('PASS: exact inertia has one negative pivot:',pivot_signs)
print('PASS: squared eigenvector residual < 10^-24')
print('PASS: |A_v|<85/1000 and |B_v|>852/10000')
print('PASS: true ground polynomial has all |z_i|<499/500 after sqrt(2) scaling')
