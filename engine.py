#!/usr/bin/env python3

import sys
import itertools
import math


class Expression:
    def __init__(self, val=math.nan, s=None):
        self.val = val
        if s is None:
            self.s = '#' if math.isnan(val) else str(val)
        else:
            self.s = s

    def isnan(self):
        return math.isnan(self.val)

    def _make_s(self, op, other):
        return '(%s %s %s)' % (self.s, op, other.s)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return hash((self.val, self.s))

    def __add__(self, other):
        return Expression(self.val + other.val, self._make_s('+', other))

    def __sub__(self, other):
        return Expression(self.val - other.val, self._make_s('-', other))

    def __mul__(self, other):
        return Expression(self.val * other.val, self._make_s('*', other))

    def __truediv__(self, other):
        if other.val != 0 and self.val % other.val == 0:
            return Expression(self.val // other.val, self._make_s('/', other))
        else:
            return Expression()

    def __str__(self):
        return '%s%s%s%s%s' % ('\033[31m', str(self.val), '\033[0;37m', self.s, '\033[0m')


def combine2(x, y):
    exps = (x + y, x - y, y - x, x * y, x / y, y / x)
    for exp in exps:
        if not exp.isnan():
            yield exp


def combine_expressions(exps):
    """all the combinations of applying +-*/ to exps
    """
    n = len(exps)

    if n == 0:
        return
    elif n == 1:
        yield from exps
    elif n == 2:
        yield from combine2(*exps)
    else:
        for x, y, *rest in itertools.permutations(exps):
            for exp in combine2(x, y):
                yield from combine_expressions([exp] + rest)


def resolve_exps(exps):
    for exp in combine_expressions(exps):
        #if exp.val == int(exp.val):
        if exp.val == 24:
            yield exp


def resolve_nums(nums):
    exps = [Expression(x) for x in nums]
    return resolve_exps(exps)


def resolve(args):
    nums = [int(s) for s in args]
    return resolve_nums(nums)


if __name__ == '__main__':
    r = set(resolve(sys.argv[1:]))
    for sol in r:
        print(sol)

