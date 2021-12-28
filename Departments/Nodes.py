import random


class Vertex(object):
    def __init__(self, node_id: int, pos: tuple = None) -> None:
        random.seed(node_id)
        self.edgeDictOut = {}
        self.edgeDictIn = {}
        self.pos = pos if pos != None else (   35+random.random(), 32+random.random(), 0.0)
        self.id = node_id
        self.info = ''
        self.distance = float('inf')
        self.previous = None
        self.visited = False

    def __hash__(self) -> int:
        return self.id

    def __gt__(self, other) -> float:
        return self.distance > other.distance

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def set_visited(self):
        self.visited = True

    def __repr__(self):
        repr = f"{self.id}: |edges out| "
        for key in self.edgeDictOut:
            repr += str(key.id) + ' '
        repr += " |edges in| "
        for key in self.edgeDictIn:
            repr += str(key.id) + ' '
        return repr

    def __repr__(self):
        return f"{self.id}: |edges out| {self.edgeDictOut.keys()} |edges in| {self.edgeDictIn.keys()}"

    # def __repr__(self):
    #     repr = f"{self.id}: |edges out| "
    #     for key in self.edgeDictOut:
    #         repr += f"[{self.id} -> " + str(key.id) + '] '
    #     repr += " |edges in| "
    #     for key in self.edgeDictIn:
    #         repr += f"[{self.id} <- " + str(key.id) + '] '
    #     return repr
