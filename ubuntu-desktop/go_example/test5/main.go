package main

import (
    "fmt"
    "sort"
)

func main() {
    numbers := []int{5, 2, 8, 3, 1, 6, 4, 7}
    fmt.Println("Unsorted numbers:", numbers)
    sort.Ints(numbers)
    fmt.Println("Sorted numbers:", numbers)
}
