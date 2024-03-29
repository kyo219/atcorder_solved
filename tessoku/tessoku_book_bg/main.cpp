#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


std::pair<int64_t, int64_t> solve(int64_t a, int64_t b, int64_t c, int d, int64_t e, const std::vector<int64_t> &f, const std::vector<int64_t> &g, const std::vector<int64_t> &h) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t a, b, c;
    int d;
    int64_t e;
    std::cin >> a >> b >> c >> d;
    std::vector<int64_t> f(d), g(d), h(d);
    std::cin >> e;
    REP (i, d) {
        std::cin >> f[i] >> g[i] >> h[i];
    }
    auto [m, n] = solve(a, b, c, d, e, f, g, h);
    std::cout << m << ' ' << n << '\n';
    return 0;
}
