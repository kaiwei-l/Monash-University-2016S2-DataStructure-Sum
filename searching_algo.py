# recursion
def binary_search_recur(lower, upper, lst, target):
    if len(lst) == 0:
        return False
    if lower == upper:
        return False
    else:
        mid = (upper + lower) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return binary_search_recur(mid+1, upper, lst, target)
        else:  # mid > target
            return binary_search_recur(lower, mid, lst, target)


# iteration
def binary_search_iter(lower, upper, lst, target):
    if len(lst) == 0:
        return False
    while lower <= upper:
        mid = (lower + upper) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lower = mid + 1
        else:  # mid > target
            upper = mid - 1
    return False

test = []
for i in range(1000000):
    test.append(i)

target = 499999999999
print(binary_search_recur(0, len(test)-1, test, target))
print(binary_search_iter(0, len(test)-1, test, target))
