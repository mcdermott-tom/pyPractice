planets = [
    # format('name', radius, density, distance from sun)
    ('Tommy', 2440, 5.43, 0.395),
    ('Luis', 6378, 3.93, 1.595)
]

rad = lambda x: x[1]

planets.sort(key=rad, reverse=False)
print(planets)