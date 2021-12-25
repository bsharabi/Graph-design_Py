from typing import List

class Node:
    def __init__(self, node_id: int, pos: tuple = None) -> None:
        self.edgeDictOut = {}
        self.edgeDictIn = {}
        self.pos = pos
        self.id = node_id
        self.info = ''
        pass

    # def __repr__(self):
    #     repr = f"{self.id}: |edges out| "
    #     for key in self.edgeDictOut:
    #         repr += str(key.id) + ' '
    #     repr += " |edges in| "
    #     for key in self.edgeDictIn:
    #         repr += str(key.id) + ' '
    #     return repr
    
    def __repr__(self):
        repr = f"{self.id}: |edges out| "
        for key in self.edgeDictOut:
            repr +=f"{self.id} -> "+ str(key.id) + ' ,'
        repr += " |edges in| "
        for key in self.edgeDictIn:
            repr +=f"{self.id} <- "+ str(key.id) + ' ,'
        return repr
