class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph= defaultdict(list)
        for v,u in edges:
            graph[v].append(u)
            graph[u].append(v)
        
        visited=set()
        connected=0
        curr_visited=len(visited)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        for i in range(n):
            dfs(i)
            if len(visited)>curr_visited:
                curr_visited=len(visited)
                connected+=1
        return connected