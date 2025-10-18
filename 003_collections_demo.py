# collections_demo.py - namedtuple, defaultdict, Counter
from collections import namedtuple, defaultdict, Counter

if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(f"x={p.x}, y={p.y}")
    print('namedtuple:', p)

    # 设置新建的默认值，为空[]的list
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    print('defaultdict:', dict(d))

    c = Counter('abracadabra')
    print('Counter 最常见 2 个:', c.most_common(2))
