import timeit
import random


def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return -1

    # Створюємо таблицю пропусків для всіх символів з патерну
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    default_skip = m  # Для символів, яких немає в патерні, задаємо пропуск = m

    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        if j == -1:
            return i + 1
        # Якщо символа немає в таблиці пропусків, використовуємо default_skip
        i += skip.get(text[i + m - j - 1], default_skip)
    return -1


def knuth_morris_pratt(text, pattern):
    m = len(pattern)
    n = len(text)

    def compute_lps_array(pattern):
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps_array(pattern)

    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1



def rabin_karp(text, pattern, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    h = 1
    p = 0
    t = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
        
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None


# Вибір підрядків
def choose_substrings(text):
    real_substring = text[len(text) // 2: len(text) // 2 + 10]  # існуючий підрядок
    fake_substring = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))  # вигаданий підрядок
    return real_substring, fake_substring

# Вимірювання часу виконання
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1)


# Основна функція порівняння алгоритмів
def compare_algorithms(file1, file2):
    text1 = read_file(file1)
    text2 = read_file(file2)

    # Вибір підрядків
    real_sub1, fake_sub1 = choose_substrings(text1)
    real_sub2, fake_sub2 = choose_substrings(text2)

    algorithms = {
        'Boyer-Moore': boyer_moore,
        'KMP': knuth_morris_pratt,
        'Rabin-Karp': rabin_karp
    }

    results = {}

    for name, algorithm in algorithms.items():
        # Вимірювання часу для статті 1
        time_real_1 = measure_time(algorithm, text1, real_sub1)
        time_fake_1 = measure_time(algorithm, text1, fake_sub1)

        # Вимірювання часу для статті 2
        time_real_2 = measure_time(algorithm, text2, real_sub2)
        time_fake_2 = measure_time(algorithm, text2, fake_sub2)

        results[name] = {
            'Article 1 (Real)': time_real_1,
            'Article 1 (Fake)': time_fake_1,
            'Article 2 (Real)': time_real_2,
            'Article 2 (Fake)': time_fake_2
        }

    return results

# Запуск порівняння
results = compare_algorithms('article1.txt', 'article2.txt')

# Виведення результатів
for algorithm, times in results.items():
    print(f"{algorithm}:")
    for case, time_taken in times.items():
        print(f"  {case}: {time_taken:.6f} seconds")