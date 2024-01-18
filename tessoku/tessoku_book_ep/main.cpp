#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

const std::string YES = "Yes";
const std::string NO = "No";
bool solve(auto N, auto M, const std::vector<std::vector<auto> > &C) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    auto N, M;
    std::cin >> N;
    std::vector<std::vector<auto> > C(N + 28, std::vector<auto>((N + 28)));
    std::cin >> M;
    REP (j, N + 4) {
        REP (i, 24) {
            std::cin >> C[i + j][i + j];
        }
    }
    auto ans = solve(N, M, C);
    std::cout << (ans ? YES : NO) << '\n';
    return 0;
}