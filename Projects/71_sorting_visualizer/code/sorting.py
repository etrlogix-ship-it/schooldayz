import time, os, random

def clear(): os.system("clear")

def draw(arr, highlight=None, title=""):
    clear()
    max_val = max(arr) if arr else 1
    height = 15
    print(f"Sorting Visualizer — {title}")
    for row in range(height, 0, -1):
        line = ""
        for i, val in enumerate(arr):
            bar_height = int((val / max_val) * height)
            if highlight and i in highlight:
                char = "█"
            else:
                char = "▓" if bar_height >= row else " "
            line += char
        print(line)
    print("".join(str(v%10) for v in arr))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            draw(arr, {j, j+1}, "Bubble Sort")
            time.sleep(0.05)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            draw(arr, {i, j, min_idx}, "Selection Sort")
            time.sleep(0.03)
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            draw(arr, {j, j+1}, "Insertion Sort")
            time.sleep(0.05)
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

print("Sorting Algorithm Visualizer")
print("============================")
print("1) Bubble Sort  2) Selection Sort  3) Insertion Sort")
choice = input("Choose: ")
arr = random.sample(range(1, 50), 30)

start = time.time()
if choice == "1": bubble_sort(arr)
elif choice == "2": selection_sort(arr)
elif choice == "3": insertion_sort(arr)
elapsed = time.time() - start

draw(arr, title="Sorted!")
print(f"\nSorted in {elapsed:.2f} seconds!")
