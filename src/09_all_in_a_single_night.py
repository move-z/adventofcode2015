#!/usr/bin/env python3
import itertools


def first(*inputs):
    cities = set()
    distances = {}

    for distance in inputs:
        cities.add(distance[0])
        cities.add(distance[1])
        distances[(distance[0], distance[1])] = distance[2]
        distances[(distance[1], distance[0])] = distance[2]

    def get_distance(route):
        dist = 0
        last = None
        for city in route:
            if last is not None:
                dist += distances[last, city]
            last = city

        return dist

    return min([get_distance(r) for r in itertools.permutations(cities)])


def second(*inputs):
    cities = set()
    distances = {}

    for distance in inputs:
        cities.add(distance[0])
        cities.add(distance[1])
        distances[(distance[0], distance[1])] = distance[2]
        distances[(distance[1], distance[0])] = distance[2]

    def get_distance(route):
        dist = 0
        last = None
        for city in route:
            if last is not None:
                dist += distances[last, city]
            last = city

        return dist

    return max([get_distance(r) for r in itertools.permutations(cities)])


if __name__ == '__main__':
    data = (
        ('AlphaCentauri', 'Snowdin', 66),
        ('AlphaCentauri', 'Tambi', 28),
        ('AlphaCentauri', 'Faerun', 60),
        ('AlphaCentauri', 'Norrath', 34),
        ('AlphaCentauri', 'Straylight', 34),
        ('AlphaCentauri', 'Tristram', 3),
        ('AlphaCentauri', 'Arbre', 108),
        ('Snowdin', 'Tambi', 22),
        ('Snowdin', 'Faerun', 12),
        ('Snowdin', 'Norrath', 91),
        ('Snowdin', 'Straylight', 121),
        ('Snowdin', 'Tristram', 111),
        ('Snowdin', 'Arbre', 71),
        ('Tambi', 'Faerun', 39),
        ('Tambi', 'Norrath', 113),
        ('Tambi', 'Straylight', 130),
        ('Tambi', 'Tristram', 35),
        ('Tambi', 'Arbre', 40),
        ('Faerun', 'Norrath', 63),
        ('Faerun', 'Straylight', 21),
        ('Faerun', 'Tristram', 57),
        ('Faerun', 'Arbre', 83),
        ('Norrath', 'Straylight', 9),
        ('Norrath', 'Tristram', 50),
        ('Norrath', 'Arbre', 60),
        ('Straylight', 'Tristram', 27),
        ('Straylight', 'Arbre', 81),
        ('Tristram', 'Arbre', 90),
    )

    res = first(*data)
    print(">>> %d" % res)

    res = second(*data)
    print(">>> %d" % res)
