#include <stdlib.h>
#include <stdio.h>
#define max 20

typedef struct hashtable{
    int key;
    struct hashtable* next;
}hashtable;


void init(hashtable arr[], int n){//初始化哈希表
    for (int i = 0; i < n; ++i) {
        arr[i].key = -1;
        arr[i].next = NULL;
    }
}

void  inserthash(hashtable arr[], int list[], int m, int count){//count是list数组的个数
    int tem = 0;
    for (int i = 0; i < count; ++i) {
        tem = list[i]%m;
        if (arr[tem].key == -1){
            arr[tem].key = list[i];
        }
        else{
            hashtable* p = (hashtable*)malloc(sizeof(hashtable));
            p->key = list[i];
            p->next = arr[tem].next;
            arr[tem].next = p;
        }
    }
}

int main(){
    int list1[] = {5, 65, 32, 43, 28, 18, 75, 35, 11, 89};
    hashtable arr1[max];
    init(arr1, 20);
    inserthash(arr1, list1,15, 10);
    for (int i = 0; i < max; ++i) {
        printf("%d\n", arr1[i].key);
    }
    return 0;
}
