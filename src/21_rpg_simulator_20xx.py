#!/usr/bin/env python3


class Item:
    def __init__(self, name, cost, damage, defence):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.defence = defence


Item.Empty = Item("empty", 0, 0, 0)


class Character:
    def __init__(self, name, hitpoints, damage, defence, equipment=()):
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage
        self.defence = defence
        self.equipment = equipment

    def is_dead(self):
        return self.hitpoints <= 0

    def to_hit(self):
        return self.damage + sum(item.damage for item in self.equipment)

    def take_damage(self, damage):
        defence = self.defence + sum([item.defence for item in self.equipment])
        damage -= defence
        if damage <= 0:
            damage = 1
        self.hitpoints -= damage


def fight(first_player, second_player):
    while True:
        second_player.take_damage(first_player.to_hit())
        if second_player.is_dead():
            return first_player
        first_player.take_damage(second_player.to_hit())
        if first_player.is_dead():
            return second_player


weapons = (
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0)
)

armors = (
    Item.Empty,
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5)
)

rings = (
    Item.Empty,
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3)
)


def first(boss):
    combinations = [
        Character("player", 100, 0, 0, (weapon, armor, ring1, ring2))
        for weapon in weapons
        for armor in armors
        for ring1 in rings
        for ring2 in rings
        if ring1 == ring2 == Item.Empty or ring1 is not ring2
    ]

    wins = [e for e in combinations
            if e == fight(e, Character(boss.name, boss.hitpoints, boss.damage, boss.defence))]

    return min([sum([i.cost for i in c.equipment]) for c in wins])


def second(boss):
    combinations = [
        Character("player", 100, 0, 0, (weapon, armor, ring1, ring2))
        for weapon in weapons
        for armor in armors
        for ring1 in rings
        for ring2 in rings
        if ring1 == ring2 == Item.Empty or ring1 != ring2
    ]

    losses = [e for e in combinations
              if e != fight(e, Character(boss.name, boss.hitpoints, boss.damage, boss.defence))]

    for l in losses:
        if sum([i.cost for i in l.equipment]) == 282:
            print(l)
    return max([sum([i.cost for i in c.equipment]) for c in losses])


if __name__ == '__main__':
    res = first(Character("boss", 103, 9, 2))
    print(">>> %s" % res)

    res = second(Character("boss", 103, 9, 2))
    print(">>> %s" % res)
