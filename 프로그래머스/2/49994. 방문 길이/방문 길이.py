def solution(steps):
    x, y = 0, 0
    visited = set()
    for k in steps:
        if k == 'U':
            nx, ny = x, y + 1 
        elif k == 'D':
            nx, ny = x, y - 1
        elif k == 'R':
            nx, ny = x + 1, y 
        elif k == 'L':
            nx, ny = x -1 , y
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x,y,nx,ny)) 
            visited.add((nx,ny,x,y))
            x, y = nx, ny
    return len(visited)//2