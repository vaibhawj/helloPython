
def search(arr, item):
    return srch(arr, 0, len(arr)-1, item)

def srch(arr, start, end, item):
    if start >= end: return -1

    mid = int((start + end) / 2)
    if arr[mid] == item: return mid

    if item < arr[mid]:
        return srch(arr, start, mid, item)
    else:
        return srch(arr, mid+1, end, item)

