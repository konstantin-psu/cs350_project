cmake_minimum_required(VERSION 2.8.4)
project(quicksort)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pg")

set(SOURCE_FILES quicksort.cpp main.cpp)
add_executable(quicksort ${SOURCE_FILES})