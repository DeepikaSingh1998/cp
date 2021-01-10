class Graph:
    def __init__(self):
        self.v={}

    def add_vertex(self,data):
        if data not in self.v.keys():
            self.v[data]=[]
    
    def add_connectivity(self,src,dest_data):#src is data, 
       self.v[src].append(dest_data)
    
    def print_graph(self):
        for i in self.v.keys():
            s=str(i)+"->"
            x=self.v[i]
            while(i<len(x)):
                s+=str(x[i])+", "
                i+=1
            print(s[:-2])