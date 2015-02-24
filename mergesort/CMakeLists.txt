cmake_minimum_required(VERSION 2.8.4)
project(mergesort)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pg")

set(SOURCE_FILES mergesort.cpp main.cpp)
add_executable(mergesort ${SOURCE_FILES})
