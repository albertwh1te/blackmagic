package main

import (
	"fmt"
	"sort"
)

func main() {
	test_arr := []int{1, 2, 3, 4}
	fmt.Println(test_arr)
	sort.InsertionSort(test_arr)
	fmt.Println(test_arr)
}
