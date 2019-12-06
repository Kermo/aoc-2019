with open("input.txt") as f:
    data = f.readlines()

nodes = {}

def count_orbits(node, start=0):
    count = start

    for child in node["satellites"]:
        count += count_orbits(child, start + 1)
    return count

def build_nodes():
    orbits = [x.strip().split(")") for x in data]


    for obj, satellite in orbits:
        if obj not in nodes:
            nodes[obj] = {"id": obj, "orbits": None, "satellites": []}
        if satellite not in nodes:
            nodes[satellite] = {"id": satellite, "orbits": None, "satellites": []}

        nodes[satellite]["orbits"] = nodes[obj]
        nodes[obj]["satellites"].append(nodes[satellite])

    return nodes

def count_orbital_transfers():
    visited = set()
    done = False
    hops = 0

    q = [(nodes["YOU"]["orbits"], 0)]

    while len(q) > 0 and not done:
        node, hops = q.pop(0)

        if node["id"] in visited:
            continue
        visited.add(node["id"])

        for x in node["satellites"]:
            if x["id"] == "SAN":
                done = True
                break

            q.append((x, hops + 1))

        if node["orbits"] is not None:
            q.append((node["orbits"], hops + 1))

    return hops

build_nodes()

print("Part 1: " + str(count_orbits(nodes["COM"])))
print("Part 2: " + str(count_orbital_transfers()))