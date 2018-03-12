class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def ccw(A, B, C):
    return (B.x - A.x) * (C.y - A.y) > (B.y - A.y) * (C.x - A.x)


result = 0

with open("triangles.txt", "r") as f:
    for line in f.readlines():
        ar = list(map(int, line.strip().split(",")))
        points = [Point(ar[0], ar[1]), Point(ar[2], ar[3]), Point(ar[4], ar[5])]
        if ccw(points[0], points[1], Point(0, 0)) == ccw(points[1], points[2], Point(0, 0)) and \
                ccw(points[0], points[1], Point(0, 0)) == ccw(points[2], points[0], Point(0, 0)):
            result += 1

print(result)
