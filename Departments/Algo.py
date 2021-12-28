from api.GraphInter import GraphInterface
from Departments.Graph import DiGraph
from typing import Container, List
import json
import heapq
import matplotlib.pyplot as plt


class GraphAlgo(object):

    def __init__(self, graph: GraphInterface = DiGraph()) -> None:
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        file_name = file_name.split(".")
        try:
            graph = open(file_name[0]+".json")
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
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        file_name = file_name.split(".json")
        try:
            graphWrite = open("".join(file_name)+".json", 'w')
        except IOError:
            print("Could not write file:", file_name)
            return False
        with graphWrite:
            js = self.graph.getJsonGraph()
            json.dump(js, graphWrite)
            graphWrite.close()
            return True

    # O(|V|log|V|)
    def shortest_path(self, id1: int, id2: int) -> tuple:
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        """
        g = self.graph
        if id1 not in g.nodeDict or id2 not in g.nodeDict:
            return (float('inf'), [])
        self.dijkstra(id1)
        distanceToId2 = g.nodeDict[id2].distance
        listPath = []
        if distanceToId2 == float('inf'):
            return distanceToId2, listPath
        nodePrev = g.nodeDict[id2].previous
        listPath.append(id2)
        while nodePrev.id != id1:
            listPath.append(nodePrev.id)
            nodePrev = nodePrev.previous
        listPath.append(id1)
        return distanceToId2, listPath[::-1]
    
    def dijkstra(self, start):
        # Set the distance for the start node to zero
        nodeDict = self.graph.nodeDict
        unvisited_queue = []
        for vertex in nodeDict.values():
            vertex.distance = float('inf')
            vertex.previous = None
            vertex.visited = False
            t = vertex.distance, vertex
            unvisited_queue.append(t)
        nodeDict[start].distance = 0
        # Put tuple pair into the priority queue

        heapq.heapify(unvisited_queue)

        while len(unvisited_queue):
            # Pops a vertex with the smallest distance
            uv = heapq.heappop(unvisited_queue)
            current = uv[1]
            current.set_visited()
            # for next in v.adjacent:
            for next, w in current.edgeDictOut.items():
                # if visited, skip
                if nodeDict[next].visited:
                    continue
                new_dist = current.distance + w

                if new_dist < nodeDict[next].distance:
                    nodeDict[next].distance = new_dist
                    nodeDict[next].previous = current
            # Rebuild heap
            # 1. Pop every item
            while len(unvisited_queue):
                heapq.heappop(unvisited_queue)
            # 2. Put all vertices not visited into the queue
            unvisited_queue = [(v.distance, v)
                               for v in nodeDict.values() if not v.visited]

            heapq.heapify(unvisited_queue)
            
    def TSP(self, node_lst: List[int]) -> tuple:
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        if len(node_lst) ==1:
            return (node_lst,0)
        TSPpath =[]
        distance=0
        if len(node_lst)>1:
            src=node_lst.pop(0)
            dest=node_lst.pop(0)
            path=self.shortest_path(src,dest)
            if path[0]==float('inf'):
                return path
            distance+=path[0]
            TSPpath.extend(x for x in path[1] if x not in TSPpath)
        while len(node_lst)>0:
            if len(node_lst)>=2:
                if node_lst[0] in TSPpath and node_lst[1] in TSPpath:
                    node_lst.pop(0)
                    node_lst.pop(0)
                    continue
                if node_lst[0] in TSPpath:
                    node_lst.pop(0)
                    continue
                if node_lst[1] in TSPpath:
                    node_lst.pop(1)
                    continue
                src=node_lst.pop(0)
                dest=node_lst.pop(0)
                path=self.shortest_path(src,dest)
                if path[0]==float('inf'):
                    return path
                distance+=path[0]
                TSPpath.extend(x for x in path[1] if x not in TSPpath)
            else:
                src=TSPpath[-1]
                dest=node_lst.pop(0)
                path=self.shortest_path(src,dest)
                if path[0]==float('inf'):
                    return path
                distance+=path[0]
                TSPpath.extend(x for x in path[1] if x not in TSPpath)
        return TSPpath,distance
    
    def maxDistance(self) -> tuple:
        nodeDict = self.graph.nodeDict
        maxDis = float('-inf')
        for vertex in nodeDict.values():
            if vertex.distance > maxDis:
                maxDis = vertex.distance
            pass
        return maxDis

    def centerPoint(self)->tuple:
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        listPath = []
        nodeDict = self.graph.nodeDict
        for vertex in nodeDict.keys():
            self.dijkstra(vertex)
            t = self.maxDistance(), vertex
            if t[0] == float('inf'):
                return None, []

        listPath.sort()
        return listPath[0][1], listPath[0][0]

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        nodeDict = self.graph.nodeDict
        for node in nodeDict.values():
            x, y, z = node.pos
            plt.plot(x, y, markersize=15, marker="o", color="green")
            plt.text(x, y, str(node.id), color="black", fontsize=12)
            for edge in node.edgeDictOut.keys():
                destx, desty, s = nodeDict[edge].pos
                plt.annotate("", xy=(x, y), xytext=(destx, desty),
                             arrowprops={'arrowstyle': "<-", 'lw': 3})
        plt.show()

    def __repr__(self):
        return f"{self.graph}"
