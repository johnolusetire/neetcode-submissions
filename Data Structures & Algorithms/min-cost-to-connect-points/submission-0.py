class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Using prim array version

        N = len(points)
        visited = [0] * N
        min_dist = [float("inf")] * N
        min_dist[0] = 0
        total = 0
        node = 0

        def manhattan(n1, n2):
            return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

        for _ in range(N-1):
            visited[node] = 1
            u = -1
            for i in range(N):
                if not visited[i]:
                    min_dist[i] = min(min_dist[i], manhattan(points[node], points[i]))
                    if u == -1 or min_dist[i] < min_dist[u]:
                        u = i

            
            total += min_dist[u]
            node = u
                   
        return total

        