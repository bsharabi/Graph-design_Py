# from api.GraphAlgoInter import GraphAlgoInterface
from api.GraphInter import GraphInterface
from Departments.Graph import DiGraph
from typing import List
import json


class GraphAlgo:
    ''''''

    def __init__(self, graph: GraphInterface = DiGraph()) -> None:
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            graph = open(file_name)
        except OSError:
            print("Could not read file:", file_name)
            return False
        with graph:
            self.graph = DiGraph()
            data = json.load(graph)
            for node in data["Nodes"]:
                id = int(node["id"])
                if "pos" in node:
                    s = node["pos"].split(',')
                    pos = (float(s[0]), float(s[1]), float(s[2]))
                    self.graph.add_node(id, pos)
                else:
                    self.graph.add_node(id)
            for edge in data["Edges"]:
                id1 = int(edge["src"])
                id2 = int(edge["dest"])
                weight = float(edge["w"])
                self.graph.add_edge(id1, id2, weight)
            graph.close()
            return True

    def save_to_json(self, file_name: str) -> bool:
        '''Function responsible for writing the results in the output file received at the command prompt '''
        try:
            graphWrite = open("data\\"+file_name+".json", 'w')
        except IOError:
            print("Could not write file:", file_name)
            return False
        with graphWrite:
            js = self.graph.getJsonGraph()
            json.dump(js, graphWrite)
            graphWrite.close()
            return True

    def shortest_path(self, id1: int, id2: int):
        
        return None

    def TSP(self, node_lst: List[int]):
        pass

    def centerPoint(self):
        pass

    def plot_graph(self) -> None:

        raise NotImplementedError

    def __repr__(self):
        return f"{self.graph}"
