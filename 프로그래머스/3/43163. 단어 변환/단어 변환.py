from collections import deque

def solution(begin, target, words):
    step = 0
    if target not in words:
        return 0
    
    q = deque([(begin, step)])
    visited = []
    
    while q:
        curWord, step = q.popleft()
        if curWord == target:
            return step
        
        for word in words:
            if word in visited:
                continue
            cnt = 0
            for i in range(len(begin)):
                if curWord[i] == word[i]:
                    cnt += 1
            
            if cnt == len(begin) - 1:
                q.append((word, step+1))
                visited.append(word)
    
    return step