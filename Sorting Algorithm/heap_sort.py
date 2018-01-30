# -*- coding:utf-8 -*-
# 堆排序


def heap_adjust(lists,i,size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max_ = i
    if i < size/2:
        if lchild < size and lists[lchild] > lists[max_]:
            max_ = lchild
        if rchild < size and lists[rchild] > lists[max_]:
            max_ = rchild
        if max_ != i:
            lists[max_],lists[i] = lists[i],lists[max_]
            heap_adjust(lists,max_,size)

def heap_build(lists,size):
    for i in range(size/2)[::-1]:
        heap_adjust(lists,i,size)

def heap_sort(lists):
    size = len(lists)
    heap_build(lists,size)
    for i in range(size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        heap_adjust(lists,0,i)
    return lists

if __name__ == '__main__':
    lists = [3,4,7,2,6,5,9,8,1,10]
    print heap_sort(lists)

