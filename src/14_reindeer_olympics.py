#!/usr/bin/env python3


class Reindeer:
    def __init__(self, name, speed, burst, rest):
        self.name = name
        self.speed = speed
        self.burst = burst
        self.rest = rest

    def distance(self, time):
        cycle_distance = self.speed * self.burst
        cycles = time // (self.burst + self.rest)
        left = time - cycles * (self.burst + self.rest)
        return cycle_distance * cycles + self.speed * min(self.burst, left)


def first(*reindeers):
    return max([x.distance(2503) for x in reindeers])


def second(*reindeers):
    scores = {r.name: 0 for r in reindeers}
    for t in range(1, 2504):
        distances = [r.distance(t) for r in reindeers]
        for r in [reindeers[i] for i in range(len(distances)) if distances[i] == max(distances)]:
            scores[r.name] += 1

    return max(scores.values())


if __name__ == '__main__':
    data = (
        Reindeer('Vixen', 19, 7, 124),
        Reindeer('Rudolph', 3, 15, 28),
        Reindeer('Donner', 19, 9, 164),
        Reindeer('Blitzen', 19, 9, 158),
        Reindeer('Comet', 13, 7, 82),
        Reindeer('Cupid', 25, 6, 145),
        Reindeer('Dasher', 14, 3, 38),
        Reindeer('Dancer', 3, 16, 37),
        Reindeer('Prancer', 25, 6, 143)
    )

    res = first(*data)
    print(">>> %s" % res)

    res = second(*data)
    print(">>> %s" % res)
