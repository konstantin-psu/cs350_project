#ifndef QUICK_SORT_HPP_
#define QUICK_SORT_HPP_
#include <random>
#include <ctime>
#include <iostream>
template<class T>
class quicksort {
public:
    quicksort();
    //template<int> quicksort(int size);
    quicksort(int size);
    ~quicksort();
    void sort();
    void print();
private:
    void sort(T* arr, int left, int right);
    T* array; //Heap only
    int length;
    void set(T n, int id);

};


#endif
