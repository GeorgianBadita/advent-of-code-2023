#include <iostream>
#include<vector>
#include<fstream>

using std::vector;
using std::string;
using std::ifstream;
using std::ofstream;
using std::pair;

vector<string> readFile(string filePath) {
    auto result = vector<string>{};
    ifstream f(filePath);
    string line;
    if(f.is_open()) {
        while(getline(f, line)) {
            result.push_back(line);
        }
    }
    return result;
}

bool validCoords(vector<string> engineScheme, int idx, int jdx) {
    return idx >= 0 && idx < engineScheme.size() && jdx >= 0 && jdx < engineScheme[idx].size();
}

pair<unsigned long long, int> parseNum(vector<string> &engineScheme, int idx, int jdx) {
    while(validCoords(engineScheme, idx, jdx)
        && engineScheme[idx][jdx] >= '0'
        && engineScheme[idx][jdx] <= '9') {
        jdx -= 1;
    }
    jdx = std::max(jdx, 0);

    if(engineScheme[idx][jdx] < '0' || engineScheme[idx][jdx] > '9') {
        jdx += 1;
    }

    unsigned long long num = 0;
    while(validCoords(engineScheme, idx, jdx)
          && engineScheme[idx][jdx] >= '0'
          && engineScheme[idx][jdx] <= '9') {
        num = num * 10 + (engineScheme[idx][jdx] - '0');
        engineScheme[idx][jdx] = '.';
        jdx += 1;
    }
    if(jdx == engineScheme[idx].size()) {
        jdx -= 1;
    }
    return {num, jdx};
}

unsigned long long solve(vector<string> engineScheme) {
    int dx[] = {-1, 1, 1, -1, 0, 0, 1, -1};
    int dy[] = {1, -1, 1, -1, 1, -1, 0, 0};
    unsigned long long sum = 0;

    for(int idx = 0; idx < engineScheme.size(); idx++) {
        for(int jdx = 0; jdx < engineScheme[idx].size(); jdx++) {
            if(engineScheme[idx][jdx] == '*') {
                auto adjNumbers = vector<pair<int, int>>{};
                for(int dir = 0; dir < 8; dir++) {
                    int newIdx = idx + dx[dir];
                    int newJdx = jdx + dy[dir];
                    if(validCoords(engineScheme, newIdx, newJdx)
                        && engineScheme[newIdx][newJdx] >= '0'
                        && engineScheme[newIdx][newJdx] <= '9') {
                        auto number = parseNum(engineScheme, newIdx, newJdx);
                        adjNumbers.push_back(number);
                    }
                }
                for(const auto pair: adjNumbers) {
                    auto num = pair.first;
                    auto end = pair.second;
                    while(end >= 0 && num != 0) {
                        engineScheme[idx][end] = num % 10 - '0';
                        end -= 1;
                        num = num / 10;
                    }
                }
                if(adjNumbers.size() == 2) {
                    sum += adjNumbers[0].first * adjNumbers[1].first;
                }
            }
        }
    }
    return sum;
}

int main() {
    auto filePath = "./in-day3.txt";
    auto engineScheme = readFile(filePath);

    std::cout << solve(engineScheme);
    return 0;
}
