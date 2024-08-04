from fuzzy_extractor import FuzzyExtractor
import random, string

INPUT_LENGTH = 16 # bytes of input accepted
EPSILON = 8 # bits of similarity
ext = FuzzyExtractor(INPUT_LENGTH, EPSILON)

# initial sets
S_A = ["ABCDABCDABCDABCD", "EFGHEFGHEFGHEFGH", "IJKLIJKLIJKLIJKL", "MNOPMNOPMNOPMNOP", "QRSTQRSTQRSTQRST", "UVWXUVWXUVWXUVWX", "Y_Z_Y_Z_Y_Z_Y_Z_"]

S_B = ["1234123412341234", "AAAAAAAAAAAAAAAA", "ABCFABCDABCDABCF", "MPONMPONMPONMPON", "XXXXXXXXXXXXXXXX", "MNOPMNOPMNOPMPON"]

# |S_A| = n and |S_B| = m

# finding the helpers and the keys for S_A
keys = []
helpers = []

for a in S_A:
    k, h = ext.generate(a)
    keys.append(k)
    helpers.append(h)
    # also pretend we're creating S_A^k here which is hash(a)^k

# this is O(n * c) where c is the complexity of generate

# at this point A sends the helpers to B along with S_A^k
# helpers, S_A^k -> B

recov = [[None for _ in range(len(S_B))] for _ in range(len(helpers))]

for i in range(len(S_B)):
    for j in range(len(helpers)):
        recov[j][i] = ext.reproduce(S_B[i], helpers[j])

# this is O(nm * c') where c' is the complexity of reproduce

# after making the recovery matrix, B sends it back to A

candis = []

for i in range(len(recov)):
    for j in range(len(recov[i])):
        for k in range(len(keys)):
            if keys[k] == recov[i][j]:
                if S_A[k] not in candis:
                    candis.append(S_A[k])

# this is O(n^2m)

print(S_A)
print(S_B)
print(candis)
