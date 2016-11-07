import random
from Heap import Heap


def test():
    test_lst = []
    for j in range(1, 10):
        for i in range(j * 100):
                test_lst.append(random.randint(1, j*100))
        random.shuffle(test_lst)
        print(shaker_sort(test_lst))


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst


def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_pos = i
        for j in range(min_pos, len(lst)):
            if lst[j] < lst[min_pos]:
                min_pos = j
        lst[i], lst[min_pos] = lst[min_pos], lst[i]
    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        tmp = lst[i]
        while j >= 0 and lst[j] > tmp:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = tmp

    return lst


def quick_sort(lst):
    if len(lst) == 0:
        return False
    start = 0
    end = len(lst) - 1
    quick_sort_aux(lst, start, end)
    return lst


def quick_sort_aux(lst, start, end):
    if start >= end:
        return
    else:
        boundary = partition(lst, start, end)
        quick_sort_aux(lst, start, boundary-1)
        quick_sort_aux(lst, boundary+1, end)


def partition(lst, start, end):
    pivot = lst[start]
    boundary = start
    for i in range(start + 1, end + 1):
        if lst[i] < pivot:
            boundary += 1
            lst[boundary], lst[i] = lst[i], lst[boundary]
    lst[boundary], lst[start] = lst[start], lst[boundary]
    return boundary


def merge_sort(lst):
    start = 0
    end = len(lst) - 1
    tmp = [None] * len(lst)
    merge_sort_aux(lst, tmp, start, end)
    return lst


def merge_sort_aux(lst, tmp, start, end):
    if start < end:  # we still have two more items needs to be sorted
        mid = (start + end) // 2
        merge_sort_aux(lst, tmp, start, mid)
        merge_sort_aux(lst, tmp, mid+1, end)

        merge_array(lst, tmp, start, mid, end)

        for i in range(start, end + 1):
            lst[i] = tmp[i]
        return lst


def merge_array(lst, tmp, start, mid, end):
    ia = start
    ib = mid + 1
    for k in range(start, end + 1):
        if ia > mid:
            tmp[k] = lst[ib]
            ib += 1
        elif ib > end:
            tmp[k] = lst[ia]
            ia += 1
        elif lst[ia] > lst[ib]:
            tmp[k] = lst[ib]
            ib += 1
        else:  # lst[ia] < lst[ib]
            tmp[k] = lst[ia]
            ia += 1
    return tmp


def bubble_sort_ver1(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                swap(lst, j, j + 1)
    return lst


def bubble_sort_ver2(lst):
    for i in range(len(lst) - 1):
        swapped = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
                swapped = True
        if swapped is False:
            return lst


def shaker_sort(lst):
    i = 0
    while i != len(lst) - 2:
        swapped = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                swapped = True
                swap(lst, j, j + 1)
        if swapped is False:
            return lst
        swapped = False

        i += 1
        for j in range(len(lst) - 1 - i, i - 1, -1):
            if lst[j] < lst[j - 1]:
                swap(lst, j, j - 1)
                swapped = True
        if swapped is False:
            return lst
        i += 1


def heap_sort(lst):
    a_heap = Heap()
    for item in lst:
        a_heap.add(item)
    tmp = []
    while not a_heap.is_empty():
        tmp.append(a_heap.get_max())
    return tmp

random.seed()
#test()
lst = [3, 2, 1, 5, 6, 7]
print(shaker_sort(lst))
