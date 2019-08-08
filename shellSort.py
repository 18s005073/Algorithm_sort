# 希尔排序
'''
https://www.cnblogs.com/chengxiao/p/6104371.html
选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
按增量序列个数 k，对序列进行 k 趟排序；
每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，
分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
'''
def shellSort(arr):
    import math
    gap = int(len(arr)/3)
    while gap >0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i-gap
            while j >= 0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

if __name__ == '__main__':
    arr = [1,5,2,7,4,0,4,8,0,12,15,10]
    print(shellSort(arr))

