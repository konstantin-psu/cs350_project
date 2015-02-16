#include "quicksort.h"


template <class T>
quicksort<T>::quicksort() {
    array = nullptr;
    srand(time(NULL));
    length = 0;
}

//template<class T>
//quicksort::quicksort(int size) {
//    array = nullptr;
//    srand(time(NULL));
//    arr = new T[size];
//    length = size;
//    for (int i = 0; i < length; i++) {
//        array[i]  = set(nullptr, i);
//    }
//}
//
//template <class T>
//quicksort<T>::quicksort(int size) {
//    srand(time(NULL));
//    array = new T[size];
//    length = size;
//    for (int i = 0; i < length; i++) {
//        array[i]  = 0;
//    }
//}

template <class T>
quicksort<T>::quicksort(int size) {
    srand(time(NULL));
    array = new int[size];
    length = size;
    for (int i = 0; i < length; i++) {
        array[i]  = rand() % 10000 + 1;
    }
}
template <class T>
quicksort<T>::~quicksort() {
    if (array != NULL) {
        delete [] array;
    }
}

template <class T>
void quicksort<T>::set(T n, int id){
    if (id < length) {
        array[id] = n;
    }
}

template <class T>
void quicksort<T>::sort() {
    sort(array, 0, length-1);
}

template <class T>
void quicksort<T>::sort(T *arr, int left, int right) {
    int i = left, j = right;
    int tmp;
    T pivot = arr[(left + right) / 2];

    /* partition */
    while (i <= j) {
        while (arr[i] < pivot)
            i++;
        while (arr[j] > pivot)
            j--;
        if (i <= j) {
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    };

    /* recursion */
    if (left < j)
        sort(arr, left, j);
    if (i < right)
        sort(arr, i, right);
}

template <class T>
void quicksort<T>::print() {
    for (int i = 0; i<length;i++) {
        std::cout<<array[i]<<" ";
    }
    std::cout<<"\n";
}

template class quicksort<int>;
