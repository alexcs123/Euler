from problems import *


def test(p=None):
    if p:
        print(f'{"PASSED" if p() == a[p] else "FAILED"} {p.__name__}\n')
    else:
        f = []
        for p in a:
            print(f'Testing {p.__name__}')
            if p() != a[p]:
                f.append(p)
        print(f'\nPASSED {len(a) - len(f)}/{len(a)} tests ({"{:.1f}".format((len(a) - len(f)) / len(a) * 100)}%)\n')
        if len(f):
            print(f'FAILED {str(len(f))}:')
            for p in f:
                print(p.__name__)
            print()


a = {
    p001: 233168,
    p002: 4613732,
    p003: 6857,
    p004: 906609,
    p005: 232792560,
    p006: 25164150,
    # p007: 104743,  # slow
    p008: 23514624000,
    p009: 31875000,
    # p010: 142913828922,  # slow
    p011: 70600674,
    # p012: 76576500,  # slow
    p013: 5537376230,
    # p014: 837799,  # slow
    p015: 137846528820,
    p016: 1366,
    p017: 21124,
    p018: 1074,
    p019: 171,
    p020: 648,
    # p021: 31626,  # slow
    p022: 871198282,
    # p023: 4179871,  # slow
    p024: 2783915460,
    p025: 4782,
    # p027: -59231,  # slow
    p028: 669171001,
    p029: 9183,
    p030: 443839,
    p031: 73682,
    p034: 40730,
    p035: 55,
    p036: 872187,
    p039: 840,
    p040: 210,
    p042: 162,
    p048: 9110846700,
    p053: 4075,
    p056: 972,
    p067: 7273,
    # p097: 8739992577,  # slow
    # p206: 1389019170  # slow
}
