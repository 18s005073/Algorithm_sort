# 选择排序
'''
1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3.重复第二步，直到所有元素均排序完毕
'''
def selectionSort(arr):
    for i in range(0,len(arr)-1):
        k = i
        for j in range(i+1,len(arr)):
            if arr[k]>arr[j]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    return arr

if __name__ == '__main__':
    arr = [1,4,2,6,3,5]
    print(selectionSort(arr))
