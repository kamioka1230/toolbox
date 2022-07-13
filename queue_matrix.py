#-*- coding: utf-8 -*-
import math
import argparse

def p0(s, rho):
    # Σ (sρ)^n / n!
    a = 0
    for n in range(s):
        a += math.pow((s * rho), n) / math.factorial(n)
    # (sρ) ^ s / s! * (1 - ρ)
    b = math.pow((s * rho), s) / (math.factorial(s) * (1 - rho))
    return 1 / (a + b)

def lq(s, rho):
    numerator = rho * math.pow((s * rho), s)
    denominator = math.factorial(s) * math.pow((1 - rho), 2)
    return (numerator / denominator) * p0(s, rho)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--request', default=100, type=float)
    parser.add_argument('-t', '--time',    default=0.2, type=float)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    print('λ: ' + str(args.request) + ' req/sec, Ts: ' + str(args.time) + ' ms')
    print('L: # of tasks in service,  Lq: # of tasks in queue')
    print('W: ave time in service,  Wq: ave time waiting ')
    print('\t'.join(['s', 'Lq', 'L', 'Wq', 'W']))
    request_sec = args.request
    time_sec = args.time / 1000
    for s in range(1, 99):
        rho = request_sec / (s * (1 / time_sec))
        if rho >= 1:
            continue
        Lq = lq(s, rho)
        L = Lq + s * rho
        Wq = Lq / request_sec
        W = Wq + time_sec 
        if Lq <= 0.01:
            break
        print('\t'.join([
            str(s),
            str(round(Lq, 3)),
            str(round(L, 3)),
            str(round(Wq, 3)),
            str(round(W, 3))
        ]))
