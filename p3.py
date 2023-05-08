def qsort(array, left, right):
    middle = (left+right) // 2
    
    p = array[middle]
    i,j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
def binary_search(array, element, left, right): 
    if left > right: 
        return False
    
    middle = (right+left) // 2 
    if array[middle-1] < element and array[middle] >= element: 
        return middle-1 
    elif element < array[middle]: 
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)

while True:
    try:
        arr = list(map(int,input("Введите последовательность чисел:\n").split(" ")))
        break
    except Exception as e:
        print("ОШИБКА ВВОДА ПОСЛЕДОВАТЕЛЬНОСТИ:",e)
        print("Поробуйте еще раз")
while True:
    try:
        elem = int(input("Введите любое число:\n"))
        break
    except Exception as e:
        print("ОШИБКА ВВОДА ЧИСЛА:",e)
        print("Попробуйте еще раз")

qsort(arr,0,len(arr)-1)
try:
    if ans := binary_search(arr, elem, 0, len(arr) - 1):
        print(f"Отсортированный массив:{arr}")
        print(f"Число {arr[ans]} на позиции {ans} меньше введеного числа {elem}")
    else:
        raise Exception(f"Позиция для числа {elem} не найдена!")
except Exception as e:
    print("ОШИБКА ПРИ ПОИСКЕ:",e)
    print("Найти позицию не удалось! Попробуйте заного")