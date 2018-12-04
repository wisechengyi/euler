import math
import itertools


def prod(array):
    prod = 1
    for num in array:
        prod *= num
    return prod

array = "2	3	5	7	11	13	17	19	23	29	31	37	41	43	47	53	59	61	67	71	73	79	83	89	97	101	103	107	109	113	127	131	137	139	149	151	157	163	167	173	179	181".split()
#
#
# prod = 1
# for num in array:
#     prod *= int(num)
#



num_array = [int(num) for num in array]

product = prod(num_array)
root = math.sqrt(product)

for i, v in enumerate(num_array):
    left_prod = prod(num_array[:i+1])
    right_prod = prod(num_array[i+1:])

    print left_prod, left_prod < root, right_prod

# print len(num_array)


curr_max = 2305567963945518424753102147331756070

# curr
#
for i in range(1, len(num_array)/2 + 1):
    print i
    g = itertools.combinations(num_array, i)
    while True:
        try:
            comb = next(g)
            p = prod(comb)
            if p > curr_max and p < root:
                curr_max = p
                print curr_max
            # print comb
            # print prod(comb)
        except StopIteration:
            break

    # if i>1:
    #     break
# while True:
