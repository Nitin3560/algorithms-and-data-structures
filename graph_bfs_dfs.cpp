#include <iostream>
#include <stdexcept>

class DynamicArray {
private:
    int* arr;       
    int size;       
    int capacity;   
   
    void resize() {
        capacity *= 2; 
        int* newArr = new int[capacity];  

        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }
        delete[] arr; 
        arr = newArr;  
    }

public:
    DynamicArray() {
        size = 0;
        capacity = 2;  
        arr = new int[capacity]; 
    }

    ~DynamicArray() {
        delete[] arr; 
    }

    void push_back(int value) {
        if (size == capacity) {
            resize(); 
        }
        arr[size++] = value; 
    }

    int get(int index) const {
        if (index >= size || index < 0) {
            throw std::out_of_range("Index out of bounds");
        }
        return arr[index];
    }

    int get_size() const {
        return size;
    }

    bool empty() const {
        return size == 0;
    }

    void pop_back() {
        if (size > 0) {
            size--; 
        }
    }
};

int main() {
    DynamicArray arr;
    arr.push_back(10);
    arr.push_back(20);
    arr.push_back(30);

    std::cout << "Array size: " << arr.get_size() << std::endl;
    std::cout << "Element at index 1: " << arr.get(1) << std::endl;

    arr.pop_back();
    std::cout << "Array size after pop_back: " << arr.get_size() << std::endl;

    return 0;
}
