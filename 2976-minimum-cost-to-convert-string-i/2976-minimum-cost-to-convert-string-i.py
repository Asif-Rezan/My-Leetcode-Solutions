class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        INF = 10**15
        N = 26
        
        # Distance matrix for characters a-z
        dist = [[INF] * N for _ in range(N)]
        
        # Cost to convert same character is 0
        for i in range(N):
            dist[i][i] = 0
        
        # Fill direct transformation costs
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        # Floyd-Warshall to compute all-pairs shortest paths
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Calculate total cost
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            
            if dist[u][v] == INF:
                return -1
            
            total_cost += dist[u][v]
        
        return total_cost
