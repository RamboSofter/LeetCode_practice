# python 常用库函数

## 常用数据结构函数 collections

[官方文档](https://docs.python.org/zh-cn/3/library/collections.html)
[源码](https://github.com/python/cpython/blob/3.10/Lib/collections/__init__.py)

```python
import collections

```

ChainMap 类

```python
class collections.ChainMap(*maps)
    '''合并多个字典
    将多个映射快速的链接到一起，这样它们就可以作为一个单元处理。
    还有一个 maps 属性(attribute)， maps
    一个创建子上下文的方法(method)，  new_child(m=None, **kwargs)
    一个存取它们首个映射的属性(property) parents
    '''
```

Counter类

```python
class collections.Counter([iterable-or-mapping])
    '''计算器工具
    一个 Counter 是一个 dict 的子类，用于计数可哈希对象。
    它是一个集合，元素像字典键(key)一样存储，它们的计数存储为值。计数可以是任何整数值，包括0和负数。
    Counter 类有点像其他语言中的 bags或multisets。
    '''
    # 初始化方法
    c = Counter()                           # a new, empty counter
    c = Counter('gallahad')                 # a new counter from an iterable
    c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
    c = Counter(cats=4, dogs=8)             # a new counter from keyword args
    
    # 使用 del 来删除它
    del c['sausage']
    
    # elements: 返回一个迭代器，其中每个元素将重复出现计数值所指定次。 元素会按首次出现的顺序返回。 如果一个元素的计数值小于一，elements() 将会忽略它。
    c = Counter(a=4, b=2, c=0, d=-2)
    sorted(c.elements()) # ['a', 'a', 'a', 'a', 'b', 'b']
    
    # most_common([n]):返回一个列表，其中包含 n 个最常见的元素及出现次数, n为空则返回所有元素
    Counter('abracadabra').most_common(3) # [('a', 5), ('b', 2), ('r', 2)]
    # subtract([iterable-or-mapping]) 从 迭代对象 或 映射对象 减去元素。像 dict.update() 但是是减去，而不是替换。输入和输出都可以是0或者负数。
    c = Counter(a=4, b=2, c=0, d=-2)
    d = Counter(a=1, b=2, c=3, d=4)
    c.subtract(d) # ({'a': 3, 'b': 0, 'c': -3, 'd': -6})
    # total() 计算总数值
    c = Counter(a=10, b=5, c=0)
    c.total() # 15
```

## 二分查找库函数  bisect

[文档](https://docs.python.org/zh-cn/3.10/library/bisect.html)
[代码](https://github.com/python/cpython/tree/3.10/Lib/bisect.py)

```bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)```

在 a 中找到 x 合适的插入点以维持有序。参数 lo 和 hi 可以被用于确定需要考虑的子集；默认情况下整个列表都会被使用。如果 x 已经在 a 里存在，那么插入点会在已存在元素之前（也就是左边）。如果 a 是列表（list）的话，返回值是可以被放在 list.insert() 的第一个参数的。
返回的插入点 i 将数组 a 分成两半，使得 all(val < x for val in a[lo : i]) 在左半边而 all(val >= x for val in a[i : hi]) 在右半边。
key specifies a key function of one argument that is used to extract a comparison key from each element in the array. To support searching complex records, the key function is not applied to the x value.
If key is None, the elements are compared directly with no intervening function call.
在 3.10 版更改: 增加了 key 形参。

```bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)```

```bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)```
类似于 bisect_left()，但是返回的插入点是 a 中已存在元素 x 的右侧。
返回的插入点 i 将数组 a 分成两半，使得左半边为 all(val <= x for val in a[lo : i]) 而右半边为 all(val > x for val in a[i : hi])。
key specifies a key function of one argument that is used to extract a comparison key from each element in the array. To support searching complex records, the key function is not applied to the x value.
If key is None, the elements are compared directly with no intervening function call.
在 3.10 版更改: 增加了 key 形参。

```bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)```
按照已排序顺序将 x 插入到 a 中。
此函数首先会运行 bisect_left() 来定位一个插入点。 然后，它会在 a 上运行 insert() 方法在正确的位置插入 x 以保持排序顺序。
To support inserting records in a table, the key function (if any) is applied to x for the search step but not for the insertion step.
请记住 O(log n) 搜索是由缓慢的 O(n) 抛入步骤主导的。
在 3.10 版更改: 增加了 key 形参。

```bisect.insort_right(a, x, lo=0, hi=len(a), *, key=None)```

```bisect.insort(a, x, lo=0, hi=len(a), *, key=None)```

类似于 insort_left()，但是把 x 插入到 a 中已存在元素 x 的右侧。
此函数首先会运行 bisect_right() 来定位一个插入点。 然后，它会在 a 上运行 insert() 方法在正确的位置插入 x 以保持排序顺序。
To support inserting records in a table, the key function (if any) is applied to x for the search step but not for the insertion step.
请记住 O(log n) 搜索是由缓慢的 O(n) 抛入步骤主导的。

### 搜索有序列表

上面的 bisect() 函数对于找到插入点是有用的，但在一般的搜索任务中可能会有点尴尬。下面 5 个函数展示了如何将其转变成有序列表中的标准查找函数

```python
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
```

### 例子

函数 bisect() 还可以用于数字表查询。这个例子是使用 bisect() 从一个给定的考试成绩集合里，通过一个有序数字表，查出其对应的字母等级：90 分及以上是 'A'，80 到 89 是 'B'，以此类推

```python
>>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
...     i = bisect(breakpoints, score)
...     return grades[i]
...
>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
['F', 'A', 'C', 'C', 'B', 'A', 'A']
```

`bisect()` 和 `insort()`函数也对`tuple`适用，key参数可用于提取用于对表中的记录排序的字段：

```python
>>> from collections import namedtuple
>>> from operator import attrgetter
>>> from bisect import bisect, insort
>>> from pprint import pprint

>>> Movie = namedtuple('Movie', ('name', 'released', 'director'))

>>> movies = [
...     Movie('Jaws', 1975, 'Speilberg'),
...     Movie('Titanic', 1997, 'Cameron'),
...     Movie('The Birds', 1963, 'Hitchcock'),
...     Movie('Aliens', 1986, 'Scott')
... ]

>>> # Find the first movie released on or after 1960
>>> by_year = attrgetter('released')
>>> movies.sort(key=by_year)
>>> movies[bisect(movies, 1960, key=by_year)]
Movie(name='The Birds', released=1963, director='Hitchcock')

>>> # Insert a movie while maintaining sort order
>>> romance = Movie('Love Story', 1970, 'Hiller')
>>> insort(movies, romance, key=by_year)
>>> pprint(movies)
[Movie(name='The Birds', released=1963, director='Hitchcock'),
 Movie(name='Love Story', released=1970, director='Hiller'),
 Movie(name='Jaws', released=1975, director='Speilberg'),
 Movie(name='Aliens', released=1986, director='Scott'),
 Movie(name='Titanic', released=1997, director='Cameron')]
```

如果key函数开销很大，可以通过搜索预先计算的键列表来找到记录的索引，从而避免重复调用函数

```python
>>> data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
>>> data.sort(key=lambda r: r[1])       # Or use operator.itemgetter(1).
>>> keys = [r[1] for r in data]         # Precompute a list of keys.
>>> data[bisect_left(keys, 0)]
('black', 0)
>>> data[bisect_left(keys, 1)]
('blue', 1)
>>> data[bisect_left(keys, 5)]
('red', 5)
>>> data[bisect_left(keys, 8)]
('yellow', 8)
```

## itertools 为高效循环而创建的迭代器函数

[docs](https://docs.python.org/zh-cn/3/library/itertools.html)
[详解](https://zhuanlan.zhihu.com/p/396290992)

### 无穷迭代器

| 迭代器 | 实参 | 结果 | 示例 |
| --- | --- | --- | --- |
| count() |start, [step] |start, start+step, start+2*step, ... |count(10) --> 10,11 12 13 14 ... |
| cycle() | p | p0, p1, ... plast, p0, p1, ... | cycle('ABCD') --> A B C D A B C D ... |
| repeat() | elem [,n] |elem, elem, elem, ... 重复无限次或n次 | repeat(10, 3) --> 10 10 10 |

### 根据最短输入序列长度停止的迭代器：

| 迭代器 | 实参 | 结果 | 示例 |
| --- | --- | --- | --- |
| accumulate() | p [,func] | p0, p0+p1, p0+p1+p2, ... | accumulate([1,2,3,4,5]) --> 1 3 6 10 15 |
| chain() | p, q, ... | p0, p1, ... plast, q0, q1, ... | chain('ABC', 'DEF') --> A B C D E F |
| chain.from_iterable() | iterable -- 可迭代对象 | p0, p1, ... plast, q0, q1, ... | chain.from_iterable(['ABC', 'DEF']) --> A B C D E F |
| compress() | data, selectors |  (d[0] if s[0]), (d[1] if s[1]), ... | compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F |
| dropwhile() | pred, seq | seq[n], seq[n+1], ... 从pred首次真值测试失败开始 | dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1 |
| filterfalse() | pred, seq | seq中pred(x)为假值的元素，x是seq中的元素。 |filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8 |
| groupby() | iterable[, key] | 根据key(v)值分组的迭代器 | |
| islice() | seq, [start,] stop [, step] | seq[start:stop:step]中的元素 | islice('ABCDEFG', 2, None) --> C D E F G |
| pairwise() | iterable -- 可迭代对象 | (p[0], p[1]), (p[1], p[2]) | pairwise('ABCDEFG') --> AB BC CD DE EF FG |
| starmap() | func, seq | func(*seq[0]), func(*seq[1]), ... | starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000 |
| takewhile() | pred, seq | seq[0], seq[1], ..., 直到pred真值测试失败 | takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4 |
| tee() | it, n | it1, it2, ... itn 将一个迭代器拆分为n个迭代器 | |
| zip_longest() | p, q, ... | (p[0], q[0]), (p[1], q[1]), ... | zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D- |

### 排列组合迭代器：

| 迭代器 | 实参 | 结果 |
| --- | --- | --- |
| product() | p, q, ... [repeat=1] | 笛卡尔积，相当于嵌套的for循环 |
| permutations() | p[, r] | 长度r元组，所有可能的排列，无重复元素 |
| combinations() | p, r | 长度r元组，有序，无重复元素 |
| combinations_with_replacement() | p, r | 长度r元组，有序，元素可重复 |

| 例子 | 结果 |
| --- | --- |
| product('ABCD', repeat=2) | AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD |
| permutations('ABCD', 2) | AB AC AD BA BC BD CA CB CD DA DB DC |
| combinations('ABCD', 2) | AB AC AD BC BD CD |
| combinations_with_replacement('ABCD', 2) | AA AB AC AD BB BC BD CC CD DD |

### `itertools.accumulate(iterable[, func, *, initial=None])`

创建一个迭代器，返回累积汇总值或其他双目运算函数的累积结果值（通过可选的 func 参数指定）。
如果提供了 func，它应当为带有两个参数的函数。 输入 iterable 的元素可以是能被 func 接受为参数的任意类型。 （例如，对于默认的加法运算，元素可以是任何可相加的类型包括 Decimal 或 Fraction。）
通常，输出的元素数量与输入的可迭代对象是一致的。 但是，如果提供了关键字参数 initial，则累加会以 initial 值开始，这样输出就比输入的可迭代对象多一个元素。

```python
def accumulate(iterable, func=operator.add, *, initial=None):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total

>>> data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
>>> list(accumulate(data, operator.mul))     # running product
[3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
>>> list(accumulate(data, max))              # running maximum
[3, 4, 6, 6, 6, 9, 9, 9, 9, 9]

# Amortize a 5% loan of 1000 with 4 annual payments of 90
>>> cashflows = [1000, -90, -90, -90, -90]
>>> list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt))
[1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]

# Chaotic recurrence relation https://en.wikipedia.org/wiki/Logistic_map
>>> logistic_map = lambda x, _:  r * x * (1 - x)
>>> r = 3.8
>>> x0 = 0.4
>>> inputs = repeat(x0, 36)     # only the initial value is used
>>> [format(x, '.2f') for x in accumulate(inputs, logistic_map)]
['0.40', '0.91', '0.30', '0.81', '0.60', '0.92', '0.29', '0.79', '0.63',
 '0.88', '0.39', '0.90', '0.33', '0.84', '0.52', '0.95', '0.18', '0.57',
 '0.93', '0.25', '0.71', '0.79', '0.63', '0.88', '0.39', '0.91', '0.32',
 '0.83', '0.54', '0.95', '0.20', '0.60', '0.91', '0.30', '0.80', '0.60']

>>> import itertools
>>> x = itertools.accumulate(range(5))
>>> print(list(x))
[0, 1, 3, 6, 10]
```

### itertools.chain(*iterables)

创建一个迭代器，它首先返回第一个可迭代对象中所有元素，接着返回下一个可迭代对象中所有元素，直到耗尽所有可迭代对象中的元素。可将多个序列处理为单个序列。大致相当于：

```python
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

```

### classmethod chain.from_iterable(iterable)

构建类似 chain() 迭代器的另一个选择。从一个单独的可迭代参数中得到链式输入，该参数是延迟计算的。大致相当于：

```python
def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

```

### itertools.combinations(iterable, r)

返回由输入 iterable 中元素组成长度为 r 的子序列。
组合元组会以字典顺序根据所输入 iterable 的顺序发出。 因此，如果所输入 iterable 是已排序的，组合元组也将按已排序的顺序生成。
即使元素的值相同，不同位置的元素也被认为是不同的。如果元素各自不同，那么每个组合中没有重复元素。
大致相当于：

```python
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
# combinations() 的代码可被改写为 permutations() 过滤后的子序列，（相对于元素在输入中的位置）元素不是有序的。
def combinations(iterable, r):
    # 当 0 <= r <= n 时，返回项的个数是 n! / r! / (n-r)!；当 r > n 时，返回项个数为0
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

>>> x = itertools.combinations(range(3),2)
>>> print(list(x))

[(0, 1), (0, 2), (1, 2)]

```

### itertools.combinations_with_replacement(iterable, r)

返回由输入 iterable 中元素组成的长度为 r 的子序列，允许每个元素可重复出现。
组合元组会以字典顺序根据所输入 iterable 的顺序发出。 因此，如果所输入 iterable 是已排序的，组合元组也将按已排序的顺序生成。
不同位置的元素是不同的，即使它们的值相同。因此如果输入中的元素都是不同的话，返回的组合中元素也都会不同。
大致相当于：

```python
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

>>> x = itertools.combinations_with_replacement(range(3),2)
>>> print(list(x))

[(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
```

combinations_with_replacement() 的代码可被改写为 production() 过滤后的子序列，（相对于元素在输入中的位置）元素不是有序的。

```python
# 当 n > 0 时，返回项个数为 (n+r-1)! / r! / (n-1)!
def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
```

### itertools.compress(data, selectors)

创建一个迭代器，它返回 data 中经 selectors 真值测试为 True 的元素。迭代器在两者较短的长度处停止。大致相当于：

```python
def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    return (d for d, s in zip(data, selectors) if s)

>>> x = itertools.compress(range(3),(True,False,False))
>>> print(list(x))

[0]

# 也支持其他类型的真值比如：0,1
>>> x = itertools.compress(range(3),(1,0,0))
>>> print(list(x))

[0]
```

### itertools.count(start=0, step=1)

创建一个迭代器，它从 start 值开始，返回均匀间隔的值。常用于 map() 中的实参来生成连续的数据点。此外，还用于 zip() 来添加序列号。大致相当于：

```python
# 当对浮点数计数时，替换为乘法代码有时精度会更好，例如： (start + step * i for i in count()) 。
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

>>> x = itertools.count(start=10,step=2)
>>> print(list(itertools.islice(x,0,5,1)))

[10, 12, 14, 16, 18]
```

### itertools.cycle(iterable)

创建一个迭代器，返回 iterable 中所有元素并保存一个副本。当取完 iterable 中所有元素，返回副本中的所有元素。无限重复。大致相当于：

```python
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

>>> x = itertools.cycle([0,1,2])
>>> print(list(itertools.islice(x,0,5,2)))

[0, 2, 1]
```

### itertools.dropwhile(predicate, iterable)

创建一个迭代器，如果 predicate 为true，迭代器丢弃这些元素，然后返回其他元素。注意，迭代器在 predicate 首次为false之前不会产生任何输出，所以可能需要一定长度的启动时间。大致相当于：

```python
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x

>>> x = itertools.dropwhile(lambda x: x > 5, [8,6,4,2])
>>> print(list(x))

[4, 2]
```

### itertools.groupby(iterable, key=None)

创建一个迭代器，返回 iterable 中连续的键和组。key 是一个计算元素键值函数。如果未指定或为 None，key 缺省为恒等函数（identity function），返回元素不变。一般来说，iterable 需用同一个键值函数预先排序。
groupby() 操作类似于Unix中的 uniq。当每次 key 函数产生的键值改变时，迭代器会分组或生成一个新组（这就是为什么通常需要使用同一个键值函数先对数据进行排序）。这种行为与SQL的GROUP BY操作不同，SQL的操作会忽略输入的顺序将相同键值的元素分在同组中。
返回的组本身也是一个迭代器，它与 groupby() 共享底层的可迭代对象。因为源是共享的，当 groupby() 对象向后迭代时，前一个组将消失。因此如果稍后还需要返回结果，可保存为列表：

```python
groups = []
uniquekeys = []
data = sorted(data, key=keyfunc)
for k, g in groupby(data, keyfunc):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
```

groupby() 大致相当于：

```python
class groupby:
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def __next__(self):
        self.id = object()
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey, self.id))
    def _grouper(self, tgtkey, id):
        while self.id is id and self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)

>>> x = [{"a":1},{"a":2},{"a":3}]
>>> x = itertools.groupby(x,lambda y: y['a']<=2)
>>> for name,group in x:
...    print(name,group)

True [{'a': 1}, {'a': 2}]
False [{'a': 3}]
```

### itertools.islice(iterable, stop)

itertools.islice(iterable, start, stop[, step])

创建一个迭代器，返回从 iterable 里选中的元素。如果 start 不是0，跳过 iterable 中的元素，直到到达 start 这个位置。之后迭代器连续返回元素，除非 step 设置的值很高导致被跳过。如果 stop 为 None，迭代器耗光为止；否则，在指定的位置停止。与普通的切片不同，islice() 不支持将 start ， stop ，或 step 设为负值。可用来从内部数据结构被压平的数据中提取相关字段（例如一个多行报告，它的名称字段出现在每三行上）。大致相当于：

```python
# 如果 start 为 None，迭代从0开始。如果 step 为 None ，步长缺省为1。
def islice(iterable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    start, stop, step = s.start or 0, s.stop or sys.maxsize, s.step or 1
    it = iter(range(start, stop, step))
    try:
        nexti = next(it)
    except StopIteration:
        # Consume *iterable* up to the *start* position.
        for i, element in zip(range(start), iterable):
            pass
        return
    try:
        for i, element in enumerate(iterable):
            if i == nexti:
                yield element
                nexti = next(it)
    except StopIteration:
        # Consume to *stop*.
        for i, element in zip(range(i + 1, stop), iterable):
            pass

>>> x = itertools.islice(range(20),0,11,3)
>>> print(list(x))

[0, 3, 6, 9]
```

### itertools.pairwise(iterable)

返回从输入 iterable 中获取的连续重叠对。
输出迭代器中 2 元组的数量将比输入的数量少一个。 如果输入可迭代对象中少于两个值则它将为空。
大致相当于：

```python
def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
```

### itertools.permutations(iterable, r=None)

连续返回由 iterable 元素生成长度为 r 的排列。
如果 r 未指定或为 None ，r 默认设置为 iterable 的长度，这种情况下，生成所有全长排列。
排列元组会以字典顺序根据所输入 iterable 的顺序发出。 因此，如果所输入 iterable 是已排序的，组合元组也将按已排序的顺序生成。
即使元素的值相同，不同位置的元素也被认为是不同的。如果元素值都不同，每个排列中的元素值不会重复。
大致相当于：

```python
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
```

permutations() 的代码也可被改写为 product() 的子序列，只要将含有重复元素（来自输入中同一位置的）的项排除。

```python
# 当 0 <= r <= n ，返回项个数为 n! / (n-r)! ；当 r > n ，返回项个数为0。
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
```

### itertools.product(*iterables, repeat=1)

可迭代对象输入的笛卡儿积。
大致相当于生成器表达式中的嵌套循环。例如， product(A, B) 和 ((x,y) for x in A for y in B) 返回结果一样。
嵌套循环像里程表那样循环变动，每次迭代时将最右侧的元素向后迭代。这种模式形成了一种字典序，因此如果输入的可迭代对象是已排序的，笛卡尔积元组依次序发出。
要计算可迭代对象自身的笛卡尔积，将可选参数 repeat 设定为要重复的次数。例如，product(A, repeat=4) 和 product(A, A, A, A) 是一样的。
该函数大致相当于下面的代码，只不过实际实现方案不会在内存中创建中间结果。

```python
# 在 product() 运行之前，它会完全耗尽输入的可迭代对象，在内存中保留值的临时池以生成结果积。 相应地，它只适用于有限的输入。
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

>>> a = (1,2,3)
>>> b = ('a','b')
>>> x = itertools.product(a,b)
>>> print(list(x))

[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
```

### itertools.repeat(object[, times])

创建一个迭代器，不断重复 object 。除非设定参数 times ，否则将无限重复。可用于 map() 函数中的参数，被调用函数可得到一个不变参数。也可用于 zip() 的参数以在元组记录中创建一个不变的部分。
大致相当于：

```python
def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object

# repeat 最常见的用途就是在 map 或 zip 提供一个常量流：
>>> list(map(pow, range(10), repeat(2)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> x = itertools.repeat(1,4)
>>> print(list(x))

[1, 1, 1, 1]
```

### itertools.starmap(function, iterable)

创建一个迭代器，使用从可迭代对象中获取的参数来计算该函数。当参数对应的形参已从一个单独可迭代对象组合为元组时（数据已被“预组对”）可用此函数代替 map()。map() 与 starmap() 之间的区别可以类比 function(a,b) 与 function(*c) 的区别。大致相当于:

```python
def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)
>>> li =[(2, 3), (3, 1), (4, 6), (5, 3), (6, 5), (7, 2)]
>>> list(itertools.starmap(lambda x,y: x+y, li))

[5, 4, 10, 8, 11, 9]


>>> list(map(lambda x,y: x+y, li))

TypeError: <lambda>() missing 1 required positional argument: 'y'


>>> list(map(lambda x , y : x ** y, [2,4,6],[3,2,1]))

[8, 16, 6]
```

### itertools.takewhile(predicate, iterable)

创建一个迭代器，只要 predicate 为真就从可迭代对象中返回元素。大致相当于:

```python
def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
```

### itertools.tee(iterable, n=2)

从一个可迭代对象中返回 n 个独立的迭代器。
下面的Python代码能帮助解释 tee 做了什么（尽管实际的实现更复杂，而且仅使用了一个底层的 FIFO 队列）。
大致相当于：

```python
def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                try:
                    newval = next(it)   # fetch a new value and
                except StopIteration:
                    return
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)

# 这是一个爆炸内存的神奇QAQ
>>> x = itertools.tee(range(5),2)
>>> print([list(x) for x in x])

[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

一旦 tee() 实施了一次分裂，原有的 iterable 不应再被使用；否则tee对象无法得知 iterable 可能已向后迭代。
tee 迭代器不是线程安全的。当同时使用由同一个 tee() 调用所返回的迭代器时可能引发 RuntimeError，即使原本的 iterable 是线程安全的。
该迭代工具可能需要相当大的辅助存储空间（这取决于要保存多少临时数据）。通常，如果一个迭代器在另一个迭代器开始之前就要使用大部份或全部数据，使用 list() 会比 tee() 更快。

### itertools.zip_longest(*iterables, fillvalue=None)

创建一个迭代器，从每个可迭代对象中收集元素。如果可迭代对象的长度未对齐，将根据 fillvalue 填充缺失值。迭代持续到耗光最长的可迭代对象。大致相当于：

```python
def zip_longest(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)

>>> x = itertools.zip_longest(range(3),range(5))
>>> print(list(x))

[(0, 0), (1, 1), (2, 2), (None, 3), (None, 4)]


>>> x = zip(range(3),range(5))
>>> print(list(x))

[(0, 0), (1, 1), (2, 2)]
```

如果其中一个可迭代对象有无限长度，zip_longest() 函数应封装在限制调用次数的场景中（例如 islice() 或 takewhile()）。除非指定， fillvalue 默认为 None 。
