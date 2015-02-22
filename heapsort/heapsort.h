#include <random>
#include <ctime>
#include <iostream>

template<class T>
class heapsort {
public:
    heapsort();
    heapsort(int size);
    ~heapsort();
    void sort();

private:
    void checkRootNode(T *array, size_t root, size_t size);
    void buildHeap(T *array, size_t size);
    void heapSort(T *array, size_t size);
    void printArray(T *array, size_t size);
    //T* array;
    int size;
};