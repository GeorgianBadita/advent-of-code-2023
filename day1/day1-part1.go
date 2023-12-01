package main

import (
	"bufio"
	"os"
	"unicode"
)

func readFromFile(filePath string) ([]string, error) {
	file, err := os.Open(filePath)

	if err != nil {
		return nil, err
	}

	scanner := bufio.NewScanner(file)

	res := []string{}

	for scanner.Scan() {
		line := scanner.Text()
		res = append(res, line)
	}

	return res, nil
}

func solve(doc []string) uint64 {
	res := uint64(0)

	for _, line := range doc {
		firstDigPos := 0
		for p, rn := range line {
			if unicode.IsDigit(rn) {
				firstDigPos = p
				break
			}
		}

		lastDigitPos := len(line) - 1
		for idx := len(line) - 1; idx >= 0; idx-- {
			if unicode.IsDigit(rune(line[idx])) {
				lastDigitPos = idx
				break
			}
		}

		firstDig := uint64(line[firstDigPos] - '0')
		secondDig := uint64(line[lastDigitPos] - '0')

		num := (firstDig*10 + secondDig)
		res += num
	}
	return res
}

func main() {
	path := "./in-day1.txt"

	doc, err := readFromFile(path)

	if err != nil {
		panic(err)
	}

	println(solve(doc))
}
