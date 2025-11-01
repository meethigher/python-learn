# itertools_demo.py - 常用 itertools
import itertools

if __name__ == '__main__':

    # islice(iterable, stop) --> islice object
    # islice(iterable, start, stop[, step]) --> islice object
    print('累加 take 5:', list(itertools.islice(itertools.count(1), 5)))


    print('组合 C(4,2):', list(itertools.combinations('ABCD', 2)))
    print('排列 P(3):', list(itertools.permutations('ABC', 3)))
    print('重复:', list(itertools.repeat('x', 3)))
