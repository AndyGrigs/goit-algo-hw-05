
# Реалізація сортування вставками
import random
import timeit


def insertion_sort(arr):
    for element in range(1, len(arr)): # Починаємо з другого елемента

        element_to_isert = arr[element] # Ключовий елемент, який потрібно вставити

        element_before = element - 1 # Індекс для попередніх елементів
            # Порівнюємо з попередніми елементами  зміщуємо елементи вправо
        while element_before >= 0 and element_to_isert < arr[element_before]:

            arr[element_before + 1] = arr[element_before] # Зсуваємо елемент вправо

            element_before -= 1 # Переходимо до попереднього елемента

        arr[element_before + 1] = element_to_isert  # Вставляємо ключовий елемент у правильне місце
    return arr


print(insertion_sort([12, 11, 13, 5, 6]))

# Реалізація сортування злиттям

def merge_sort(arr):
    # Базовий випадок: якщо довжина масиву <= 1, масив вже відсортований
    if len(arr) > 1:
        # 1. Розбиваємо масив на дві частини
        mid = len(arr) // 2              # Знаходимо середину масиву
        left_half = arr[:mid]            # Ліва половина масиву
        right_half = arr[mid:]           # Права половина масиву

        # 2. Викликаємо merge_sort рекурсивно для лівої і правої частин
        merge_sort(left_half)            # Сортуємо ліву половину
        merge_sort(right_half)           # Сортуємо праву половину

        # 3. Злиття двох відсортованих частин
        i = j = k = 0

        # Порівнюємо елементи з обох половин і вставляємо менший у масив arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Якщо залишилися елементи в лівій половині, додаємо їх
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Якщо залишилися елементи в правій половині, додаємо їх
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  # Повертаємо відсортований масив

# print("Merge", merge_sort([38, 27, 43, 3, 9, 82, 10]))

def timsort(arr):
    return sorted(arr)

# Генерація тестових наборів даних
size = 1000  # Розмір масивів для тестування
random_data = random.sample(range(1, size + 1), size)
reversed_data = list(range(size, 0, -1))
sorted_data = list(range(1, size + 1))

# Функція для вимірювання часу виконання алгоритмів
def measure_time(sort_func, data):
    return timeit.timeit(lambda: sort_func(data.copy()), number=10)

# Порівняння алгоритмів на різних наборах даних
print("Результати вимірювання часу (у секундах):\n")

print("Випадковий набір чисел:")
print(f"Insertion Sort: {measure_time(insertion_sort, random_data):.5f}")
print(f"Merge Sort: {measure_time(merge_sort, random_data):.5f}")
print(f"Timsort: {measure_time(timsort, random_data):.5f}\n")

print("Відсортований у зворотному порядку набір:")
print(f"Insertion Sort: {measure_time(insertion_sort, reversed_data):.5f}")
print(f"Merge Sort: {measure_time(merge_sort, reversed_data):.5f}")
print(f"Timsort: {measure_time(timsort, reversed_data):.5f}\n")

print("Відсортований набір:")
print(f"Insertion Sort: {measure_time(insertion_sort, sorted_data):.5f}")
print(f"Merge Sort: {measure_time(merge_sort, sorted_data):.5f}")
print(f"Timsort: {measure_time(timsort, sorted_data):.5f}")
