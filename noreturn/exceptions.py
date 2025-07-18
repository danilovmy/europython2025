from dataclasses import dataclass

@dataclass
class Node:
    value: int = None
    left: int = None
    right: int = None

    def path(self):
      # should be implemented path logic
      return f'-> {self}'

    @property
    def children(self):
        yield from (child for child in (self.left, self.right) if child)


class Response(Exception):
    def __init__(self, node):
      self.value = node

def dfs(node, target):
    if node.value == target:
      raise Response(node)    # exit on early success
    for child in node.children:
        dfs(child, target)


if __name__ == "__main__":
    root_node = Node(42)
    try:
        dfs(root_node, 42)
    except Response as response:
        print(" found:", response.value.path())
