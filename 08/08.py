import collections

with open("input.txt") as f:
    data = [int(x) for x in f.readline()]

width = 25
height = 6
pixels_per_layer = width * height
assert len(data) % pixels_per_layer == 0
layers = []

def digits_multiplied():
    while data:
        layers.append(data[:pixels_per_layer])
        del data[:pixels_per_layer]

    n_zero = 99999999
    n_zero_current = 0
    layer_with_fewest_0 = []
    for layer in layers:
        n_zero_current = len([i for i in layer if i == 0])
        if n_zero_current < n_zero:
            n_zero = n_zero_current
            layer_with_fewest_0 = layer
    c = collections.Counter(layer_with_fewest_0)
    return c[1] * c[2]


def print_image():
    visible = []
    for i in range(pixels_per_layer):
        for layer in layers:
            color = layer[i]
            if color < 2:
                visible.append(color)
                break
    image = ""
    x = 0
    for y in range(height):
        for pixel in (i for i in visible[x:x + width]):
            if pixel == 0:
                image += " "
            elif pixel == 1:
                image += "#"
        image += "\n"
        x += width
    print(image)
    return "Done"

print("Part 1: " + str(digits_multiplied()))
print("Part 2: " + print_image())

