"""
Count inverse using divide and conquer

@author: ziye
"""


def count_inverse(array):
    if len(array) == 1:
        return 0, array
    elif len(array) == 2:
        if array[0] < array[1]:
            return 0, array
        else:
            return 1, array[::-1]
    else:
        left_half_len = len(array) // 2
        left_count, left_array,  = count_inverse(array[:left_half_len])
        right_count, right_array,  = count_inverse(array[left_half_len:])
        split_count, sorted_array = merge_count(left_array, right_array)
        count = left_count + right_count + split_count
        return count, sorted_array


def merge_count(left_array, right_array):
    sorted_array = [0] * (len(left_array) + len(right_array))

    i = 0
    j = 0
    k = 0
    count = 0

    while True:
        if left_array[i] < right_array[j]:
            sorted_array[k] = left_array[i]
            i += 1
            k += 1
            if i == len(left_array):
                sorted_array[k:] = right_array[j:]
                break
        else:
            sorted_array[k] = right_array[j]
            count += len(left_array) - i
            j += 1
            k += 1
            if j == len(right_array):
                sorted_array[k:] = left_array[i:]
                break

    return count, sorted_array


if __name__ == "__main__":
    f = open('IntegerArray.txt')
    lines = f.readlines()
    f.close()
    array = [int(line) for line in lines]

    count, sorted_array = count_inverse(array)
    print(f"Inverse count is {count}")
