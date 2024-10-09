import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def print_point(self):
    #     print(f"[{self.x}, {self.y}]", end=" ")

    def get_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class PointSet:
    def __init__(self):
        self.points = []

    # Private
    def __sort_by__key(self, key):
        return sorted(self.points, key=lambda point: getattr(point, key))

    def __sort_by_x(self):
        return self.__sort_by__key("x")

    def __sort_by_y(self):
        return self.__sort_by__key("y")

    def __get_closest_pair_recur(self, arr_x, arr_y):
        n = len(arr_x)

        if n < 4:
            return self.__get_closets_pair_brute_force(arr_x)

        xmid = arr_x[n // 2].x
        arr_x_left = arr_x[: n // 2]
        arr_x_right = arr_x[n // 2 :]

        arr_y_left = list(filter(lambda p: p.x <= xmid, arr_y))
        arr_y_right = list(filter(lambda p: p.x > xmid, arr_y))

        d_pair_left = self.__get_closest_pair_recur(arr_x_left, arr_y_left)
        d_pair_right = self.__get_closest_pair_recur(arr_x_right, arr_y_right)

        d_pair = d_pair_left
        if d_pair_right[0] < d_pair_left[0]:
            d_pair = d_pair_right

        span = list(filter(lambda p: abs(p.x - xmid) < d_pair[0], arr_y))
        return self.__find_min_spanning_pair(span, d_pair)

    def __get_closets_pair_brute_force(self, point_set):
        min_dist = float("inf")
        n = len(point_set)
        closest_pair = None
        for i in range(n):
            for j in range(i + 1, n):
                dist = point_set[i].get_distance(point_set[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (point_set[i], point_set[j])
        return min_dist, closest_pair

    def __find_min_spanning_pair(self, span, d_pair):
        min_dist = d_pair[0]
        n = len(span)
        closest_pair = d_pair[1]
        for i in range(n):
            for j in range(i + 1, n):
                if span[j].y - span[i].y > d_pair[0]:
                    break
                dist = span[i].get_distance(span[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (span[i], span[j])
        return (min_dist, closest_pair)

    # Public
    def append_point(self, point):
        self.points.append(point)

    def get_closest_pair(self):
        points_x = self.__sort_by_x()
        points_y = self.__sort_by_y()
        return self.__get_closest_pair_recur(points_x, points_y)

    # def reset(self):
    #     self.pints = []


# def print_point_set(point_set):
#     for i in range(len(point_set.points)):
#         point_set.points[i].print_point()


def main():
    num_runs = int(input())

    for _ in range(num_runs):
        num_points = int(input())
        point_set = PointSet()

        for _ in range(num_points):
            x, y = map(float, input().split())
            point = Point(x, y)
            point_set.append_point(point)

        d_pair = point_set.get_closest_pair()

        print(f"{d_pair[0]:.4f}")
        point1_index = point_set.points.index(d_pair[1][0])
        point2_index = point_set.points.index(d_pair[1][1])
        print(f"{point1_index} {point2_index}")


main()
