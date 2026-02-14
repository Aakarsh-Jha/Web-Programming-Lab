def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    return -1


n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements in sorted order: ").split()))
key = int(input("Enter element to search: "))

result = binary_search(arr, 0, n - 1, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
