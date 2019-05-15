package main

import (
	"fmt"
	"github.com/MarkWh1te/algo4go"
)

func randomSlice(upper int) []int {
	length := random(10, upper)
	// use slice because length is not a constant
	result := make([]int, length)
	for index := 0; index < length; index++ {
		result[index] = random(1, upper)
	}
	return result
}

func main() {
	const UPPER int = 13
	test := randomSlice(UPPER)
	length := len(test)
	QuickSort(&test, 0, len(test)-1)
	fmt.Println(test)
}
