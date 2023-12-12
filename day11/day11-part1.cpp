#include <iostream>
#include<vector>
#include<fstream>
#include<queue>

using std::vector;
using std::string;
using std::ifstream;
using std::ofstream;
using std::pair;
using std::queue;

vector<string> readFile1(string filePath) {
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

vector<string> rotateMap1(vector<string>& map) {
    auto newMap = vector<string>{};
    for(int jdx = 0; jdx < map[0].size(); jdx++) {
        auto line = string {};
        for(int idx = 0; idx < map.size(); idx++) {
            line += map[idx][jdx];
        }
        newMap.emplace_back(line);
    }
    return newMap;
}

vector<string> extendGalaxyLines1(vector<string>& map) {
    auto linesToAugment = vector<int>{};

    for(int idx = 0; idx < map.size(); idx++) {
        int diffChars = 0;
        for(int jdx = 0; jdx < map[0].size() - 1; jdx++) {
            if(map[idx][jdx] != map[idx][jdx + 1]) {
                diffChars += 1;
            }
        }
        if(diffChars == 0) {
            linesToAugment.push_back(idx);
        }
    }

    auto newMap = vector<string>{};
    auto posInLine = 0;

    for(int idx = 0; idx < map.size(); idx++) {
        if(idx == linesToAugment[posInLine]) {
            posInLine += 1;
            newMap.push_back(map[idx]);
            newMap.push_back(map[idx]);
        } else {
            newMap.push_back(map[idx]);
        }
    }

    return newMap;
}

pair<vector<string>, vector<pair<int, int>>> extendGalaxy1(vector<string>& map) {
    // This can be done way better or avoided altogether, but I'm in a rush rn
    auto newMap = extendGalaxyLines1(map);
    newMap = rotateMap1(newMap);
    newMap = extendGalaxyLines1(newMap);
    newMap = rotateMap1(newMap);
    newMap = rotateMap1(newMap);
    newMap = rotateMap1(newMap);

    auto galaxies = vector<pair<int, int>> {};

    for(int idx = 0; idx < newMap.size(); idx++) {
        for(int jdx = 0; jdx < newMap[0].size(); jdx++) {
            if(newMap[idx][jdx] == '#') {
                galaxies.emplace_back(idx, jdx);
            }
        }
    }

    return {newMap, galaxies};
}

bool validCoords1(int x, int y, vector<string>& map) {
    return x >= 0 && x < map.size() && y >= 0 && y < map[0].size();
}

int bfs1(pair<int, int> start, pair<int, int> dest, vector<string>& map, vector<vector<bool>> visited) {
    auto bfsQueue = queue<pair<pair<int, int>, int>>{};
    bfsQueue.emplace(start, 0);
    visited[start.first][start.second] = true;

    int dx[] = {0, 0, -1, 1};
    int dy[] = {-1, 1, 0, 0};

    while(!bfsQueue.empty()) {
        auto next = bfsQueue.front();
        bfsQueue.pop();

        int nx = next.first.first, ny = next.first.second, lvl = next.second;

        if(nx == dest.first && ny == dest.second) {
            return lvl;
        }

        for(int d = 0; d < 4; d++) {
            int newX = nx + dx[d];
            int newY = ny + dy[d];

            if(validCoords1(newX, newY, map) && !visited[newX][newY]) {
                visited[newX][newY] = true;
                bfsQueue.push({{newX, newY}, lvl + 1});
            }
        }
    }

    return -1;
}

int solve1(vector<string> map,  vector<pair<int, int>> galaxies) {
    auto visited = vector<vector<bool>>{};
    for(int idx = 0; idx < map.size(); idx++) {
        auto line = vector<bool>{};
        for(int jdx = 0; jdx < map[0].size(); jdx++) {
            line.push_back(false);
        }
        visited.push_back(line);
    }

    int res = 0;
    for(int idx =0; idx < galaxies.size() - 1; idx++) {
        std::cout << "Processed: " << idx << " out of " << galaxies.size() - 1 << '\n';
        for(int jdx = idx + 1; jdx < galaxies.size(); jdx++) {
            res += bfs1(galaxies[idx], galaxies[jdx], map, visited);
        }
    }

    return res;
}

int main1() {
    auto filePath = "./in-day11.txt";

    auto map = readFile1(filePath);

    auto mapAndGalaxies = extendGalaxy1(map);

    std::cout << solve1(mapAndGalaxies.first, mapAndGalaxies.second);
    return 0;
}