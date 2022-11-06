def solution(n):
    list = [None]*(n+1)
    for i in range(n+1):
        list[i] = [None]*(n+1)
        for j in range(n+1):
            list[i][j] = 0
    
    list[0][0] = 1
    for i in range(1, n+1):
        for j in range(n+1):
            list[i][j] = list[i-1][j]
            if j >= i:
                list[i][j] += list[i-1][j-i]
    return list[n][n] - 1


# print(solution(200))