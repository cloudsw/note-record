#include <stdio.h>

void merge(int arr[], int L, int M, int R){//L,M,R为索引序列，从0开始。L为数组的左边端点，R为数组的右边端点，M为数组的两个不同小数组的分隔点。
    int left_size = M - L;
    int right_size = R - M + 1;
    int left[left_size];
    int right[right_size];
    int i, j, k;
    for (i = L; i < M; i++) {
        left[i] = arr[i];
    }
    for (i = M; i <= R; i++) {
        right[i - M] = arr[i];
    }

    i = 0, j = 0, k = 0;
    while (i < left_size && j < right_size){//i,j都没有超过两个小数组的总个数
        if (left[i] < right[j]){
            arr[k] = left[i];
            i++;
            k++;
        }
        else {
            arr[k] = right[j];
            j++;
            k++;
        }
    }
    while (i < left_size){//此时，right已经完成插入
        arr[k] = left[i];
        i++;
        k++;
    }
    while (j < right_size){//此时，left已经完成插入
        arr[k] = right[j];
        j++;
        k++;
    }
}
void merge_sort(int arr[], int L, int R){
    if (L == R){
        return;
    }
    else{
        int M = (L + R) / 2;
        merge_sort(arr, L, M);
        merge_sort(arr, M+1, R);
        merge(arr, L, M+1, R);
    }
}

int main(){
    int list[] = {3, 5, 7, 9, 10, 1, 2, 4, 6, 8};
    int L = 0;
    int R = 9;
    merge_sort(list, L, R);
    for (int i = 0; i <=R; ++i) {
        printf("%d ", list[i]);
    }
    return 0;
}
