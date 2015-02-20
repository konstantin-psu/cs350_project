#include "mergesort.cpp"
#include <iostream>

using namespace std;

int main() {

    cout << "Hello, World!" << endl;
    mergesort<int> mSort(100);
    mSort.sort();

    return 0;
}
