#include "mergesort.h"
#include <iostream>
#include <vector>
#include <algorithm>


template <class T>
mergesort<T>::mergesort() {
    array = nullptr;
    srand(time(NULL));
    length = 0;
}


template <class T>
mergesort<T>::mergesort(int size) {
    srand(time(NULL));
    array = new int[size];
    length = size;
    for (int i = 0; i < length; i++) {
        array[i] = rand() % 1000 + 1;
    }
}


template <class T>
mergesort<T>::~mergesort() {
    if (array != NULL) {
        delete [] array;
    }
}



template <class T>
void mergesort<T>::sort() {
    int* sortedArray = new int[length];
    sort(0, length, sortedArray);
}



template <class T>
void mergesort<T>::merge(T begin, T middle, T end, T* result) {
    T a = begin, b = middle, r = 0; //, r = *result;

    while (a < middle && b < end) {
        if (array[a] < array[b])
            result[r++] = array[a++];
        else
            result[r++] = array[b++];
    }

    while (a < middle)
        result[r++] = array[a++];
    while (b < end)
        result[r++] = array[b++];
    while (begin < end)
        array[begin++] = *result++;
}



template <class T>
void mergesort<T>::sort(T begin, T end, T* result) {
    T size = end - begin;
    if (size > 1) {
        T middle = begin + (size / 2);
        sort(begin, middle, result);
        sort(middle, end, result);
        merge(begin, middle, end, result);
    }
}



template <class T>
void mergesort<T>::print() {
    for (int i = 0; i < length; i++) {
        std::cout << array[i] << " ";
    }
    std::cout << "\n";
}



template class mergesort<int>;
template class mergesort<float>;


