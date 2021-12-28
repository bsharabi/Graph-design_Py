from Departments.Nodes import Vertex as Node
from typing import DefaultDict, OrderedDict


class DiGraph(object):

    def __init__(self) -> None:
        self.nodeDict = {}
        self.mCount = 0
        self.edge_Size = 0
        self.node_Size = 0

    # runTime O(1)
    def v_size(self) -> int:
        return self.node_Size

    # runTime O(1)
    def e_size(self) -> int:
        return self.edge_Size

    # runTime O(1)
    def get_all_v(self) -> dict:
        return self.nodeDict

    # Average runTime O(1) Worst Case O(n)
    def all_in_edges_of_node(self, id1: int) -> dict:
        try:
            outNode = self.nodeDict[id1]
            return outNode.edgeDictIn
        except KeyError:
            print(f"Key {id1} does not exist in dictionary")
            return dict

    # Average runTime O(1) Worst Case O(n)
    def all_out_edges_of_node(self, id1: int) -> dict:
        try:
            inNode = self.nodeDict[id1]
            return inNode.edgeDictOut
        except KeyError:
            print(f"Key {id1} does not exist in dictionary")
            return dict

    # runTime O(1)
    def get_mc(self) -> int:
        return self.mCount

    # Average runTime O(1) Worst Case O(n)
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodeDict and id2 in self.nodeDict and id1 != id2:
            src_node = self.nodeDict.get(id1)
            dest_node = self.nodeDict.get(id2)
            if id2 not in src_node.edgeDictOut and id1 not in dest_node.edgeDictIn:
                src_node.edgeDictOut[id2] = weight
                dest_node.edgeDictIn[id1] = weight
                self.edge_Size += 1
                self.mCount += 1
                # print(f"edge {id1,id2,weight} was added successfully")
                return True
        # print(f"edge {id1,id2,weight} already exists or one of the nodes dose not exists")
        return False

    # Average runTime O(1) Worst Case O(n)
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.nodeDict:
            self.nodeDict[node_id] = Node(node_id, pos)
            self.mCount += 1
            self.node_Size += 1
            # print(f"node {node_id} was added successfully")
            return True
        # print(f"node {node_id} already exists or one of the nodes dose not exists")
        return False

    # O(k)
    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodeDict:
            node = self.nodeDict.get(node_id)
            for nodeOut in list(node.edgeDictOut):
                self.remove_edge(node_id, nodeOut.id)
            for nodeIn in list(node.edgeDictIn):
                self.remove_edge(nodeIn.id, node_id)
            del self.nodeDict[node_id]
            self.node_Size -= 1
            self.mCount += 1
            # print(f"node id {node_id} was removed successfully")
            return True
        # print(f"node id {node_id} does not exists")
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.nodeDict and node_id2 in self.nodeDict and node_id1 != node_id2:
            src_node = self.nodeDict[node_id1]
            dest_node = self.nodeDict[node_id2]
            if node_id2 in src_node.edgeDictOut and node_id1 in dest_node.edgeDictIn:
                del src_node.edgeDictOut[node_id2]
                del dest_node.edgeDictIn[node_id1]
                self.edge_Size -= 1
                self.mCount += 1
                # print(f"edge {node_id1,node_id2} was removed successfully")
                return True
        # print(f"edge {node_id1,node_id2} does not exists")
        return False

    # O(|V|+|E|)
    def getJsonGraph(self) -> dict:
        jsonOut = {"Edges": [], "Nodes": []}
        for node_id, node in self.nodeDict.items():
            if node.pos != None:
                position = f"{node.pos[0]},{node.pos[1]},{node.pos[2]}"
                jsonOut["Nodes"].append({"pos": position, "id": node_id})
            else:
                jsonOut["Nodes"].append({"id": node_id})
            for edge, weight in node.edgeDictOut.items():
                jsonOut["Edges"].append(
                    {"src": node_id, "w": weight, "dest": edge})
        return jsonOut

    def __repr__(self):
        return f"|V|={self.v_size()} , |E|={self.e_size()}"
