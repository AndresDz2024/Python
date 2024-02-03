def C_pairs(T_n, n, k):
    pairs = set()
    for i in range(n):
        for j in range(i+1, n):
            if (T_n[i] + T_n[j]) % k == 0:
                pairs.add((min(T_n[i], T_n[j]), max(T_n[i], T_n[j])))
    return len(pairs)

def proceso_T(T):
    for case in range(T):
        n, k = map(int, input().split())
        T_n = list(map(int, input().split()))
        result = C_pairs(T_n, n, k)
        print("Case {}: {}".format(case+1, result))

T = int(input())
proceso_T(T)        