package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	str := string(data)
	lines := strings.Split(str, "\n")
	dictionary := make(map[string]int)
	for _, line := range lines {
		dictionary[line] = 1
	}
	fmt.Println(str)
}
