def insertion_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

arr = list(map(int, input("Enter an array values: ").split()))
sorted_arr = insertion_sort(arr)
print(sorted_arr)