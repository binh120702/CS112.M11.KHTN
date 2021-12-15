# 1561C - Deep Down Below
ts = int(input())

for _ in range(ts): 
    n = int(input())
    max_monster = [[0,0] for _ in range(n)]
    for i in range(n):
        a = [int(x) for x in input().split()]
        max_monster[i][0] = 0;
        max_monster[i][1] = a[0] 
        for j in range(a[0]):
            max_monster[i][0] = max(max_monster[i][0], a[j+1]-j)

    max_monster.sort(key = lambda x : x[0]) 
    hero = 0
    monster_cleared = 0
    for i in range(n):
        max_monster[i][0] -= monster_cleared
        monster_cleared += max_monster[i][1]
        hero = max(hero, max_monster[i][0])
    print(hero + 1)
