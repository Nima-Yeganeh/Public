#include <iostream>

int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n-1);
    }
}

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    int result = factorial(n);
    std::cout << "The factorial of " << n << " is " << result << std::endl;
    return 0;
}
