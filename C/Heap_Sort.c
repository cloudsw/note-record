#include <stdio.h>

void swap(int arr[], int i, int j){
    int tem = arr[i];
    arr[i] = arr[j];
    arr[j] = tem;
}

void heapify(int tree[], int n,int i){//n为tree数组的个数，i为开始进行heapify的索引。
    int cl = 2 * i + 1;
    int cr = 2 * i + 2;
    int max = i;
    if (cl < n && tree[cl] > tree[max]){
        max = cl;
    }
    if (cr < n && tree[cr] > tree[max]){
        max = cr;
    }
    if (max != i){
        swap(tree, max, i);
        heapify(tree, n, max);
    }
}

void build_heap(int tree[], int n){//建造heap，从下往上依次进行heapify操作。
    int last_note = n - 1;
    int parent = (last_note - 1) / 2;
    int i;
    for (i = parent; i >= 0; i--){
        heapify(tree, n, i);
    }
}

void heap_sort(int tree[], int n){
    build_heap(tree, n);
    int i;
    for (i = n - 1; i >=0 ; i--) {
        swap(tree, i, 0);
        heapify(tree, i, 0);
    }
}

int main(){
    int list[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    heap_sort(list, 10);
    for (int i = 0; i < 10; ++i) {
        printf("%d ",list[i]);
    }
    return 0;
}
