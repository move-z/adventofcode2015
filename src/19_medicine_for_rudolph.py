#!/usr/bin/env python3
from re import finditer


def first(molecule, *transformations):
    result = set()

    for t, r in transformations:
        pos = [m.start() for m in finditer(t, molecule)]
        for i in pos:
            result.add(molecule[:i] + r + molecule[i + len(t):])

    return len(result)


def second(molecule, *transformations):
    cache = {}

    def counter(start, depth):
        if start in cache:
            return depth + cache[start]

        depths = set()
        for t, r in transformations:
            pos = [m.start() for m in finditer(r, start)]
            for i in pos:
                new_str = start[:i] + t + start[i + len(r):]
                if new_str == 'e':
                    cache[start] = 1
                    return depth + 1
                d = counter(new_str, depth + 1)
                if d is not None:
                    depths.add(d)
        if not depths:
            return None
        child_depth = min(depths)
        cache[start] = child_depth - depth
        return child_depth

    return counter(molecule, 0)


if __name__ == '__main__':
    data = (
        ('Al', 'ThF'),
        ('Al', 'ThRnFAr'),
        ('B', 'BCa'),
        ('B', 'TiB'),
        ('B', 'TiRnFAr'),
        ('Ca', 'CaCa'),
        ('Ca', 'PB'),
        ('Ca', 'PRnFAr'),
        ('Ca', 'SiRnFYFAr'),
        ('Ca', 'SiRnMgAr'),
        ('Ca', 'SiTh'),
        ('F', 'CaF'),
        ('F', 'PMg'),
        ('F', 'SiAl'),
        ('H', 'CRnAlAr'),
        ('H', 'CRnFYFYFAr'),
        ('H', 'CRnFYMgAr'),
        ('H', 'CRnMgYFAr'),
        ('H', 'HCa'),
        ('H', 'NRnFYFAr'),
        ('H', 'NRnMgAr'),
        ('H', 'NTh'),
        ('H', 'OB'),
        ('H', 'ORnFAr'),
        ('Mg', 'BF'),
        ('Mg', 'TiMg'),
        ('N', 'CRnFAr'),
        ('N', 'HSi'),
        ('O', 'CRnFYFAr'),
        ('O', 'CRnMgAr'),
        ('O', 'HP'),
        ('O', 'NRnFAr'),
        ('O', 'OTi'),
        ('P', 'CaP'),
        ('P', 'PTi'),
        ('P', 'SiRnFAr'),
        ('Si', 'CaSi'),
        ('Th', 'ThCa'),
        ('Ti', 'BP'),
        ('Ti', 'TiTi'),
        ('e', 'HF'),
        ('e', 'NAl'),
        ('e', 'OMg'),
    )

    molecule = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'

    res = first(molecule, *data)
    print(">>> %s" % res)

    res = second(molecule, *data)
    print(">>> %s" % res)
