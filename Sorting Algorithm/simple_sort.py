# -*- coding:utf-8
"""
# 简单排序
# 依次找到最小的元素，依次从前排到后
# @author:BigOceans
# https://github.com/fanzhihai
"""

def simple_sort(lists):
    count = len(lists)
    for i in range(count):
        min = i
        
        for j in range(i+1, count):
            if lists[min] > lists[j]:
                min = j
                
        lists[min], lists[i] = lists[i],lists[min]

    return lists


if __name__ == '__main__':
    lists = [2,5,1,3,6,9,7]
    print u'原始数组:' + str(lists)
    
    lists_sorted = simple_sort(lists)

    print u'排序数组:' + str(lists_sorted)
