# -*- coding:utf-8
"""
# 冒泡排序
# 将数组当中的左右元素，依次比较，保证右边的元素始终大于左边的元素，保证最大的在右边，就像冒泡一样，大的气泡在下面
# @author:BigOceans
# https://github.com/fanzhihai
"""

def bubble_sort(lists):
    count = len(lists)

    for i in range(count):
        for j in range(i+1,count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]

    return lists


if __name__ == '__main__':
    lists = [2,5,1,3,6,9,7]
    print u'原始数组:' + str(lists)
    
    lists_sorted = bubble_sort(lists)

    print u'排序数组:' + str(lists_sorted)
