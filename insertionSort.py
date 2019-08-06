# 插入排序
'''
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置.
(如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面.)
'''
def insertionSort(arr):
    arr1 = list()
    arr1.append(arr[0])
    for j in range(1,len(arr)):
        for i in range(0,j):
            if arr[j] < arr1[i]:
                arr1.insert(i,arr[j])
                break
            elif i == j-1:
                arr1.append(arr[j])

    return arr1

if __name__ == '__main__':
    arr = [1,3,5,2,4,5,2,7,3,9,5]
    print(insertionSort(arr))
