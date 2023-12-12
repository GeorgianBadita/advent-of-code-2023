#include <iostream>
#include<vector>
#include<fstream>
#include<queue>

#define NMAX 141
#define INF 1ULL << 32

using std::vector;
using std::string;
using std::ifstream;
using std::ofstream;
using std::pair;
using std::queue;

typedef unsigned long long resType;

resType dist[NMAX][NMAX];
bool linesToAugment[NMAX];
bool colsToAugment[NMAX];

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

auto cmp = [](pair<pair<int, int>, resType> left, pair<pair<int, int>, resType> right) { return left.second < right.second; };
typedef std::priority_queue<pair<pair<int, int>, resType>, std::vector<pair<pair<int, int>, resType>>, decltype(cmp)> PriorityQueue;



bool validCoords(int x, int y, vector<string>& map) {
    return x >= 0 && x < map.size() && y >= 0 && y < map[0].size();
}

void dijkstra(pair<int, int> start, vector<string>& map, bool* lines, bool* cols, int factor) {
    int dx[] = {0, 0, -1, 1};
    int dy[] = {-1, 1, 0, 0};

    for(int idx = 0; idx < NMAX; idx++) {
        for(int jdx = 0; jdx < NMAX; jdx++) {
            dist[idx][jdx] = INF;
        }
    }

    dist[start.first][start.second] = 0ULL;
    auto bfsQueue = PriorityQueue(cmp);
    bfsQueue.emplace(start, dist[start.first][start.second]);


    while(!bfsQueue.empty()) {
        auto next = bfsQueue.top();
        bfsQueue.pop();
        int nx = next.first.first, ny = next.first.second;
        resType dst = next.second;

        if(dist[nx][ny] != dst) {
            continue;
        }

        if((dist[nx][ny] == 0 && nx != start.first && ny != start.second) || dist[nx][ny] < 0) {
            throw "IEEEEE";
        }

        for(int d = 0; d < 4; d++) {
            int newX = nx + dx[d];
            int newY = ny + dy[d];

            if(validCoords(newX, newY, map)) {
                resType cost = 1ULL;

                if(linesToAugment[newX]) {
                    cost = factor;
                }

                if(colsToAugment[newY]) {
                    cost = factor;
                }

                if(dist[nx][ny] + cost < dist[newX][newY]) {
                    dist[newX][newY] = 1LL*dist[nx][ny] + 1LL*cost;
                    bfsQueue.push({{newX, newY}, dist[newX][newY]});
                }
            }
        }
    }
}

resType solve(vector<string> map, int factor) {
    auto galaxies = vector<pair<int, int>>{};
    for(int idx = 0; idx < map.size(); idx++) {
        for(int jdx = 0; jdx < map.size(); jdx++) {
            if(map[idx][jdx] == '#') {
                galaxies.push_back({idx, jdx});
            }
        }
    }

    for(int idx = 0; idx < NMAX; idx++){
        linesToAugment[idx] = false;
    }

    for(int idx = 0; idx < NMAX; idx++) {
        colsToAugment[idx] = false;
    }

    for(int idx = 0; idx < map.size(); idx++) {
        int diffChars = 0;
        for(int jdx = 0; jdx < map[0].size() - 1; jdx++) {
            if(map[idx][jdx] != map[idx][jdx + 1]) {
                diffChars += 1;
            }
        }
        if(diffChars == 0) {
            linesToAugment[idx] = true;
        }
    }

    for(int jdx = 0; jdx < map[0].size(); jdx++) {
        int diffChars = 0;
        for(int idx = 0; idx < map.size() - 1; idx++) {
            if(map[idx][jdx] != map[idx + 1][jdx]) {
                diffChars += 1;
            }
        }
        if(diffChars == 0) {
            colsToAugment[jdx] = true;
        }
    }

    resType res = 0ULL;
    for(int idx = 0; idx < galaxies.size() - 1; idx++) {
        std::cout << "Processing " << idx << " out of: " << galaxies.size() - 1 << '\n';
        dijkstra(galaxies[idx], map, linesToAugment, colsToAugment, factor);
        for(int jdx = idx + 1; jdx < galaxies.size(); jdx++) {
            res += dist[galaxies[jdx].first][galaxies[jdx].second];
        }
    }

    return res;
}

int main() {
    auto filePath = "./in-day11.txt";

    auto map = readFile(filePath);

    std::cout << solve(map, 1000000);
    return 0;
}