#include "heapsort.h"
#include <iostream>
//#include <vector>
#include <cstdlib>
#include <algorithm>


/*
ALGORITHM HeapBottomUp(H [1..n])
//Constructs a heap from elements of a given array
// by the bottom-up algorithm
//Input: An array H [1..n] of orderable items
//Output: A heap H [1..n]
for i ← n/2 downto 1 do
    k ← i; v ← H [k]
    heap ← false
    while not heap and 2 ∗ k ≤ n do
        j ← 2 ∗ k
        if j < n //there are two children
            if H [j ] < H [j + 1] j ← j + 1
        if v ≥ H [j ]
            heap ← true
        else H [k] ← H [j ]; k ← j
    H [k] ← v

* */



template <class T>
heapsort<T>::heapsort() {
    size = 0;

    /*array = nullptr;
    srand(time(NULL));
    length = 0;*/
}



template <class T>
heapsort<T>::heapsort(int length) {
    size = length;
    /*srand(time(NULL));
    array = new int[size];
    length = size;
    for (int i = 0; i < length; i++) {
        array[i] = rand() % 1000 + 1;
    }*/
}


template <class T>
heapsort<T>::~heapsort() {
    /*if (array != NULL) {
        delete [] array;
    }*/
}



template <class T>
void heapsort<T>::sort() {
    int length = size;
    srand(time(NULL));
    T* array = new int[length];

    for (int i = 0; i < length; i++) {
        array[i] = rand() % 1000 + 1;
    }

    //int size = length;
    printArray(array, length);

    if (length > 1) {
        buildHeap(array, length);
        heapSort(array, length);
        printArray(array, length);
    }
}


template <class T>
void heapsort<T>::checkRootNode(T* array, size_t root, size_t size) {
//void heapsort<T>::checkRootNode(size_t root, size_t size) {
    size_t left = 2 * root;
    size_t right = 2 * root + 1;
    if ((left < size) && (array[root] < array[left])) {
        std::swap(array[root], array[left]);
        checkRootNode(array, left, size);
    }

    if (right < size && array[root] < array[right]) {
        std::swap(array[root], array[right]);
        checkRootNode(array, right, size);
    }
}



template <class T>
void heapsort<T>::buildHeap(T *array, size_t size) {
//void heapsort<T>::buildHeap(size_t size) {
    for (size_t i = size/2; i > 0; --i) {
        checkRootNode(array, i, size);
    }
}



template <class T>
//void heapsort<T>::heapSort(size_t size) {
void heapsort<T>::heapSort(T *array, size_t size) {
    while (size > 1) {
        std::swap(array[1], array[size-1]);
        checkRootNode(array, 1, --size);
    }
}



template <class T>
void heapsort<T>::printArray(T* array, size_t size) {
    for (size_t i = 1; i < size; ++i) {
        std::cout << array[i] << ' ';
    }
    std::cout << std::endl;
}



template class heapsort<int>;


