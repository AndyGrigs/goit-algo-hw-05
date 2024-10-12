def bi_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper = None

    while left <= right:
        iterations +=1
        mid = (left + right) // 2

        if arr[mid] == target:
            upper = arr[mid]
            return (iterations, upper)
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper = arr[mid]
            right = mid - 1


    if left < len(arr):
        upper = arr[left]

    return (iterations, upper)

# Тестуємо функцію:
arr = [0.1, 0.5, 1.3, 2.7, 3.6, 5.8, 7.9, 9.1]
target = 3.6

result = bi_search(arr, target)
print(result) 