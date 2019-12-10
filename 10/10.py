from math import atan, degrees

with open("input.txt") as f:
    data = list(f.read().splitlines())
    data2 = data

def gcd(x, y):
    if not x:
        return abs(y)
    if not y:
        return abs(x)

    while y:
        x, y = y, x % y
    return abs(x)

def get_best_station(asteroids):
    asteroids_in_los = [len(get_directions(station, asteroids)) for station in asteroids]
    station_id = asteroids_in_los.index(max(asteroids_in_los))
    return asteroids[station_id]

def calculate_angle(vector):
    if vector[1] == 0:
        return 90
    return degrees(atan(vector[0]/vector[1]))

def split_quadrants(directions):
    quadrants = []
    quadrants.append([x for x in directions if x[0] >= 0 and x[1] < 0])
    quadrants.append([x for x in directions if x[0] > 0  and x[1] >= 0])
    quadrants.append([x for x in directions if x[0] <= 0 and x[1] > 0])
    quadrants.append([x for x in directions if x[0] < 0  and x[1] <= 0])
    return quadrants


def lazer_pew_pew(quadrants, station, asteroids, size_x, size_y):
    target_amount = len(asteroids) - 200
    while True:
        for quadrant in quadrants:
            for direction in quadrant:
                multi = 1
                while True:
                    coord = (station[0] + direction[0] * multi, station[1] + direction[1] * multi)

                    if coord[0] < 0 or coord[0] > size_x or \
                            coord[1] < 0 or coord[1] > size_y:
                        break

                    if coord in asteroids:
                        asteroids.remove(coord)

                        if len(asteroids) == target_amount:
                            return coord[0] * 100 + coord[1]
                        break
                    multi += 1

def get_directions(station, asteroids):
    directions = set()
    for asteroid in asteroids:
        if asteroid == station:
            continue

        vec = (asteroid[0] - station[0], asteroid[1] - station[1])
        gcd_value = gcd(vec[0], vec[1])
        vec = (vec[0] // gcd_value, vec[1] // gcd_value)

        directions.add(vec)

    return directions

def count_detected_asteroids():
    size_x, size_y = len(data[0]), len(data)

    asteroids = [(x, y) for y in range(size_y) for x in range(size_x) if data[y][x] == "#"]

    return max([len(get_directions(station, asteroids)) for station in asteroids])

def return_bet_coordinates():

    size_x, size_y = len(data2[0]), len(data2)

    asteroids = [(x, y) for y in range(size_y) for x in range(size_x) if data2[y][x] == "#"]
    station = get_best_station(asteroids)

    directions = list(get_directions(station, asteroids))
    directions.sort(key=lambda direction: calculate_angle(direction), reverse=True)

    quadrants = split_quadrants(directions)

    return lazer_pew_pew(quadrants, station, asteroids, size_x, size_y)


print("Part 1: " + str(count_detected_asteroids()))
print("Part 2: " + str(return_bet_coordinates()))