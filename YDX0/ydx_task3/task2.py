import sys
import numpy as np
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
image = np.array([list(map(int, list(input().strip()))) for _ in range(n)])
t = int(input())
exceptions = {}
for _ in range(t):
    a, b, c = map(int, input().split())
    exceptions[(a, b)] = c
    exceptions[(b, a)] = c

max_sum = 9 * k
INF = 10**18

penalty = np.array([[(i - j) ** 2 for j in range(10)] for i in range(10)])
for (a, b), c in exceptions.items():
    penalty[a][b] = penalty[b][a] = c

prev_dp = np.full((10, max_sum + 1, 10), INF)
for start in range(10):
    if start <= max_sum:
        prev_dp[start, start, start] = 0

for length in range(1, k):
    curr_dp = np.full((10, max_sum + 1, 10), INF)
    for st in range(10):
        dp_st = prev_dp[st]
        curr_st = curr_dp[st]
        for s in range(max_sum + 1):
            last_costs = dp_st[s]
            for last in range(10):
                cost_here = last_costs[last]
                if cost_here == INF:
                    continue
                penalty_last = penalty[last]
                for nxt in range(10):
                    ns = s + nxt
                    if ns > max_sum:
                        continue
                    cost_next = cost_here + penalty_last[nxt]
                    if cost_next < curr_st[ns, nxt]:
                        curr_st[ns, nxt] = cost_next
    prev_dp = curr_dp

def get_block_cost(p, start, end):
    target_sum = p * k
    if target_sum > max_sum:
        return INF
    return prev_dp[start, target_sum, end]

min_block_cost = np.full(10, INF)
for p in range(10):
    target_sum = p * k
    if target_sum > max_sum:
        continue
    costs = prev_dp[:, target_sum, :].flatten()
    min_block_cost[p] = costs.min()

total_penalty = 0

for row in image:
    m = len(row)
    best_cost = {}
    heap = []


    p0 = row[0]
    for st in range(10):
        for en in range(10):
            c = get_block_cost(p0, st, en)
            if c < INF:
                f_cost = c + sum(min_block_cost[row[j]] for j in range(1, m))
                state = (0, en)
                if best_cost.get(state, INF) > c:
                    best_cost[state] = c
                    heapq.heappush(heap, (f_cost, c, 0, en))

    ans = INF

    while heap:
        f_cost, cost, pos, end_digit = heapq.heappop(heap)

        if pos == m-1:
            ans = cost
            break

        if best_cost.get((pos, end_digit), INF) < cost:
            continue

        p_next = row[pos + 1]

        penalty_prev_end = penalty[end_digit]

        for st_next in range(10):
            conn_cost = penalty_prev_end[st_next]
            target_sum = p_next * k
            if target_sum > max_sum:
                continue
            curr_dp_st = prev_dp[st_next]
            for en_next in range(10):
                block_cost_val = curr_dp_st[target_sum, en_next]
                if block_cost_val == INF:
                    continue
                new_cost = cost + conn_cost + block_cost_val
                state_next = (pos + 1, en_next)
                if best_cost.get(state_next, INF) > new_cost:
                    best_cost[state_next] = new_cost
                    heur = sum(min_block_cost[row[j]] for j in range(pos + 2, m))
                    heapq.heappush(heap, (new_cost + heur, new_cost, pos + 1, en_next))

    total_penalty += ans

print(total_penalty)
