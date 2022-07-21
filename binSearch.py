import random
import time

def naive(num, arr):
    for i in arr:
        if(i==num):
            return i
    return -1

def binSearch(num, arr, low, high):
    if high >= low:
        ind = (high+low)//2
        
        #if element is found
        if arr[ind] == num:
            return ind

        #if element is smaller than mid
        elif arr[ind] > num:
            return binSearch(num, arr, low, ind-1)

        #if element is larger than mid
        else:
            return binSearch(num, arr, ind+1, high)

    else:
        return -1

if __name__=="__main__":

    length = 300000
    sorted_list=set()
    while len(sorted_list)< length:
        sorted_list.add(random.randint(-3*length,3*length))    
    sorted_list=sorted(list(sorted_list))

    elem = int(input("\n\nInput number to search: "))
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    start=time.time()
    result = binSearch(elem,sorted_list, 0, len(sorted_list)-1)
    end = time.time()
    print(f'~boring stuff~\n\nThe sorted list length is {len(sorted_list)}',
        'units...',
        '\nCrazy, huh?!\n',
        'The median value is {0}'.format(sorted_list[len(sorted_list)//2]),
        '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n', sep ='\n')

    print(f'{elem} is present omg! :D' if result != -1 else f'Unfortunately {elem} is not present')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print("Binary search time: ", (end-start))

    print('\n')

    start=time.time()
    result = naive(elem,sorted_list)
    end = time.time()
    print("Naive search time: ", (end-start))
    
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    