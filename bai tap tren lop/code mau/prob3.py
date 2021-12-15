def escape_able(n, k, rooms_with_monsters, corridors):
    # create corridors
    neightbours = [[] for _ in range(n)]
    for edge in corridors:
        neightbours[edge[0]].append(edge[1])
        neightbours[edge[1]].append(edge[0])

    # monsters
    queue = []
    monster_to_this = [n+1]*n

    for monster in rooms_with_monsters:
        monster_to_this[monster] = 0
        queue.append(monster)

    while queue:
        u = queue.pop(0)
        for v in neightbours[u]:
            if monster_to_this[v] == n+1: 
                monster_to_this[v] = monster_to_this[u] + 1
                queue.append(v)
    # hero           
    queue = []
    hero_to_this = [n+1]*n
    hero_to_this[0] = 0
    queue.append(0)

    while queue:
        u = queue.pop(0)
        for v in neightbours[u]:
            if hero_to_this[v] == n+1: 
                hero_to_this[v] = hero_to_this[u] + 1
                queue.append(v)
    
    # check per leaf
    for leaf in range(1,n):
        if len(neightbours[leaf]) == 1: # check if this is a leaf
            if monster_to_this[leaf] > hero_to_this[leaf]:
                return True
    return False


t=int(input())
for _ in range(t):
    input()
    n, k = [int(q) for q in input().split()]
    rooms_with_monsters = [int(q)-1 for q in input().split()]
    corridors = [[int(q)-1 for q in input().split()] for _ in range(n-1)]  
    if escape_able(n, k, rooms_with_monsters, corridors):
        print("YES")
    else:
        print("NO")