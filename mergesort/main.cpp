#include "mergesort.cpp"
#include <iostream>

using namespace std;

int main() {

    cout << "Hello, World!" << endl;
    mergesort<int> mSort(2000000000);
    mSort.sort();
    cout << "Goodbye" << endl;

    return 0;
}
