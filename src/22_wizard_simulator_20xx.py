#!/usr/bin/env python3

import copy


class Effect:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def run(self, target):
        pass

    def expire(self, target):
        pass

    def __repr__(self):
        return self.name


class Shield(Effect):
    def __init__(self, duration):
        super().__init__("Shield", duration)
        self.first_round = duration

    def run(self, target):
        super().run(target)
        if self.duration == self.first_round:
            target.set_defence(target.defence + 7)

    def expire(self, target):
        target.set_defence(target.defence - 7)


class Poison(Effect):
    def __init__(self, duration):
        super().__init__("Poison", duration)

    def run(self, target):
        super().run(target)
        target.take_damage(3)


class Recharge(Effect):
    def __init__(self, duration):
        super().__init__("Recharge", duration)

    def run(self, target):
        super().run(target)
        target.add_mana(101)


class Spell:
    def __init__(self, name, cost, caster):
        self.name = name
        self.cost = cost
        self.caster = caster

    def cast(self, source, target):
        self.caster(source, target)

    def can_cast(self, source, target):
        return True

    def __repr__(self):
        return self.name


class EffectSpell(Spell):
    def __init__(self, name, cost, eff_type, eff_builder, tgt):
        super().__init__(name, cost, self.eff_caster)
        self.eff_type = eff_type
        self.eff_builder = eff_builder
        self.tgt = tgt

    def eff_caster(self, source, target):
        tar = self.tgt(source, target)
        eff = self.eff_builder()
        tar.add_effect(eff)

    def can_cast(self, source, target):
        return self.tgt(source, target).can_add(self.eff_type)


MagicMissile = Spell("Magic Missile", 53, lambda s, t: t.take_damage(4))
Drain = Spell("Drain", 73, lambda s, t: (t.take_damage(2), s.heal(2)))
ApplyShield = EffectSpell("Shield", 113, Shield, lambda: Shield(6), lambda s, t: s)
ApplyPoison = EffectSpell("Poison", 173, Poison, lambda: Poison(6), lambda s, t: t)
ApplyRecharge = EffectSpell("Recharge", 229, Recharge, lambda: Recharge(5), lambda s, t: s)


class Character:
    def __init__(self, name, hitpoints, defence=0, effects=()):
        self.name = name
        self.hitpoints = hitpoints
        self.defence = defence
        self.effects = list(effects)

    def is_dead(self):
        return self.hitpoints <= 0

    def take_damage(self, damage):
        damage -= self.defence
        if damage < 1:
            damage = 1
        self.hitpoints -= damage

    def heal(self, amount):
        self.hitpoints += amount

    def set_defence(self, amount):
        self.defence = amount

    def can_add(self, eff_class):
        for e in self.effects:
            if type(e) == eff_class and e.duration > 1:
                return False
        return True

    def add_effect(self, effect):
        self.effects.append(effect)

    def run_effects(self):
        active_effects = []
        for effect in self.effects:
            if effect.duration == 0:
                effect.expire(self)
            else:
                effect.run(self)
            if effect.duration > 0:
                effect = copy.copy(effect)
                effect.duration -= 1
                active_effects.append(effect)

        self.effects = active_effects

    def __repr__(self):
        return "%s [%d HP]" % (self.name, self.hitpoints)


class Boss(Character):
    def __init__(self, hitpoints, damage, defence=0, effects=()):
        super().__init__("Boss", hitpoints, defence, effects)
        self.damage = damage

    def to_hit(self):
        return self.damage


class Player(Character):
    def __init__(self, hitpoints, mana, defence=0, effects=()):
        super().__init__("Player", hitpoints, defence, effects)
        self.mana = mana

    def add_mana(self, amount):
        self.mana += amount

    def available_moves(self, target):
        spells = (MagicMissile, Drain, ApplyShield, ApplyPoison, ApplyRecharge)
        return [spell for spell in spells if spell.cost <= self.mana and spell.can_cast(self, target)]

    def cast(self, spell, target):
        self.mana -= spell.cost
        spell.cast(self, target)

    def __repr__(self):
        return "%s [%d HP, %d MN]" % (self.name, self.hitpoints, self.mana)


def run_effects(player1, player2):
    player1.run_effects()
    player2.run_effects()
    if player2.is_dead():
        return player1
    if player1.is_dead():
        return player2
    return None


def play_round(player, boss, move):
    w = run_effects(player, boss)
    if w:
        return w

    player.cast(move, boss)
    if boss.is_dead():
        return player

    w = run_effects(player, boss)
    if w:
        return w

    player.take_damage(boss.to_hit())
    if player.is_dead():
        return boss


def first(boss):
    player = Player(50, 500)

    cur_min = 10000

    def min_mana_move(curr_player, curr_boss, move, curr_mana):
        new_player = copy.deepcopy(curr_player)
        new_boss = copy.deepcopy(curr_boss)
        new_mana = curr_mana + move.cost

        if cur_min and cur_min < new_mana:
            return None

        w = play_round(new_player, new_boss, move)
        if w == new_player:
            return new_mana
        elif w == new_boss:
            return None

        return min_mana(new_player, new_boss, new_mana)

    def min_mana(curr_player, curr_boss, curr_mana=0):
        moves = curr_player.available_moves(curr_boss)

        if not moves:
            return None

        manas = [min_mana_move(curr_player, curr_boss, move, curr_mana) for move in moves]
        manas = [mana for mana in manas if mana is not None]
        if not manas:
            return None
        return min(manas)

    return min_mana(player, boss)


def second(boss):
    player = Player(50, 500)

    cur_min = 10000

    def min_mana_move(curr_player, curr_boss, move, curr_mana):
        new_player = copy.deepcopy(curr_player)
        new_boss = copy.deepcopy(curr_boss)
        new_mana = curr_mana + move.cost

        if cur_min and cur_min < new_mana:
            return None

        new_player.hitpoints -= 1

        w = play_round(new_player, new_boss, move)
        if w == new_player:
            return new_mana
        elif w == new_boss:
            return None

        return min_mana(new_player, new_boss, new_mana)

    def min_mana(curr_player, curr_boss, curr_mana=0):
        moves = curr_player.available_moves(curr_boss)

        if not moves:
            return None

        manas = [min_mana_move(curr_player, curr_boss, move, curr_mana) for move in moves]
        manas = [mana for mana in manas if mana is not None]
        if not manas:
            return None
        return min(manas)

    return min_mana(player, boss)


if __name__ == '__main__':
    res = first(Boss(71, 10))
    print(">>> %s" % res)

    res = second(Boss(71, 10))
    print(">>> %s" % res)
