x = """\
    0     0     0     0     0     0
     0     0     0     0     0     1
     0     0     0     0     1     0
     0     0     0     0     1     1
     0     0     0     1     0     0
     0     0     0     1     0     1
     0     0     0     1     1     0
     0     0     0     1     1     1
     0     0     1     0     0     0
     0     0     1     0     0     1
     0     0     1     0     1     0
     0     0     1     0     1     1
     0     0     1     1     0     0
     0     0     1     1     0     1
     0     0     1     1     1     0
     0     0     1     1     1     1
     0     1     0     0     0     0
     0     1     0     0     0     1
     0     1     0     0     1     0
     0     1     0     0     1     1
     0     1     0     1     0     0
     0     1     0     1     0     1
     0     1     0     1     1     0
     0     1     0     1     1     1
     0     1     1     0     0     0
     0     1     1     0     0     1
     0     1     1     0     1     0
     0     1     1     0     1     1
     0     1     1     1     0     0
     0     1     1     1     0     1
     0     1     1     1     1     0
     0     1     1     1     1     1
     1     0     0     0     0     0
     1     0     0     0     0     1
     1     0     0     0     1     0
     1     0     0     0     1     1
     1     0     0     1     0     0
     1     0     0     1     0     1
     1     0     0     1     1     0
     1     0     0     1     1     1
     1     0     1     0     0     0
     1     0     1     0     0     1
     1     0     1     0     1     0
     1     0     1     0     1     1
     1     0     1     1     0     0
     1     0     1     1     0     1
     1     0     1     1     1     0
     1     0     1     1     1     1
     1     1     0     0     0     0
     1     1     0     0     0     1
     1     1     0     0     1     0
     1     1     0     0     1     1
     1     1     0     1     0     0
     1     1     0     1     0     1
     1     1     0     1     1     0
     1     1     0     1     1     1
     1     1     1     0     0     0
     1     1     1     0     0     1
     1     1     1     0     1     0
     1     1     1     0     1     1
     1     1     1     1     0     0
     1     1     1     1     0     1
     1     1     1     1     1     0
     1     1     1     1     1     1"""

y = """\
     0     0     0     0     0     0
     0     0     0     0     1     0
     0     0     0     1     0     0
     0     0     0     1     1     0
     0     0     1     0     0     0
     0     0     1     0     1     0
     0     0     1     1     0     0
     0     0     1     1     1     0
     0     1     0     0     0     0
     0     1     0     0     1     0
     0     1     0     1     0     0
     0     1     0     1     1     0
     0     1     1     0     0     0
     0     1     1     0     1     0
     0     1     1     1     0     0
     0     1     1     1     1     0
     1     0     0     0     0     0
     1     0     0     0     1     0
     1     0     0     1     0     0
     1     0     0     1     1     0
     1     0     1     0     0     0
     1     0     1     0     1     0
     1     0     1     1     0     0
     1     0     1     1     1     0
     1     1     0     0     0     1
     1     1     0     0     1     1
     1     1     0     1     0     1
     1     1     0     1     1     1
     1     1     1     0     0     1
     1     1     1     0     1     1
     1     1     1     1     0     1
     1     1     1     1     1     1
     0     0     0     0     0     1
     0     0     0     0     1     1
     0     0     0     1     0     1
     0     0     0     1     1     1
     0     0     1     0     0     1
     0     0     1     0     1     1
     0     0     1     1     0     1
     0     0     1     1     1     1
     0     1     0     0     0     1
     0     1     0     0     1     1
     0     1     0     1     0     1
     0     1     0     1     1     1
     0     1     1     0     0     1
     0     1     1     0     1     1
     0     1     1     1     0     1
     0     1     1     1     1     1
     1     0     0     0     0     1
     1     0     0     0     1     1
     1     0     0     1     0     1
     1     0     0     1     1     1
     1     0     1     0     0     1
     1     0     1     0     1     1
     1     0     1     1     0     1
     1     0     1     1     1     1
     1     1     0     0     0     0
     1     1     0     0     1     0
     1     1     0     1     0     0
     1     1     0     1     1     0
     1     1     1     0     0     0
     1     1     1     0     1     0
     1     1     1     1     0     0
     1     1     1     1     1     0"""

import pprint
import itertools
import math

#pick is 0 indexed
def hasNeighbor(picked, total_num):
    for i in range(total_num-1):
        if (picked >>i & 1) and (picked >> (i+1) & 1):
            return True

    if (picked & 1) and (picked >> (total_num - 1) & 1):
        return True

    return False

def count_neighbor_pick(n):
    s = 0
    for x in range(2 ** n):
        if hasNeighbor(x, n):
            s += 1
    return s

def nCr(n,r):
    f = math.factorial
    try:
        return f(n) / f(r) / f(n-r)
    except ValueError:
        return 0

for N in xrange(3,15):
    s = N
    for p in xrange(3, N+1):
        # print N, p
        s += nCr(N,p) - nCr(N-p-1, p-1)/p
    print N, s, count_neighbor_pick(N)

# def comb_num(table_size):
#     if (table_size < 2):
#         return 1
#
#     s = 0
#
#     for total_pick in xrange(3,table_size):
#         pool_left = table_size - 2
#
#         for k in xrange(0, pool_left+1):
#             if k > 0:
#                 break
#             else:
#                 for temp_pool in xrange(k,pool_left+1):
#                     s += nCr(temp_pool, k)
#
#     return s
#
# mx = ["".join(l.split()) for l in x.split('\n')]
# my = ["".join(l.split()) for l in y.split('\n')]
#
# # print mx, my
#
# count = 0
# map = {}
#
# for i, v in enumerate(mx):
#     t = my[i]
#     map[i]=mx.index(t)
#     # print i, mx.index(t)
#
#
# # pprint.pprint(map)
# #
# chains = []
# #
# for k,v in map.iteritems():
#     # print k,v
#     if not chains:
#         chains.append([k,v])
#         continue
#
#     if not any([k in l for l in chains]):
#         new_l = [k,v]
#         new_k = v
#         while (new_k not in new_l) or new_l.index(new_k) > 0:
#             next_v = map[new_k]
#             new_l.append(next_v)
#             new_k = next_v
#
#         chains.append(new_l)
#
# print chains
# print [len(x) for x in chains]
#


# ways = []
# for l in chains:
#     length = len(l)-1
#     ways.append(length)
#
# print ways
#
# sum_all = 0
# for L in range(1,len(ways)+1):
#     # print L
#     for subset in itertools.combinations(ways, L):
#         print(subset)
#
#         local_product = 1
#         for x in subset:
#             if x == 1 or x == 2:
#                 local_product *= x
#                 continue
#             local_product *= x * (2 ** (x - 3))
#             # print local_product
#         sum_all += local_product
#         # if subset:
#         #     tmp = 1
#         #     for x in subset:
#         #         tmp *= x
#         #     sum_all += tmp
# #
# print sum_all
# print 2**64 - sum_all
