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

deque类

```python
class collections.deque([iterable[, maxlen]])
    '''双向队列对象
    从左到右初始化(用方法 append()) ，从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。
    Deque队列是由栈或者queue队列生成的
    '''
    append(x) # 添加 x 到右端。

    appendleft(x) # 添加 x 到左端。 

    clear() # 移除所有元素，使其长度为0.

    copy() # 创建一份浅拷贝。

    count(x) # 计算 deque 中元素等于 x 的个数。

    extend(iterable) # 扩展deque的右侧，通过添加iterable参数中的元素。
    
    # 扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。
    extendleft(iterable)

    # 返回 x 在 deque 中的位置（在索引 start 之后，索引 stop 之前）。 返回第一个匹配项，如果未找到则引发 ValueError。
    index(x[, start[, stop]])

    insert(i, x) # 在位置 i 插入 x  如果插入会导致一个限长 deque 超出长度 maxlen 的话，就引发一个 IndexError。

    pop() # 移去并且返回一个元素，deque 最右侧的那一个。 如果没有元素的话，就引发一个 IndexError。

    popleft() # 移去并且返回一个元素，deque 最左侧的那一个。 如果没有元素的话，就引发 IndexError。
    
    remove(value) # 移除找到的第一个 value。 如果没有的话就引发 ValueError。
    
    reverse() # 将deque逆序排列。返回 None 。

    rotate(n=1) # 向右循环移动 n 步。 如果 n 是负数，就向左循环。
    
    # 如果deque不是空的，向右循环移动一步就等价于 d.appendleft(d.pop()) ， 向左循环一步就等价于 d.append(d.popleft()) 。

    maxlen # Deque的最大尺寸，如果没有限定的话就是 None 。

>>> from collections import deque
>>> d = deque('ghi')                 # make a new deque with three items
>>> for elem in d:                   # iterate over the deque's elements
...     print(elem.upper())
G
H
I

>>> d.append('j')                    # add a new entry to the right side
>>> d.appendleft('f')                # add a new entry to the left side
>>> d                                # show the representation of the deque
deque(['f', 'g', 'h', 'i', 'j'])

>>> d.pop()                          # return and remove the rightmost item
'j'
>>> d.popleft()                      # return and remove the leftmost item
'f'
>>> list(d)                          # list the contents of the deque
['g', 'h', 'i']
>>> d[0]                             # peek at leftmost item
'g'
>>> d[-1]                            # peek at rightmost item
'i'

>>> list(reversed(d))                # list the contents of a deque in reverse
['i', 'h', 'g']
>>> 'h' in d                         # search the deque
True
>>> d.extend('jkl')                  # add multiple elements at once
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])
>>> d.rotate(1)                      # right rotation
>>> d
deque(['l', 'g', 'h', 'i', 'j', 'k'])
>>> d.rotate(-1)                     # left rotation
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])

>>> deque(reversed(d))               # make a new deque in reverse order
deque(['l', 'k', 'j', 'i', 'h', 'g'])
>>> d.clear()                        # empty the deque
>>> d.pop()                          # cannot pop from an empty deque
Traceback (most recent call last):
    File "<pyshell#6>", line 1, in -toplevel-
        d.pop()
IndexError: pop from an empty deque

>>> d.extendleft('abc')              # extendleft() reverses the input order
>>> d
deque(['c', 'b', 'a'])
```

defaultdict类

```python
class collections.defaultdict(default_factory=None, /[, ...])
    '''返回一个新的类似字典的对象。 defaultdict 是内置 dict 类的子类。
    本对象包含一个名为 default_factory 的属性，构造时，第一个参数用于为该属性提供初始值，默认为 None。所有其他参数（包括关键字参数）都相当于传递给 dict 的构造函数。
    defaultdict 对象除了支持标准 dict 的操作，还支持以下方法作为扩展：
    '''
    __missing__(key)
    # 如果 default_factory 属性为 None，则调用本方法会抛出 KeyError 异常，附带参数 key。

class dict(iterable, **kwargs)
    list(d) # 返回字典 d 中使用的所有键的列表。
    
    len(d) #  返回字典 d 中的项数。
    
    d[key] # 返回 d 中以 key 为键的项。 如果映射中不存在 key 则会引发 KeyError。
    
    d[key] = value # 将 d[key] 设为 value。

    del d[key] #  将 d[key] 从 d 中移除。 如果映射中不存在 key 则会引发 KeyError。
    
    key in d #  如果 d 中存在键 key 则返回 True，否则返回 False。

    key not in d # 等价于 not key in d。   

    iter(d) # 返回以字典的键为元素的迭代器。 这是 iter(d.keys()) 的快捷方式。
    
    clear() # 移除字典中的所有元素。
    

    copy() #  返回原字典的浅拷贝。
    
    get(key[, default]) # 如果 key 存在于字典中则返回 key 的值，否则返回 default。 如果 default 未给出则默认为 None，因而此方法绝不会引发 KeyError。
    
    items() # 返回由字典项 ((键, 值) 对) 组成的一个新视图。 参见 视图对象文档。
    

    keys() #  返回由字典键组成的一个新视图。 参见 视图对象文档。

    pop(key[, default]) # 如果 key 存在于字典中则将其移除并返回其值，否则返回 default。 如果 default 未给出且 key 不存在于字典中，则会引发 KeyError。
    

    popitem() # 从字典中移除并返回一个 (键, 值) 对。 键值对会按 LIFO 的顺序被返回。
    

    popitem() # 适用于对字典进行消耗性的迭代，这在集合算法中经常被使用。 如果字典为空，调用 popitem() 将引发 KeyError。

    reversed(d) # 返回一个逆序获取字典键的迭代器。 这是 reversed(d.keys()) 的快捷方式。

    setdefault(key[, default]) # 如果字典存在键 key ，返回它的值。如果不存在，插入值为 default 的键 key ，并返回 default 。 default 默认为 None。
    
    update([other]) # 使用来自 other 的键/值对更新字典，覆盖原有的键。 返回 None。
    
    update() # 接受另一个字典对象，或者一个包含键/值对（以长度为二的元组或其他可迭代对象表示）的可迭代对象。 如果给出了关键字参数，则会以其所指定的键/值对更新字典: d.update(red=1, blue=2)。

    values() # 返回由字典值组成的一个新视图。 
```

