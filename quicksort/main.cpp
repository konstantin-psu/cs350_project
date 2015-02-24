#include <iostream>
//#include "hoare.hpp"
#include "quicksort.h"
//#include "lomuto.hpp"

using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    quicksort<int> qsort(2000000000);
    qsort.sort();
    //quicksort<int> qsort = quicksort<int>(10);
    cout << "Goodbye" << endl;
    return 0;
}
