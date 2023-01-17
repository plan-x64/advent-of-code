import datautils
import itertools
import re


def parse_input(data):
    pattern = re.compile("Sensor at x=(.*?), y=(.*?): closest beacon is at x=(.*?), y=(.*)")
    sensors = {}
    beacons = set()
    for line in data.splitlines():
        results = pattern.search(line)
        sensor = (int(results.group(1)), int(results.group(2)))
        beacon = (int(results.group(3)), int(results.group(4)))
        sensors[sensor] = manhattan_distance(sensor, beacon)
        beacons.add(beacon)
    return sensors, beacons


def manhattan_distance(p1,  p2):
    (p1_x, p1_y) = p1
    (p2_x, p2_y) = p2
    return abs(p1_x - p2_x) + abs(p1_y - p2_y)


def pt1(sensors, beacons):
    """
    The search space is quite large, so instead of calculating all points within the Manhattan
    distance for all sensors, we can instead calculate the four lines that bound each sensor.
    Using the bounding lines there are three possibilities for covering the row_intercept line:

    1. Intercept is in the upper half (i.e. sy <= row_intercept <= sy + distance)
    2. Intercept is in the lower half (i.e. sy - distance <= row_intercept < sy)
    3. Intercept is out of bound from a given sensor

    If we find that the row_intercept is within the Manhattan distance of a sensor we can calculate
    where the upper two, or lower two bounding lines intersect the row_intercept. The difference in
    x-values from the two intersecting lines will be the places where a beacon cannot exist. If
    we do this for all sensors then we can calculate how many x-values for the given row_intercept
    cannot contain a beacon.
    """
    row_intercept = 2000000
    covered = set()
    filtered_beacons = {by for (_, by) in beacons if by == row_intercept}
    for sensor, distance in sensors.items():
        (sx, sy) = sensor
        if sy <= row_intercept <= sy + distance:
            x_min = row_intercept - sy - distance + sx
            x_max = sy + distance + sx - row_intercept
            covered.update(range(x_min, x_max+1))
        elif sy - distance <= row_intercept < sy:
            x_min = sy - distance + sx - row_intercept
            x_max = row_intercept - sy + distance + sx
            covered.update(range(x_min, x_max+1))
        else:
            continue  # neither the top nor bottom intersect the row_intercept
    return len(covered.difference(filtered_beacons))


def pt2(sensors):
    """
    Since there is only a single point that could have the distress beacon we assume that it should
    be right outside the range of two of the sensors. To reduce the search space from O(10^12) we
    can generate four lines that are outside the bounding lines for each sensor. Taking the point
    where a positive and negatively sloped line intersect we can check if the Manhattan distance
    is larger towards each sensor than the sensor to its closest beacon. If the Manhattan distance
    to our intersected point is larger than the Manhattan distance of each sensor to its beacon
    then we know we have found the distress beacons' position.
    """
    max_bound = 4000000
    pos_intercepts = set()
    neg_intercepts = set()

    for (sx, sy), distance in sensors.items():
        pos_intercepts.add(sy + distance - sx + 1)  # y = x + (sy+distance-sx+1)
        pos_intercepts.add(sy - distance - sx - 1)  # y = x + (sy-distance-sx-1)
        neg_intercepts.add(sy + distance + sx + 1)  # y = -x + (sy+distance+sx+1)
        neg_intercepts.add(sy - distance + sx - 1)  # y = -x + (sy-distance+sx-1)

    for (a, b) in itertools.product(pos_intercepts, neg_intercepts):
        (x, y) = ((b-a)//2, (b+a)//2)  # position where negative and positive sloped line intersect
        if (0 < x < max_bound) and (0 < y < max_bound):
            if all(manhattan_distance((x, y), sensor) > distance for (sensor, distance) in sensors.items()):
                return 4000000*x+y


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/15/input"
    input_data = datautils.read_input_data(url)
    (_sensors, _beacons) = parse_input(input_data)
    print("({},  {})".format(pt1(_sensors, _beacons), pt2(_sensors)))
