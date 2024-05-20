import unittest
from bst import BST

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            self.bst.insert(value)

    def test_insert_and_search(self):
        self.assertTrue(self.bst.search(5))
        self.assertTrue(self.bst.search(3))
        self.assertFalse(self.bst.search(10))
        self.bst.insert(10)
        self.assertTrue(self.bst.search(10))

    def test_in_order_traversal(self):
        self.assertEqual(self.bst.in_order_traversal(), [2, 3, 4, 5, 6, 7, 8])

    def test_find_min(self):
        self.assertEqual(self.bst.find_min(), 2)

    def test_find_max(self):
        self.assertEqual(self.bst.find_max(), 8)

    def test_height(self):
        self.assertEqual(self.bst.height(), 3)

    def test_count_leaves(self):
        self.assertEqual(self.bst.count_leaves(), 4)

    def test_serialize_deserialize(self):
        tree_str = self.bst.serialize()
        new_bst = BST()
        new_bst.deserialize(tree_str)
        self.assertEqual(new_bst.in_order_traversal(), self.bst.in_order_traversal())

if __name__ == "__main__":
    unittest.main()