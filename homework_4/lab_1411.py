#Cesar Cortez
#PSID = 1836168

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_largest]:
                index_largest = j
        numbers[i], numbers[index_largest] = numbers[index_largest], numbers[i]

        print(' '.join([str(x) for x in numbers]),'')
        
    return numbers


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]

    selection_sort_descend_trace(numbers)