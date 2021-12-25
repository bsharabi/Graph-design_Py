import unittest
from Departments.Graph import DiGraph
from Departments.Nodes import Node

class TestDiGraph(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.graph = DiGraph()
        for id in range(4):
            self.graph.add_node(id)
        print(self.graph)

    def test_v_size(self):
        print("\nTest v_size")
        print("----------------------------")
        self.assertEqual(self.graph.v_size(), 4)
        self.graph.add_node(id)
        self.assertEqual(self.graph.v_size(), 5)

    def test_e_size(self):
        print("\nTest e_size")
        print("----------------------------")
        self.assertEqual(self.graph.e_size(), 0)
        self.graph.add_edge(0, 1, 1)
        self.assertEqual(self.graph.e_size(), 1)
        self.graph.add_edge(1, 0, 1.1)
        self.assertEqual(self.graph.e_size(), 2)
        self.graph.add_edge(1, 0, 1.1)
        self.assertEqual(self.graph.e_size(), 2)
        self.graph.add_edge(1, 2, 1.3)
        self.assertEqual(self.graph.e_size(), 3)
        self.graph.add_edge(2, 3, 1.1)
        self.assertEqual(self.graph.e_size(), 4)
        self.graph.add_edge(1, 3, 1.9)
        self.assertEqual(self.graph.e_size(), 5)

    def test_get_all_v(self):
        print("\nTest get_all_v")
        print("----------------------------")
        self.assertDictEqual(self.graph.get_all_v(), self.graph.nodeDict)

    def test_all_in_edges_of_node(self):
        print("\nTest all_in_edges_of_node")
        print("----------------------------")
        g = self.graph
        nodeDictIn = g.all_in_edges_of_node(1)
        self.assertDictEqual({}, nodeDictIn)
        g.add_edge(0, 1, 8)
        self.assertDictEqual({g.nodeDict[0]: 8}, nodeDictIn)
        g.add_edge(2, 1, 8)
        g.add_edge(3, 1, 8)
        self.assertDictEqual(
            {g.nodeDict[0]: 8, g.nodeDict[2]: 8, g.nodeDict[3]: 8}, nodeDictIn)

    def test_all_out_edges_of_node(self):
        print("\nTest all_out_edges_of_node")
        print("----------------------------")
        g = self.graph
        nodeDictOut = g.all_out_edges_of_node(1)
        self.assertDictEqual({}, nodeDictOut)
        g.add_edge(1, 0, 8)
        self.assertDictEqual({g.nodeDict[0]: 8}, nodeDictOut)
        g.add_edge(1, 2, 8)
        g.add_edge(1, 3, 8)
        self.assertDictEqual(
            {g.nodeDict[0]: 8, g.nodeDict[2]: 8, g.nodeDict[3]: 8}, nodeDictOut)


    def test_get_mc(self):
        print("\nTest get_mc")
        print("----------------------------")
        self.assertEqual(self.graph.get_mc(), 4)
        self.graph.add_edge(0, 1, 1)
        self.assertEqual(self.graph.get_mc(), 5)
        self.graph.add_edge(0, 1, 1)
        self.assertEqual(self.graph.get_mc(), 5)
        self.graph.add_node(3)
        self.assertEqual(self.graph.get_mc(), 5)
        self.graph.add_node(4)
        self.assertEqual(self.graph.get_mc(), 6)
        pass

    def test_add_edge(self):
        print("\nTest add_edge")
        print("----------------------------")
        g = self.graph

        self.assertTrue(g.add_edge(0, 1, 1))
        self.assertTrue(g.add_edge(1, 0, 1.1))

        self.assertFalse(g.add_edge(0, 1, 1))

        self.assertFalse(g.add_edge(5, 1, 1))
        self.assertFalse(g.add_edge(0, 5, 1))

        self.assertFalse(g.add_edge(5, 5, 1))

    def test_add_node(self):
        print("\nTest add_node")
        print("----------------------------")
        g = self.graph
        self.assertFalse(g.add_node(0))
        self.assertFalse(g.add_node(1))
        self.assertTrue(g.add_node(4))

    def test_remove_node(self):
        print("\nTest remove_node")
        print("----------------------------")

        g = self.graph
        self.assertFalse(g.remove_node(5))
        self.assertTrue(g.remove_node(3))
        self.assertFalse(3 in g.nodeDict)
        self.assertTrue(g.remove_node(1))

    def test_remove_edge(self):
        print("\nTest remove_edge")
        print("----------------------------")
        g = self.graph
        self.assertFalse(g.remove_edge(0, 2))
        g.add_edge(0, 1, 2)
        self.assertTrue(g.remove_edge(0, 1))


if __name__ == '__main__':
    unittest.main()
