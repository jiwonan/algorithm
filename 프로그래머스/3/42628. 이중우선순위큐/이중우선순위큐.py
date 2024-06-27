def solution(operations):
    answer = []
    queue = []
    for operation in operations:
        op, num = operation.split()
        
        if op == "I":
            queue.append(int(num))
            queue.sort()
        elif len(queue) > 0:
            if int(num) == -1:
                queue.pop(0)
            else:
                queue.pop()
    
    if len(queue) <= 0:
        return [0,0]
    else:
        return [max(queue), min(queue)]
            
    
    return answer