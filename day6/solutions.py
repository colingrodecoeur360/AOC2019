def load_input():
    with open("day6/input.txt") as f:
        lines = f.readlines()
    return [line.strip().split(")") for line in lines]


def compute_orbiting_planets_by_center(orbits):
    orbiting_planets_by_center = dict()
    for orbit in orbits:
        if orbit[0] in orbiting_planets_by_center:
            orbiting_planets_by_center[orbit[0]].append(orbit[1])
        else:
            orbiting_planets_by_center[orbit[0]] = [orbit[1]]
    return orbiting_planets_by_center


class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.distance_to_center = parent.distance_to_center + 1 if parent else 0

    def __repr__(self):
        return f"{self.name} ({self.distance_to_center})"


def build_tree(orbits):
    root_node = "COM"
    tree = {root_node: Node(root_node)}
    orbiting_planets_by_center = compute_orbiting_planets_by_center(orbits)
    origins = [root_node]
    while len(orbiting_planets_by_center):
        next_origins = []
        for origin in origins:
            orbiting_objects = orbiting_planets_by_center.get(origin, [])
            for orbiting_object in orbiting_objects:
                next_origins.append(orbiting_object)
                tree[orbiting_object] = Node(name=orbiting_object, parent=tree[origin])
            if origin in orbiting_planets_by_center:
                del orbiting_planets_by_center[origin]
        origins = next_origins
    return tree


def compute_total_distance(tree):
    return sum(planet.distance_to_center for planet in tree.values())


def compute_number_of_transfers(tree, node1, node2):
    def build_ancestors(node):
        ancestors = []
        while node:
            ancestors.append(node)
            node = node.parent
        return list(reversed(ancestors))

    ancestors = [build_ancestors(tree[node]) for node in (node1, node2)]
    closest_ancestor = None
    for ancestor1, ancestor2 in zip(*ancestors):
        if ancestor1 != ancestor2:
            closest_ancestor = ancestor1.parent
            break
    return (tree[node1].parent.distance_to_center
            + tree[node2].parent.distance_to_center
            - 2 * closest_ancestor.distance_to_center)


if __name__ == "__main__":
    orbits = load_input()
    tree = build_tree(orbits)
    print(compute_total_distance(tree))
    print(compute_number_of_transfers(tree, "YOU", "SAN"))
