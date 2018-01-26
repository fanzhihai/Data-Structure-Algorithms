#-*- coding:utf-8 -*-
# 插入排序

def insert_sort(lists):
    num = len(lists) 
    for i in range(num):
        key = lists[i]
        j = i-1
        while j>= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

if __name__ == '__main__':
    lists = [3,4,7,2,1,10]
    print insert_sort(lists)
