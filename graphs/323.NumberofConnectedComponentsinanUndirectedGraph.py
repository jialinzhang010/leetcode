class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = defaultdict(list)
        for x, y in edges:
            hashmap[x].append(y)
            hashmap[y].append(x)
        visited = set()
        count = 0
        for index in range(n):
            if index not in visited:
                self.dfs(index, visited, hashmap)
                count += 1
        return count
    def dfs(self, index, visited, hashmap):
        if index in visited:
            return
        visited.add(index)
        for neighbor in hashmap[index]:
            self.dfs(neighbor, visited, hashmap)