# python3
import sys


def compute_min_refills(distance, tank, stops):
    full_travel = [0, *stops, distance]
    current = 0
    possible_next = 0
    refills = 0

    while current < len(full_travel):
        if possible_next == len(full_travel):
            return refills
            
        if tank >= full_travel[possible_next] -  full_travel[current]:
            possible_next += 1
        elif tank <= full_travel[possible_next] -  full_travel[current]:
            refills += 1
            current = possible_next - 1
            
            if full_travel[possible_next] - full_travel[current] > tank:
                return -1

    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
