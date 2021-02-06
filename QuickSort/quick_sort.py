def quick_sort(array, pivot_location, compare_count=0):
    if len(array) == 1:
        return array, compare_count
    if len(array) == 2:
        if array[0] < array[1]:
            return [array[0], array[1]], compare_count + 1
        else:
            return [array[1], array[0]], compare_count + 1
    else:
        array, pivot_index = partition(array, pivot_location)
        if pivot_index >= 2:

            array[:pivot_index], compare_count = quick_sort(
                array[:pivot_index],
                pivot_location,
                compare_count
            )

        if pivot_index <= len(array) - 3:
            array[pivot_index+1:], compare_count = quick_sort(
                array[pivot_index+1:],
                pivot_location,
                compare_count
            )

    compare_count += len(array) - 1

    return array, compare_count


def partition(array, pivot_location):

    pivot_index = get_pivot_index(array, pivot_location)

    # put the pivot index in the beginning of the array
    if pivot_index != 0:
        array[0], array[pivot_index] = array[pivot_index], array[0]

    i = 1       # index of first element > array[0]

    for j in range(1, len(array)):
        if array[j] < array[0]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[0], array[i-1] = array[i-1], array[0]

    # return the index of pivot
    return array, i - 1


def get_pivot_index(array, pivot_location):
    if pivot_location == 'first':
        pivot_index = 0
    elif pivot_location == 'last':
        pivot_index = len(array) - 1
    else:
        first = array[0]
        middle = array[(len(array) - 1) // 2]
        last = array[-1]

        if middle < first < last or last < first < middle:
            pivot_index = 0

        elif first < middle < last or last < middle < first:
            pivot_index = (len(array) - 1) // 2

        else:
            pivot_index = len(array) - 1

    return pivot_index


if __name__ == "__main__":
    f = open("QuickSort.txt")
    array = [int(line) for line in f]
    sorted_array, compare_count = quick_sort(array, 'first')
    print(compare_count)

    f = open("QuickSort.txt")
    array = [int(line) for line in f]
    sorted_array, compare_count = quick_sort(array, 'last')
    print(compare_count)

    f = open("QuickSort.txt")
    array = [int(line) for line in f]
    sorted_array, compare_count = quick_sort(array, 'median')
    print(compare_count)
