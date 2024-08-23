# import sys
# input = sys.stdin.readline
    
# from collections import deque
# def bfs(graph, start, visited):
    
#     queue = deque([start])
    
#     visited[start] = True
    
#     while queue:
#         v = queue.popleft()
        
#         print(v, end=' ')
        
#         for i in graph[int(v)]:
#             if not visited[int(i)]:
#                 queue.append(i)
#                 visited[int(i)] = True
                
# def dfs(graph, v, visited):
    
#     visited[v] = True
    
#     print(v, end=' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
            
# node_dfs = [[]]
# node_bfs = [[]]
# info = input()
# info = info.split()
# for _ in range(int(info[1])):
#     s = input()
#     if s.split() == []:
#         break
#     node_dfs.append(s.split())
#     node_bfs.append(s.split())
    
# visited_dfs = [False] * (int(info[0]) + 1)
# visited_bfs = [False] * (int(info[0]) + 1)

# dfs(node_dfs, int(info[2]), visited_dfs)
# print()
# bfs(node_bfs, int(info[2]), visited_bfs)

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited.append(start)
    for node in sorted(graph[start]):
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    
    return visited

def main():
    n, m, v = map(int, input().split())
    
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    
    dfs_result = dfs(graph, v, [])
    bfs_result = bfs(graph, v)
    
    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))

if __name__ == "__main__":
    main()
