

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

distances = [
    euclidean_distance(points[i], points[j])
    for i in range(len(points))
    for j in range(i + 1, len(points))
]

min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")