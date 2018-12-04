import math
import itertools
import sys





def prod(array):
    prod = 1
    for num in array:
        prod *= num
    return prod


if __name__ == "__main__":


    array = "2	3	5	7	11	13	17	19	23	29	31	37	41	43	47	53	59	61	67	71	73	79	83	89	97	101	103	107	109	113	127	131	137	139	149	151	157	163	167	173	179	181".split()
    #
    #
    # prod = 1
    # for num in array:
    #     prod *= int(num)
    #



    num_array = [int(num) for num in array]

    print len(num_array)

    test_num = sys.argv[1]
    print test_num

    bitarray = "{0:042b}".format(int(test_num))

    print bitarray



    mask = bitarray[::-1]

    print mask


    result = 1
    for i,v in enumerate(mask):
        if v=='1':
            result *= num_array[i]

    print result
    print result % 10**16
