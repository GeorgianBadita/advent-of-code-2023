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

func containsStartingFrom(line string, idx int, toFind string) bool {
	toFindCnt := 0
	for toFindCnt < len(toFind) {
		if idx+toFindCnt >= len(line) || line[idx+toFindCnt] != toFind[toFindCnt] {
			return false
		}
		toFindCnt += 1
	}

	return true
}

func solve(doc []string) uint64 {
	res := uint64(0)

	digits := map[string]uint64{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}

	for _, line := range doc {
		firstDig := uint64(0)
		found := false
		for idx, rn := range line {
			if found {
				break
			}

			if unicode.IsDigit(rn) {
				firstDig = uint64(rn - '0')
				found = true
			} else {
				for k, v := range digits {
					if containsStartingFrom(line, idx, k) {
						firstDig = v
						found = true
						break
					}
				}
			}
		}

		found = false
		secondDig := uint64(0)
		for idx := len(line) - 1; idx >= 0; idx-- {
			if found {
				break
			}

			rn := rune(line[idx])
			if unicode.IsDigit(rn) {
				secondDig = uint64(rn - '0')
				found = true
			} else {
				for k, v := range digits {
					if containsStartingFrom(line, idx, k) {
						secondDig = v
						found = true
						break
					}
				}
			}
		}

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
