#-*- coding:utf-8 -*-
# 希尔排序

def shell_sort(lists):
    num = len(lists)
    step = 2
    gap  = num / step
    while gap > 0:
        for i in range(gap):
            j = i + gap
            while j < num:
                k = j - gap
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + gap] = lists[k]
                        lists[k] = key
                    k -= gap
                j += gap
        gap /= step
    return lists


if __name__ == '__main__':
    lists = [3,4,7,2,1,10]
    print shell_sort(lists)
