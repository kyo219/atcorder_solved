#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


auto solve(int D, int64_t X, const std::vector<int64_t> &A, int Q, const std::vector<int64_t> &S, const std::vector<int64_t> &T) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int D;
    int64_t X;
    int Q;
    std::cin >> D;
    std::vector<int64_t> A(D - 1);
    std::cin >> X;
    REP (i, D - 1) {
        std::cin >> A[i];
    }
    std::cin >> Q;
    std::vector<int64_t> S(Q), T(Q);
    REP (i, Q) {
        std::cin >> S[i] >> T[i];
    }
    auto ans = solve(D, X, A, Q, S, T);
    std::cout << n << '\n';
    REP (i, n) {
        std::cout << a[i] << ' ';
    }
    std::cout << '\n';
    REP (i, n) {
        std::cout << b[i] << ' ';
    }
    std::cout << '\n';
    return 0;
}
