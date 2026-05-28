class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph= defaultdict(list)
        for v,u in edges:
            graph[v].append(u)
            graph[u].append(v)
        
        visited=set()
        connected=0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected+=1
        return connected