#include <iostream>
#include <fstream>

int main() {
    // Open input file
    std::ifstream infile("input.txt");
    if (!infile.is_open()) {
        std::cerr << "Error: could not open input file" << std::endl;
        return 1;
    }

    // Open output file
    std::ofstream outfile("output.txt");
    if (!outfile.is_open()) {
        std::cerr << "Error: could not open output file" << std::endl;
        return 1;
    }

    // Copy data from input file to output file
    std::string line;
    while (std::getline(infile, line)) {
        outfile << line << std::endl;
    }

    // Close files
    infile.close();
    outfile.close();

    return 0;
}
