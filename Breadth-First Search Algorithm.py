from queue import Queue
adj_list={
    "A":["B","J","G"],
    "B":["A","D"],
    "C":["H"],
    "D":["B","J","H"],
    "E":["G","F","I"],
    "F":["G","E","I","H"],
    "G":["A","J","F","E"],
    "H":["D","F","I","C"],
    "I":["E","F","H"],
    "J":["A","B","D","G"]

}
visited={}
level={}
parent={}
bfs_traversal_output=[]
queue= Queue()
for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]= -1
s="A"
visited[s]= True
level[s]= 0
queue.put(s)
while not queue.empty():
    u= queue.get() #pop the first element of the queue
    bfs_traversal_output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)
print(bfs_traversal_output)
print(level)
print(level["D"])
v="C" #if initial is A and C is the goal then 
path=[]
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(path)
