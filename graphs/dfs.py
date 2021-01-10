#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
from generate import Graph
#from formation import node, Graph
#from bisect import bisect_left as bl                #c++ lowerbound bl(array,element)
#from bisect import bisect_right as br               #c++ upperbound br(array,element)

def depth_first(graph,i,visited,rstack):
    visited[i]=True
    if rstack[i]==True:
        return True
    rstack[i]=True
    j=graph.v[i]
    while(j!=None):
        if rstack[j.vertex]==True:
            return True
        if not visited[j.vertex]:
            depth_first(graph,j.vertex,visited,rstack)
        j=j.next
    return False
    

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    
    graph=Graph()
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(4)
    graph.add_node(3)
    graph.add_node(2)
    graph.add_connectivity(0,1)
    graph.add_connectivity(0,4)
    graph.add_connectivity(1,0)
    graph.add_connectivity(1,4)
    graph.add_connectivity(1,2)
    graph.add_connectivity(1,3)
    graph.add_connectivity(4,0)
    graph.add_connectivity(4,1)
    graph.add_connectivity(4,3)
    graph.add_connectivity(3,4)
    graph.add_connectivity(3,1)
    graph.add_connectivity(3,2)
    graph.add_connectivity(2,1)
    graph.add_connectivity(2,3)
    visited={}
    rstack={}
    for i in range(5):
        visited[i]=rstack[i]=False
    print(depth_first(graph,0,visited,rstack))


#-----------------------------BOSS-------------------------------------!
# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()