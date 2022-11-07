class HashRing:
    def __init__(self, nodes: list):
        self.nodes = nodes
        self.n = len(nodes)

    def get_node(self, key: int = 0):
        if self.n == 0:
            return None
        return self.nodes[key % self.n]

    def delete_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.n -= 1

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.n += 1

    def get_n(self):
        return self.n
