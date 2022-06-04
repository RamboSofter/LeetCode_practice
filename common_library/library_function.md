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