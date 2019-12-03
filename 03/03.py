with open("input.txt") as f:
    wireA, wireB = [x.split(",") for x in f.readlines()]


def get_direction(step):
    if step.startswith("U"):
        return 1 + 0j
    elif step.startswith("D"):
        return -1 + 0j
    elif step.startswith("L"):
        return 0 + -1j
    elif step.startswith("R"):
        return 0 + 1j


def trace_wire_pos(wire_path):
    wire_pos = 0 + 0j
    wire_locs = []
    for step in wire_path:
        step_len = int(step[1:])
        step_dir = get_direction(step)
        for _ in range(step_len):
            wire_pos += step_dir
            wire_locs.append(wire_pos)
    return wire_locs


wireA_pos = trace_wire_pos(wireA)
wireB_pos = trace_wire_pos(wireB)


common_locs = set(wireA_pos).intersection(set(wireB_pos))
min_mhtn_dists_common = min(int(abs(x.real) + abs(x.imag)) for x in common_locs)
print("Part 1:", min_mhtn_dists_common)


path_len_to_intersections = []
for intersection in common_locs:
    wireA_intersection_len = wireA_pos.index(intersection) + 1  # removed origin
    wireB_intersection_len = wireB_pos.index(intersection) + 1
    path_len_to_intersections.append(wireA_intersection_len + wireB_intersection_len)
print("Part 2:", min(path_len_to_intersections))