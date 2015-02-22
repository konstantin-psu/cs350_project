#include "heapsort.cpp"
#include <iostream>

using namespace std;

int main() {

    cout << "Hello, World!" << endl;
    heapsort<int> hSort(100);
    /*printArray(array, size);
    buildHeap(array, size);
    heapSort(array, size);
    printArray(array, size);*/
    hSort.sort();

    return 0;
}
