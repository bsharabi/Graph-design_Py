import unittest
import os
from Departments.Algo import GraphAlgo
from Departments.Graph import DiGraph


class TestAlgo(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.graph = DiGraph()
        for n in range(4):
            self.graph.add_node(n)
        self.algo = GraphAlgo()

    def test_get_graph(self):
        a = self.algo
        print("\nTest get_graph")
        print("----------------------------")
        self.assertNotEqual(a.get_graph(), None)
        self.algo = GraphAlgo(self.graph)
        a = self.algo
        self.assertEqual(a.get_graph(), self.graph)

    def test_load_File(self):
        a = self.algo
        print("\nTest load_File")
        print("----------------------------")
        self.assertFalse(a.load_from_json("data\T0D.json"))
        self.assertTrue(a.load_from_json("data\T0.json"))
        T0 = {
            "Nodes": [
                {
                    "id": 0
                },
                {
                    "id": 1
                },
                {
                    "id": 2
                },
                {
                    "id": 3
                }
            ],
            "Edges": [
                {
                    "src": 0,
                    "dest": 1,
                    "w": 1
                },
                {
                    "src": 1,
                    "dest": 0,
                    "w": 1.1
                },
                {
                    "src": 1,
                    "dest": 2,
                    "w": 1.3
                },
                {
                    "src": 1,
                    "dest": 3,
                    "w": 1.8
                },
                {
                    "src": 2,
                    "dest": 3,
                    "w": 1.1
                }
            ]
        }
        graph = a.get_graph()
        self.assertDictEqual(graph.getJsonGraph(), T0)
        self.assertTrue(a.load_from_json("data\A0.json"))
        A0 = {
            "Edges": [
                {
                    "src": 0,
                    "w": 1.4004465106761335,
                    "dest": 1
                },
                {
                    "src": 0,
                    "w": 1.4620268165085584,
                    "dest": 10
                },
                {
                    "src": 1,
                    "w": 1.8884659521433524,
                    "dest": 0
                },
                {
                    "src": 1,
                    "w": 1.7646903245689283,
                    "dest": 2
                },
                {
                    "src": 2,
                    "w": 1.7155926739282625,
                    "dest": 1
                },
                {
                    "src": 2,
                    "w": 1.1435447583365383,
                    "dest": 3
                },
                {
                    "src": 3,
                    "w": 1.0980094622804095,
                    "dest": 2
                },
                {
                    "src": 3,
                    "w": 1.4301580756736283,
                    "dest": 4
                },
                {
                    "src": 4,
                    "w": 1.4899867265011255,
                    "dest": 3
                },
                {
                    "src": 4,
                    "w": 1.9442789961315767,
                    "dest": 5
                },
                {
                    "src": 5,
                    "w": 1.4622464066335845,
                    "dest": 4
                },
                {
                    "src": 5,
                    "w": 1.160662656360925,
                    "dest": 6
                },
                {
                    "src": 6,
                    "w": 1.6677173820549975,
                    "dest": 5
                },
                {
                    "src": 6,
                    "w": 1.3968360163668776,
                    "dest": 7
                },
                {
                    "src": 7,
                    "w": 1.0176531013725074,
                    "dest": 6
                },
                {
                    "src": 7,
                    "w": 1.354895648936991,
                    "dest": 8
                },
                {
                    "src": 8,
                    "w": 1.6449953452844968,
                    "dest": 7
                },
                {
                    "src": 8,
                    "w": 1.8526880332753517,
                    "dest": 9
                },
                {
                    "src": 9,
                    "w": 1.4575484853801393,
                    "dest": 8
                },
                {
                    "src": 9,
                    "w": 1.022651770039933,
                    "dest": 10
                },
                {
                    "src": 10,
                    "w": 1.1761238717867548,
                    "dest": 0
                },
                {
                    "src": 10,
                    "w": 1.0887225789883779,
                    "dest": 9
                }
            ],
            "Nodes": [
                {
                    "pos": "35.18753053591606,32.10378225882353,0.0",
                    "id": 0
                },
                {
                    "pos": "35.18958953510896,32.10785303529412,0.0",
                    "id": 1
                },
                {
                    "pos": "35.19341035835351,32.10610841680672,0.0",
                    "id": 2
                },
                {
                    "pos": "35.197528356739305,32.1053088,0.0",
                    "id": 3
                },
                {
                    "pos": "35.2016888087167,32.10601755126051,0.0",
                    "id": 4
                },
                {
                    "pos": "35.20582803389831,32.10625380168067,0.0",
                    "id": 5
                },
                {
                    "pos": "35.20792948668281,32.10470908739496,0.0",
                    "id": 6
                },
                {
                    "pos": "35.20746249717514,32.10254648739496,0.0",
                    "id": 7
                },
                {
                    "pos": "35.20319591121872,32.1031462,0.0",
                    "id": 8
                },
                {
                    "pos": "35.19597880064568,32.10154696638656,0.0",
                    "id": 9
                },
                {
                    "pos": "35.18910131880549,32.103618700840336,0.0",
                    "id": 10
                }
            ]
        }
        graph = a.get_graph()
        self.assertDictEqual(graph.getJsonGraph(), A0)

    def test_save_File(self):
        a = self.algo
        print("\nTest save_File")
        print("----------------------------")
        if os.path.exists("data\\test.json"):
            os.remove("data\\test.json")
        self.assertFalse(os.path.exists("data\\test.json"))
        self.assertTrue(a.save_to_json("data\\test.json"))
        self.assertTrue(os.path.exists("data\\test.json"))
        self.assertTrue(a.load_from_json("data\\test.json"))
        g = a.get_graph()
        self.assertDictEqual(g.getJsonGraph(), {"Edges": [], "Nodes": []})

    def test_shortest_path(self):
        a = self.algo
        print("\nTest shortest_path")
        print("----------------------------")
        pass

    def test_TSP(self):
        a = self.algo
        print("\nTest TSP")
        print("----------------------------")
        pass

    def test_centerPoint(self):
        a = self.algo
        print("\nTest centerPoint")
        print("----------------------------")
        pass


if __name__ == '__main__':
    unittest.main()
