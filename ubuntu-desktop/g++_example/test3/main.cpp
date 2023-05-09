#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    std::vector<int> numbers = {5, 2, 8, 3, 1, 6, 4, 7};
    std::cout << "Unsorted numbers:";
    for (int n : numbers) {
        std::cout << " " << n;
    }
    std::cout << std::endl;
    std::sort(numbers.begin(), numbers.end());
    std::cout << "Sorted numbers:";
    for (int n : numbers) {
        std::cout << " " << n;
    }
    std::cout << std::endl;
    return 0;
}
