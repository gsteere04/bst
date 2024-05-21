class TreeNode:
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key: int) -> None:
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key: int) -> None:
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key: int) -> bool:
        return self._search(self.root, key)

    def _search(self, node, key: int) -> bool:
        if node is None:
            return False
        if node.val == key:
            return True
        elif key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def in_order_traversal(self) -> list:
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result) -> None:
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.val)
            self._in_order_traversal(node.right, result)

    def find_min(self) -> int:
        if self.root is None:
            raise ValueError("Tree is empty")
        return self._find_min(self.root)

    def _find_min(self, node) -> int:
        while node.left is not None:
            node = node.left
        return node.val

    def find_max(self) -> int:
        if self.root is None:
            raise ValueError("Tree is empty")
        return self._find_max(self.root)

    def _find_max(self, node) -> int:
        while node.right is not None:
            node = node.right
        return node.val

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node) -> int:
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1

    def count_leaves(self) -> int:
        return self._count_leaves(self.root)

    def _count_leaves(self, node) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves(node.left) + self._count_leaves(node.right)

    def serialize(self) -> str:
        result = []
        self._pre_order_traversal(self.root, result)
        return ','.join(map(str, result))
    
    def deserialize(self, data: str) -> None:
        if not data:
            return
        values = list(map(int, data.split(',')))
        self.root = self._deserialize_helper(values)

