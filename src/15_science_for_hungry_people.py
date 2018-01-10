#!/usr/bin/env python3
from functools import reduce


class Ingredient:
    def __init__(self, name, **properties):
        self.name = name
        self.properties = properties


def first(*ingredients):
    def get_quantities(total, available):
        results = []
        if available == 1:
            return [(total,)]
        remainder = available - 1
        for used in range(1, total - remainder):
            for c in get_quantities(total - used, remainder):
                results.append((used,) + c)
        return results

    def score(recipe):
        scores = [prop for prop in ingredients[0].properties if prop != 'calories']
        scores = [sum([recipe[i] * ingredients[i].properties[prop] for i in range(len(recipe))]) for prop in scores]
        return reduce(lambda x, y: x * y, [s if s > 0 else 0 for s in scores])

    return max(score(recipe) for recipe in get_quantities(100, len(ingredients)))


def second(*ingredients):
    def get_quantities(total, available):
        results = []
        if available == 1:
            return [(total,)]
        remainder = available - 1
        for used in range(1, total - remainder):
            for c in get_quantities(total - used, remainder):
                results.append((used,) + c)
        return results

    def score(recipe):
        scores = [prop for prop in ingredients[0].properties if prop != 'calories']
        scores = [sum([recipe[i] * ingredients[i].properties[prop] for i in range(len(recipe))]) for prop in scores]
        return reduce(lambda x, y: x * y, [s if s > 0 else 0 for s in scores])

    def calories(recipe):
        return sum([recipe[i] * ingredients[i].properties['calories'] for i in range(len(recipe))])

    return max(score(recipe) for recipe in get_quantities(100, len(ingredients)) if calories(recipe) == 500)


if __name__ == '__main__':
    data = (
        Ingredient('Sugar', capacity=3, durability=0, flavor=0, texture=-3, calories=2),
        Ingredient('Sprinkles', capacity=-3, durability=3, flavor=0, texture=0, calories=9),
        Ingredient('Candy', capacity=-1, durability=0, flavor=4, texture=0, calories=1),
        Ingredient('Chocolate', capacity=0, durability=0, flavor=-2, texture=2, calories=8)
    )

    res = first(*data)
    print(">>> %s" % res)

    res = second(*data)
    print(">>> %s" % res)
