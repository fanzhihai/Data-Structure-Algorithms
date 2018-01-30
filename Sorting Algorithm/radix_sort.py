# -*- coding:utf-8 -*-
# 基数排序

import math

def radix_sort(lists,radix=10):
    k = int(math.ceil(math.log(max(lists),radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists       

if __name__ == '__main__':
    lists = [3,4,7,2,6,5,9,8,1,10]
    print radix_sort(lists)
