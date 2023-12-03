#include <iostream>
#include<vector>
#include<fstream>

using std::vector;
using std::string;
using std::ifstream;
using std::ofstream;

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

int solve(vector<string> engineScheme) {
    int dx[] = {-1, 1, 1, -1, 0, 0, 1, -1};
    int dy[] = {1, -1, 1, -1, 1, -1, 0, 0};
    int sum = 0;

    for(int idx = 0; idx < engineScheme.size(); idx++) {
        int jdx = 0;
        while (jdx < engineScheme[idx].size()) {
            if (engineScheme[idx][jdx] >= '0' && engineScheme[idx][jdx] <= '9') {
                int num = 0;
                bool hasSymbol = false;
                while(validCoords(engineScheme, idx, jdx) && engineScheme[idx][jdx] >= '0' && engineScheme[idx][jdx] <= '9') {
                    num = num * 10 + (engineScheme[idx][jdx]  - '0');
                    for(int dir = 0; dir < 8; dir++) {
                        int newIdx = idx + dx[dir];
                        int newJdx = jdx + dy[dir];
                        if(validCoords(engineScheme, newIdx, newJdx) && // valid coordinates
                        engineScheme[newIdx][newJdx] != '.' // it's not '.'
                        && (engineScheme[newIdx][newJdx] < '0' || engineScheme[newIdx][newJdx] > '9')) { // it's not digit
                            hasSymbol = true;
                        }
                    }
                    jdx += 1;
                }
                if(hasSymbol) {
                    sum += num;
                }
            } else {
                jdx += 1;
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
