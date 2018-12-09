package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"strconv"
)

type Node struct {
	name        string
	child_names []string
	metadata    []int
	value       int
}

var nodes []Node

var numbers []int
var metas []int

func main() {

	//Read and parse input
	r, _ := ioutil.ReadFile("input.txt")
	//Remove trailing newline
	r = r[:len(r)-1]

	space := []byte{' '}
	data := bytes.Split(r, space)
	for _, n := range data {
		number, _ := strconv.Atoi(string(n))
		numbers = append(numbers, number)
	}

	//Solve the problems
	solve_node(byte('A'), numbers)

	fmt.Printf("PART 1: %d\n", sliceSum(metas))
	fmt.Printf("PART 2: %d\n", nodes[len(nodes)-1].value)

}

func solve_node(node_name byte, node []int) ([]int, int) {
	var (
		node_children    = node[0]
		node_child_names = []string{}
		node_metadatas   = node[1]
		node_metadata    = []int{}
		node_value       int
		child_value      int
		child_values     []int
	)

	//remove header
	node = node[2:]

	for i := 1; i <= node_children; i++ {
		child_name := node_name + byte(i)
		node_child_names = append(node_child_names, string(child_name))
		node, child_value = solve_node(child_name, node)
		child_values = append(child_values, child_value)
	}

	for i := 0; i < node_metadatas; i++ {
		metas = append(metas, node[i])
		node_metadata = append(node_metadata, node[i])
	}

	if node_metadatas > 0 {
		node = node[node_metadatas:]
	}

	if len(child_values) == 0 {
		node_value = sliceSum(node_metadata)
	} else {
		for _, m := range node_metadata {
			if m >= 1 && m <= len(child_values) {
				node_value = node_value + child_values[m-1]
			}
		}
	}

	nodes = append(nodes, Node{
		name:        string(node_name),
		child_names: node_child_names,
		metadata:    node_metadata,
		value:       node_value,
	})

	return node, node_value
}

func sliceSum(slice []int) int {
	result := 0
	for _, n := range slice {
		result = result + n
	}
	return result
}
