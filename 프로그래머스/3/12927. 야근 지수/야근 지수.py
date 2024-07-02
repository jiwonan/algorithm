import heapq

def solution(n, works):
    answer = 0
    heap_list = []
    
    for work in works:
        heapq.heappush(heap_list, work * -1)
    
    for _ in range(n):
        value = heapq.heappop(heap_list)
        if value == 0:
            break
        value += 1
        heapq.heappush(heap_list, value)
    
    for work in heap_list:
        answer += (work * work)
    
    return answer