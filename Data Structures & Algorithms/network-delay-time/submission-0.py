import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        adj_map = [[] for _ in range(0, n + 1)]
        for src, dest, time in times:
            adj_map[src].append((dest, time))
        
        # Djikstra's create map for best time to node from node k
        node_times = [float("inf")] * (n+1)

        node_times[k] = 0
        min_heap = [(0, k)]

        while min_heap:
            time, node = heapq.heappop(min_heap)


            if time > node_times[node]:
                continue
            
            for neigh, neigh_time in adj_map[node]:
                new_time = time + neigh_time

                if new_time < node_times[neigh]:
                    node_times[neigh] = new_time
                    heapq.heappush(min_heap, (new_time, neigh))
        
        res = max(node_times[1:])
        return res if res != float("inf") else -1
        
