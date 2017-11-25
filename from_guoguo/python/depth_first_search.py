# encoding=utf-8 
"""
python graph algorithms
"""

a, b, c, d, e, f, g, h = range(8) 
N = [ 
    {b, c, d, e, f},    # a 
    {c, e},             # b 
    {d},                # c 
    {e},                # d 
    {f},                # e 
    {c, g, h},          # f 
    {f, h},             # g 
    {f, g}              # h 
] 
def rec_dfs(G,s,S= None):
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        rec_dfs(G,u,S)

def iter_dfs(G, s): 
    S, Q = set(), []                            # Visited-set and queue 
    Q.append(s)                                 # We plan on visiting s 
    while Q:                                    # Planned nodes left? 
        u = Q.pop()                             # Get one 
        if u in S: continue                     # Already visited? Skip it 
        S.add(u)                                # We've visited it now 
        Q.extend(G[u])                          # Schedule all neighbors 
        yield u                                 # Report u as visited 


def walk(G,s,S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u
    return P

def component(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen:
            continue
        C = walk(G,u)
        seen.update(C)
        comp.append(C)
    return comp
print(N)
print(list(iter_dfs(N,0)))
print(walk(N,0))