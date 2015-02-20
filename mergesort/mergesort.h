#include <random>
#include <ctime>
#include <iostream>

template<class T>
class mergesort {
public:
    mergesort();
    mergesort(int size);
    ~mergesort();
    void merge(T begin, T middle, T end, T* result);
    void sort();
    void print();

private:
    void sort(T begin, T end, T* result);
    T* array;
    int length;
};