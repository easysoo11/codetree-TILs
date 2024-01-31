from collections import deque

def eat_sushi():
    for idx, (r, s) in enumerate(zip(rail, seat)):
        if s and s[0][0] in r:
            while s[0][0] in r:
                r.remove(s[0][0])
                s[0][1] -= 1
                if s[0][1] == 0:
                    seat[idx] = []
                    break
            rail[idx] = r


L, Q = map(int, input().split())

t = 0
rail = deque([] for _ in range(L))
seat = [[] for _ in range(L)]
for _ in range(Q):
    com = input().split()
    rail.rotate(int(com[1]) - t)
    t = int(com[1])
    eat_sushi()
    if com[0] == '100':
        rail[int(com[2])].append(com[3])
    elif com[0] == '200':
        seat[int(com[2])].append([com[3], int(com[4])])
    elif com[0] == '300':
        person, sushi = 0, 0
        for s in seat:
            if s:
                person += 1
        for r in rail:
            if r:
                sushi += len(r)

        print(person, sushi)

    eat_sushi()