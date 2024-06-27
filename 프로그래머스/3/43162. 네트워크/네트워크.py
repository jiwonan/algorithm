def solution(n, computers):
    network = defineNetwork(n, computers)
    return count(network, n)

def count(network, n):
    visited = [False for _ in range(n)]
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        queue = []
        queue.append(i)
        cnt += 1
        while len(queue) > 0:
            com = queue.pop(0)
            for j in network[com]:
                if visited[j]:
                    continue
                visited[j] = True
                queue.append(j)
    
    return cnt
    


def defineNetwork(n, computers):
    network = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            if computers[i][j] == 1 and i != j:
                temp.append(j)
        network.append(temp)
    
    return network