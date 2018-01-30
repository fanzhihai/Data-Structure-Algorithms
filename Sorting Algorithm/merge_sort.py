# -*- coding:utf-8 -*-
# 归并排序

def merge(left,right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)

if __name__ == '__main__':
    lists = [3,4,7,2,6,5,9,8,1,10]
    print merge_sort(lists)
        
