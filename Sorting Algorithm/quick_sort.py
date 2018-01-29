#-*- coding:utf-8 -*-
# 快速排序

def quick_sort(lists,left,right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and key <= lists[right]:
            right -= 1
        lists[left] = lists[right]
        while left < right and key >= lists[left]:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists,low,left - 1)
    quick_sort(lists,left + 1,high)
    return lists

if __name__ == '__main__':
    lists = [3,4,7,2,6,5,9,8,1,10]
    print quick_sort(lists,0,9)
